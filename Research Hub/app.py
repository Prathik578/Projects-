import os
import sqlite3
from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from helpers import login_required

# Initialize Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = "cs50_rocks_dude"  # Secret key for sessions
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # Max 16MB per file
app.config['TRAP_HTTP_EXCEPTIONS'] = False
ALLOWED_EXTENSIONS = {"pdf"}

# Ensure upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Helper: Check if file is a valid PDF


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Helper: Connect to DB


def get_db_connection():
    conn = sqlite3.connect("researchhub.db")
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn

# Route: Home Page


@app.route("/")
def index():
    return render_template("index.html")

# Route: Register


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Username and password required", "danger")
            return redirect("/register")

        conn = get_db_connection()
        user = conn.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()

        if user:
            flash("Username already taken", "warning")
            return redirect("/register")

        conn.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                     (username, generate_password_hash(password)))
        conn.commit()
        flash("Registered! Please log in.", "success")
        return redirect("/login")

    return render_template("register.html")

# Route: Login


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

        if not user or not check_password_hash(user["hash"], password):
            flash("Invalid username or password", "danger")
            return redirect("/login")

        session["user_id"] = user["id"]  # Log them in
        flash("Logged in!", "success")
        return redirect("/dashboard")

    return render_template("login.html")

# Route: Logout


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# Route: Dashboard (Protected)


@app.route("/dashboard")
@login_required
def dashboard():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("dashboard.html")

# Route: Upload Paper (Protected)


@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        file = request.files.get("file")
        title = request.form.get("title")
        authors = request.form.get("authors")
        year = request.form.get("year")
        abstract = request.form.get("abstract")

        if not file or file.filename == "" or not title or not authors:
            flash("Missing required fields", "danger")
            return redirect("/upload")

        if file and allowed_file(file.filename):
            # Secure the filename and make it unique
            original_name = file.filename
            safe_name = secure_filename(original_name)
            unique_name = f"{session['user_id']}_{safe_name}"

            # Save file to disk
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], unique_name))

            # Save info to DB
            conn = get_db_connection()
            conn.execute("""
                INSERT INTO papers (user_id, title, authors, year, abstract, filename, original_filename)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (session["user_id"], title, authors, year, abstract, unique_name, original_name))
            conn.commit()

            flash("Paper uploaded successfully!", "success")
            return redirect("/library")
        else:
            flash("Invalid file. Only PDFs allowed.", "danger")
            return redirect("/upload")

    return render_template("upload.html")

# Route: Library (View Papers)


@app.route("/library")
@login_required
def library():
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    query = request.args.get("q", "")

    if query:
        # Search logic
        papers = conn.execute("""
            SELECT * FROM papers
            WHERE user_id = ? AND (title LIKE ? OR authors LIKE ?)
        """, (session["user_id"], f"%{query}%", f"%{query}%")).fetchall()
    else:
        papers = conn.execute("SELECT * FROM papers WHERE user_id = ?",
                              (session["user_id"],)).fetchall()

    return render_template("library.html", papers=papers)


@app.route("/delete/<int:paper_id>", methods=["POST"])
@login_required
def delete(paper_id):
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    # CRITICAL: Ensure the paper belongs to the logged-in user
    paper = conn.execute("SELECT filename FROM papers WHERE id = ? AND user_id = ?",
                         (paper_id, session["user_id"])).fetchone()

    if paper:
        # Delete file from disk
        os.remove(os.path.join(app.config["UPLOAD_FOLDER"], paper["filename"]))
        # Delete row from DB
        conn.execute("DELETE FROM papers WHERE id = ? AND user_id = ?",
                     (paper_id, session["user_id"]))
        conn.commit()
        flash("Paper deleted.", "success")
    else:
        flash("Paper not found or unauthorized.", "danger")

    return redirect("/library")


@app.route("/uploads/<filename>")
@login_required
def uploaded_file(filename):
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    # Verify ownership before serving
    paper = conn.execute("SELECT id FROM papers WHERE filename = ? AND user_id = ?",
                         (filename, session["user_id"])).fetchone()

    if paper:
        return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
    else:
        return "Unauthorized", 403


# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return render_template("error/404.html"), 404


@app.errorhandler(403)
def forbidden(error):
    return render_template("error/403.html"), 403


@app.errorhandler(500)
def internal_error(error):
    # Optional: Rollback database session if needed
    # db.session.rollback()
    return render_template("error/500.html"), 500


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error/404.html"), 404


if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)

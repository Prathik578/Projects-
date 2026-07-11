from functools import wraps
from flask import session, redirect, url_for, flash, render_template


def login_required(f):
    """
    Decorate routes to require login.
    If user is not logged in, redirect to login page.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to access this page.", "warning")
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def apology(message, code=400):
    """Render message as an apology to user."""
    return render_template("error.html", message=message, code=code), code

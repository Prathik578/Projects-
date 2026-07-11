# ResearchHub

> A modern web application for managing personal research papers, built as the final project for Harvard University's CS50x: Introduction to Computer Science.

---

#### Video demo: <https://drive.google.com/drive/folders/1fO8S5eRe_PcSPxSHe0BZHxEayAAC8was>

## Overview

ResearchHub is a Flask-based web application that enables users to build and organize their own digital research library. The application allows authenticated users to upload research papers, store metadata, search through their collection, edit existing entries, and remove papers when they are no longer needed.

The objective of this project was to apply the concepts learned throughout CS50x by building a complete full-stack web application from scratch using Python, Flask, SQLite, HTML, CSS, JavaScript, and Bootstrap.

---

## Features

### User Authentication
- Secure user registration
- User login and logout
- Password hashing using Werkzeug
- Session-based authentication

### Research Paper Management
- Upload PDF research papers
- Store paper metadata:
  - Title
  - Authors
  - Publication Year
  - Abstract
- View uploaded papers
- Edit paper information
- Delete papers

### Personal Library
- Private paper collection for each user
- Papers are associated with the logged-in account
- Easy navigation through the research library

### Search
- Search papers by title
- Search papers by author
- Quickly locate research papers

### User Interface
- Responsive Bootstrap layout
- Clean academic-inspired design
- Custom styling
- Custom error pages

---

# Technology Stack

## Backend

- Python
- Flask

## Database

- SQLite

## Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap 5

## Libraries

- Flask
- Flask-Session
- Werkzeug
- CS50 SQL Library

---

# Project Structure

```
ResearchHub/
│
├── app.py
├── helpers.py
├── schema.sql
├── requirements.txt
├── README.md
│
├── uploads/
│
├── instance/
│   └── research.db
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   └── img/
│
└── templates/
    ├── layout.html
    ├── index.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── upload.html
    ├── library.html
    └── error/
        |── 400.html
        |── 500.html
        |── 403.html
        |── 404.html
```

---

# Database Design

The application uses two primary database tables.

## Users

Stores user account information.

| Column | Description |
|---------|-------------|
| id | Primary Key |
| username | Unique username |
| hash | Hashed password |

---

## Papers

Stores uploaded research paper information.

| Column | Description |
|---------|-------------|
| id | Primary Key |
| user_id | Owner of the paper |
| title | Paper title |
| authors | Authors |
| year | Publication year |
| abstract | Paper abstract |
| filename | Uploaded PDF filename |
| uploaded_at | Upload timestamp |

Each paper belongs to a specific user through the `user_id` foreign key, ensuring users can only access their own research papers.

---

# How It Works

1. Users register for a new account or log in.
2. After authentication, they are redirected to their personal dashboard.
3. Users upload PDF research papers together with metadata.
4. The uploaded file is stored on the server while metadata is stored in the SQLite database.
5. Users can browse their personal library.
6. Search functionality allows users to quickly locate papers.
7. Papers can be edited or removed at any time.

---

# Skills Demonstrated

This project combines many of the concepts taught throughout CS50x, including:

- Python programming
- Flask web development
- SQL databases
- User authentication
- Session management
- File uploads
- HTML templates with Jinja
- CSS styling
- JavaScript interactions
- CRUD operations
- Software architecture
- Database design

---

# Installation

Clone the repository:

```bash
git clone <Research Hub>
cd ResearchHub
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize the database:

```bash
sqlite3 instance/research.db < schema.sql
```

Run the application:

```bash
flask run
```

How to Open your browser:

so you can download this code and then run the flask server in the folder of Research Hub

---

# Future Improvements

Some planned improvements include:

- AI-generated paper summaries
- Automatic keyword extraction
- Citation generation
- Tags and categories
- Reading progress
- Notes and annotations
- Dark mode
- Cloud storage integration
- Collaboration features
- Public researcher profiles

---

# Lessons Learned

Building ResearchHub was an opportunity to apply nearly every major topic covered in CS50x. Beyond programming, this project reinforced the importance of planning, debugging, database design, application architecture, and breaking large problems into smaller, manageable components.

This project represents my first complete full-stack web application developed from an initial idea through planning, implementation, testing, and deployment.

---

# Author

**Prathik**

CS50x Final Project (2026)

---

# Acknowledgements

This project was created as the final project for **Harvard University's CS50x: Introduction to Computer Science**.

Special thanks to Professor David J. Malan and the entire CS50 teaching team for creating an exceptional course that inspired me to continue exploring computer science and software engineering also, I have used AI called Chatgpt and copilot to plan the folder structure and for debugging code but the rest of it is planned and executed by me.


import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
comments = []


def add_comment(username, comment):
    # add new comment
    comments.append({"from": username, "comment": comment})


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_books", methods=["GET", "POST"])
def get_books():
    books = mongo.db.books.find()
    return render_template("books.html", books=books)
    #1st books gets passed to genre.html 
    #2nd books is the variable defined here and what's being returned from the DB.

def user(username):
    # display new comment
    if request.method == "POST":
        username = session["user"]
        comment = request.form["comment"]
        add_comment(username, comment)
        return redirect(url_for("book", username=session["user"]))

    return render_template("book.html", username=username,
                           book_comments=comments)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get(
                        "username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Wrong Password. Please try again.")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Wrong Username. Please try again.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
    # displays flash message after the message has been sent.
    # it should return an empty template
        flash("Your message has been sent")
    return render_template("contact.html")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = {
            "book_title": request.form.get("book_title"),
            "book_author": request.form.get("book_author"),
            "genre_name": request.form.get("genre_name"),
            "book_description": request.form.get("book_description"),
            "book_image": request.form.get("book_image"),
            "added_by": session["user"]
        }

        mongo.db.books.insert_one(book)
        flash("Your Book has been Added")
        return redirect(url_for("get_books"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("add_book.html", genres=genres)


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        edition = {
            "book_title": request.form.get("book_title"),
            "book_author": request.form.get("book_author"),
            "genre_name": request.form.get("genre_name"),
            "book_description": request.form.get("book_description"),
            "book_image": request.form.get("book_image"),
            "added_by": session["user"]
        }
        mongo.db.books.update(
            {"_id": ObjectId(book_id)}, edition)
        flash("Your Book Information is Updated")

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("edit_book.html", book=book, genres=genres)


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Your Book is Deleted")
    return redirect(url_for("get_books"))


@app.route("/get_genres")
def get_genres():
    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    return render_template("genres.html", genres=genres)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("get_genres"))

    return render_template("add_genre.html")


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    if request.method == "POST":
        edition = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.update({"_id": ObjectId(genre_id)}, edition)
        flash("Genre is Updated")
        return redirect(url_for("get_genres"))

    genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    mongo.db.genres.remove({"_id": ObjectId(genre_id)})
    flash("Genre is Deleted")
    return redirect(url_for("get_genres"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
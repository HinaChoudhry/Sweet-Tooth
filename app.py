import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_paginate import Pagination, get_page_args
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# Index
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


# Recipes page
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    # The below code has been taken and amended from
    # https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    per_page = 12
    total = len(recipes)
    pagination_recipes = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='materializecss')
    return render_template('recipes.html',
                           recipes=pagination_recipes,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


# Search feature
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    per_page = 12
    total = len(recipes)
    pagination_recipes = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='materializecss')
    return render_template("recipes.html", recipes=pagination_recipes,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
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

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("account", username=session["user"]))

    return render_template("register.html")


# Log in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "account", username=session["user"]))
            else:
                flash("Incorrect Username and/or password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Account page
@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    # this gets the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipes = list(mongo.db.recipes.find({"created_by": username.lower()}))
    if session["user"]:
        return render_template("account.html",
                               username=username, recipes=recipes)

    return redirect(url_for("login"))


# Log out
@app.route("/logout")
def logout():
    # This removes the user from the session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Add recipe feature
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if "user" in session:
        if request.method == "POST":
            recipe = {
                "category_name": request.form.get("category_name"),
                "recipe_name": request.form.get("recipe_name"),
                "description": request.form.get("description"),
                "ingredients": request.form.getlist("ingredients"),
                "method": request.form.getlist("method"),
                "image_url": request.form.get("image_url"),
                "created_by": session["user"]
            }
            mongo.db.recipes.insert_one(recipe)
            flash("Recipe uploaded")
            return redirect(url_for("get_recipes"))
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("upload.html", categories=categories)
    else:
        flash("Log in to use this feature")
        return render_template("403.html")


# Edit recipes
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if "user" in session:
        if request.method == "POST":
            submit = {
                "category_name": request.form.get("category_name"),
                "recipe_name": request.form.get("recipe_name"),
                "description": request.form.get("description"),
                "ingredients": request.form.getlist("ingredients"),
                "method": request.form.getlist("method"),
                "image_url": request.form.get("image_url"),
                "created_by": session["user"]
            }
            mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
            flash("Recipe updated")
            return redirect(url_for("account", username=session["user"]))
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("edit_recipe.html",
                               recipe=recipe, categories=categories)
    else:
        flash("Log in to use this feature")
        return render_template("403.html")


# DElete recipes
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    if "user" in session:
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        flash("Recipe deleted")
        return redirect(url_for("get_recipes"))
    else:
        flash("Log in to use this feature")
        return render_template("403.html")


# Categories feature
@app.route("/get_categories")
def get_categories():
    # The below line and else statement was taken and amended from
    # https://github.com/AmyOShea/MS3-Cocktail-Hour/blob/master/app.py
    if session['user'] == 'admin':
        categories = list(mongo.db.categories.find().sort("category_name", 1))
        return render_template("categories.html", categories=categories)
    else:
        return render_template("403.html")
 

# Add category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if session['user'] == 'admin':
        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name")
            }
            mongo.db.categories.insert_one(category)
            flash("New category added")
            return redirect(url_for("get_categories"))
        return render_template("add_category.html")
    else:
        return render_template("403.html")


# Edit category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if session['user'] == 'admin':
        if request.method == "POST":
            submit = {
                "category_name": request.form.get("category_name")
            }
            mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
            flash("Category Successfully Updated")
            return redirect(url_for("get_categories"))

        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
        return render_template("edit_category.html", category=category)

    else:
        return render_template("403.html")


# Delete category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    if session['user'] == 'admin':
        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        flash("Category deleted")
        return redirect(url_for("get_categories"))
    else:
        return render_template("403.html")


# Full recipe feature
@app.route("/full_recipe/<recipe_id>")
def full_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("full_recipe.html", recipe=recipe)


# Error Handlers

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)

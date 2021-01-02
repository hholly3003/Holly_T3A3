from main import db, bcrypt
from flask import Blueprint, jsonify, request, abort, render_template, url_for, flash, redirect, request
from models.User import User
from schemas.UserSchema import user_schema, users_schema
from flask_jwt_extended import create_access_token,jwt_required
from flask_login import login_user, current_user, logout_user
from forms import RegistrationForm, LoginForm
from services.auth_service import verify_user
from datetime import timedelta

users = Blueprint("users", __name__, url_prefix="/users")

#TEMPORARY ROUTE LATER MERGE TO USER_REGISTER ROUTE
@users.route("/register", methods=["GET", "POST"])
def user_register():
    #NEED TO REDIRECT TO SHOW PROFILE IF HAVE TIME
    if current_user.is_authenticated:
        return redirect(url_for("profiles.profile_index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user:
            flash("The email address is registered. Please use another email!")
        else:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
            user = User(email=form.email.data, password=hashed_password)
        
            db.session.add(user)
            db.session.commit()
            flash("Your account has been created! You are now able to login", "success")
            return redirect(url_for("users.user_login"))
    return render_template("register.html", form=form)

@users.route("/login", methods=["GET","POST"])                                                            # Login route
def user_login():
    #NEED TO REDIRECT TO SHOW PROFILE IF HAVE TIME
    if current_user.is_authenticated:
        return redirect(url_for("profiles.profile_index"))
    form = LoginForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user and bcrypt.check_password_hash(existing_user.password, form.password.data):
            login_user(existing_user, remember=form.remember.data)
            next_page = request.args.get("next")
            if next_page:
                return redirect(next_page)
            else:
                #NEED TO REDIRECT TO SHOW PROFILE IF HAVE TIME
                return redirect(url_for(f"profiles.profile_index"))
        else:
            flash("Login Unsuccessful. Please check your email and password", "danger")
    return render_template("login.html", form=form)

@users.route("/logout", methods=["GET","POST"])                                                            # Login route
def user_logout():
    logout_user()
    return redirect(url_for(f"users.user_login"))

# @users.route("/register", methods=["GET","POST"])                                                         # Register route
# def user_register():
#     form = RegistrationForm()
#     user_fields = user_schema.load(request.json)                                                    # Getting the fields from the User Schema
#     user = User.query.filter_by(email=user_fields["email"]).first()                                 # Query the user table with the email and return the first user
    
#     if user:                                                                                        # If a user is returned 
#         return abort(401, description="Email already in use")                                       # Return the error "Email already in use"

#     user = User()                                                                                   # Re-init user as a new instance of the User model

#     user.email = user_fields["email"]                                                               # Add email to the user
#     user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")          # Hash the password and add it to the user

#     db.session.add(user)                                                                            # Add the user to the db session
#     db.session.commit()                                                                             # Commit the session

#     return jsonify(user_schema.dump(user))                                                          # Return the user that was just created

# @users.route("/login", methods=["GET","POST"])                                                            # Login route
# def user_login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == "admin@blog.com" and form.password.data == "password":
#             flash("You have been logged in!", "success")
#             return redirect(url_for("users.users_index"))
#         else:
#             flash("Login Unsuccessful. Please check username and password", "danger")
#     return render_template("login.html", form=form)
    # user_fields = user_schema.load(request.json)                                                    # Getting the fields from the User Schema
    # user = User.query.filter_by(email=user_fields["email"]).first()                                 # Query the user table with the email and return the first user

    # if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):          # If there is no user or the password is wrong
    #     return abort(401, description="Incorrect username or password")                             # Return the error "Incorrect username or password"

    # expiry = timedelta(days=1)                                                                      # Time for the token to expire
    # access_token = create_access_token(identity=str(user.id), expires_delta=expiry)                 # The access token, with the user id and the expiration date

    # return jsonify({ "token": access_token })                                                       # Return the token
    

@users.route("dump/all/<int:id>", methods=["GET"])
@jwt_required
@verify_user
def dump_data(user, id):
    #Check if the user is an admin
    admin = db.session.query(User).filter(User.is_admin == True)

    if not admin:
        return abort(400, "Unauthorised for this feature")
    
    # Get databse table
    tables = User.get_table()
    tables_in_list = tables.fetchall()

    for table in tables_in_list:
        print(table)
    
    # Get the schema list
    #Dump the data

#     query = db.session.query(Profile)
#     query = query.filter(Profile.admin == True).filter_by(profileid = id, user_id=user.id).first()
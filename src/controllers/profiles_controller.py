import os
import json
from models.Profile import Profile                                     # Importing the Profile Model
from models.User import User, load_user                                           # Importing the User Model
from schemas.ProfileSchema import profile_schema, profiles_schema      # Importing the Profile Schema
from main import db                                                    # This is the db instance created by SQLAlchemy
from main import bcrypt                                                # Import the hasing package from main
from services.auth_service import verify_user 
from sqlalchemy.orm import joinedload                                  # 
from flask_jwt_extended import jwt_required, get_jwt_identity          # Packages for authorization via JWTs
from flask import Blueprint, request, jsonify, abort, render_template, redirect, url_for                   # Import flask and various sub packages
from flask_login import login_required, current_user

from schemas.UserSchema import users_schema
from schemas.ProfileSchema import profiles_schema
from schemas.TrackSchema import tracks_schema
from schemas.PlaylistSchema import playlists_schema
from schemas.CollectionSchema import collections_schema
from schemas.ArtistSchema import artists_schema
from schemas.AlbumSchema import albums_schema
from schemas.AlbumTypeSchema import album_type_schema

profiles = Blueprint("profiles", __name__, url_prefix="/profile")      # Creating the profile blueprint 

tables = ["users", "profiles", "tracks", "playlists", "collections", "artists", "albums", "album_types"]
schemas = [users_schema, profiles_schema, tracks_schema, playlists_schema, collections_schema, artists_schema, albums_schema, album_type_schema ]

@profiles.route("/", methods=["GET"])                                  # Route for the profile index
def profile_index():                                                   # This function will run when the route is matched
    profiles = Profile.query.options(joinedload("user")).all()         # Retrieving all profiles from the db
    return jsonify(profiles_schema.dump(profiles))                     # Returning all the profiles in json

@profiles.route("/", methods=["POST"])                                 # Route for the profile create
@jwt_required                                                          # JWT token is required for this route
@verify_user                                                           # Auth service to make sure the correct user owns this profile
def profile_create(user):                                              # This function will run when the route is matched

    if user.profile != []:                                             # If the user already has a profile
        return abort(400, description="User already has profile")      # Return the error "Email already in use"

    profile_fields = profile_schema.load(request.json)                 # Retrieving the fields from the request
    profile = Profile.query.filter_by(username=profile_fields["username"]).first() # Query the user table with the email and return the first user

    if profile:                                                        # If a user is returned 
        return abort(400, description="username already in use")       # Return the error "Email already in use"

    new_profile = Profile()                                            # Create a new profile object from the Profile model 
    new_profile.username = profile_fields["username"]                  # Add username to the new_profile 
    new_profile.firstname = profile_fields["firstname"]                # Add username to the new_profile 
    new_profile.lastname = profile_fields["lastname"]                  # Add username to the new_profile 
    new_profile.user_id = user.id                                      # Add username to the new_profile 
    
    user.profile.append(new_profile)                                   # Add profile to the user
    db.session.commit()                                                # Commit the DB session
      
    return jsonify(profile_schema.dump(new_profile))                   # Return the newly created profile

@profiles.route("/<int:id>", methods=["GET"])                          # Route for the profile create
def profile_show(id):                                                  # Auth service to make sure the correct user owns this profile
    profile = Profile.query.get(id)                                    # Query the user table with the id then return that user
    return jsonify(profile_schema.dump(profile))                       # Returb the profile in JSON

@profiles.route("/web/", methods=["GET"])                          
def display_profile():                                                  
    user = load_user(current_user.get_id())
    profile = Profile.query.filter_by(
        user_id=user.id).order_by(Profile.id)

    return render_template("profiles.html", profile=profile)
    

@profiles.route("/<int:id>", methods=["PUT", "PATCH"])                 # Route for the profile create
@jwt_required                                                          # JWT token is required for this route
@verify_user                                                           # Auth service to make sure the correct user owns this profile
def profile_update(user, id):                             
    
    profile_fields = profile_schema.load(request.json)                 # Retrieving the fields from the request
    profile = Profile.query.filter_by(id=id, user_id=user.id)          # Query the user table with the id and the user id then return the first user
    if not profile:                                                    # If there is no profile found
        return abort(401, description="Unauthorized to update this profile")  # Return this error

    print(profile.__dict__)
    profile.update(profile_fields)                                     # Update the fields with the data from the request
    db.session.commit()                                                # Commit the session to the db
    return jsonify(profile_schema.dump(profile[0]))                    # Return the recently committed profile


@profiles.route("/<int:id>", methods=["DELETE"])                       # Route for the profile create
@jwt_required        
@verify_user                                                           # Auth service to make sure the correct user owns this profile
def profile_delete(user, id):
    profile = Profile.query.filter_by(id=id, user_id=user.id).first()  # Query the user table with the id and the user id then return the first user
    # print(profile[0].__dict__)
    # return("bills")
    if not profile:                                                    # If there is any number other than 1
        return abort(400, description="Unauthorized to update this profile") # Return this error
    
    db.session.delete(profile)
    db.session.commit()                                                # Commit the session to the db
    return jsonify(profile_schema.dump(profile))                       # Return the deleted profile


@profiles.route("dump/all/<int:id>", methods=["GET"])
@jwt_required
@verify_user
def profile_dump(user, id):
    profile = db.session.query(Profile).filter(Profile.user.is_admin == True).filter_by(id=id, user_id=user.id).first()
  
    if not profile:
        return abort(400, description="Unauthorised to complete this action")
    i=0
    try:
        os.remove("backup/backup.json")
        print("file successfully deleted")
    except:
        print("file does not exist")
    for table in tables:        
        query = db.engine.execute(f'SELECT * FROM {table}')
        data = ((schemas[i]).dump(query))

        print(data)

        data = json.dumps(data)
        i+=1
    
        file = open("backup/backup.json", "a")
        file.write(data)
        file.close()
    return "Data backed up"
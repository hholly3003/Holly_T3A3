from main import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted")

@db_commands.cli.command("seed")                                # this fronction will run when "flask db-custom seed" is run"
def seed_db():
    from models.User import User                                # Importing the User model
    from models.Profile import Profile                          # Importing the Profile model
    from models.Playlist import Playlist
    from models.Track import Track
    from models.Album import Album
    from models.Artist import Artist
    from main import bcrypt                                     # Hashing module for the passwords
    from faker import Faker                                     # Importing the faker module for fake data
    import random                                               # Importing random from the python standard library

    faker = Faker()
    users = []
    albums = []

    for i in range(5):                                                           # Do this 5 times
        user = User()                                                           # Create an user object from the User model
        user.email = f"test{i+1}@test.com"                                      # Assign an email to the user object
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8") # Assign ta hashed password to the user object
        db.session.add(user)                                                    # Add the user to the db session
        users.append(user)                                                      # Append the user to the users list

    db.session.commit()                                                         # Commit the seeion to the db 

    for i in range(5):
        profile = Profile()                                                     # Create a profile object from the Profile model                 

        profile.username = faker.first_name()                                   # Add a username to the profile object
        profile.firstname = faker.first_name()                                  # Add a firstname to the profile object
        profile.lastname = faker.last_name()                                    # Add a lastname to the profile object
        profile.user_id = users[i].id                                           # Add a user_id to the profile object. This comes from real ids from the users list

        db.session.add(profile)                                                 # Add the profile to the session
    db.session.commit()                                                        # Commit the session to the database

    for i in range(10):
        album = Album()
        album.name = faker.catch_phrase()
        album.album_type = "SINGLE"
        db.session.add(album)
        albums.append(album)
    db.session.commit()

    for i in range(20):
        playlist = Playlist()                                                   # Create a playlist object from Playlist model
        playlist.name = faker.catch_phrase()
        playlist.owner_id = random.choice(users).id
        playlist.collaborative = False
        playlist.public = True

        track = Track()
        track.name = faker.file_name()
        track.track_num = random.choice(range(20))
        track.album_id = random.choice(albums).album_id
        track.disc_num = 1
        track.duration_ms = 2500
        track.explicit = True

        db.session.add(playlist)
        db.session.add(track)
    db.session.commit()

    for i in range(5):
        artist = Artist()
        artist.name = faker.name_nonbinary()

        db.session.add(artist)
    db.session.commit()  
    
    print("Tables seeded")                                                      # Print a message to let the user know they 

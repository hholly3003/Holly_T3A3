from main import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.Playlist import Playlist
    from faker import Faker
    faker = Faker()

    for i in range(10):
        playlist = Playlist()
        playlist.title = faker.catch_phrase()
        db.session.add(playlist)
        print(f"{i+1} playlist record(s) created")
    db.session.commit()
    print("Tables Seeded!")

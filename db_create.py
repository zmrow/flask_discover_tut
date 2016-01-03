from app import db
from models import BlogPost

# create the db and db tables
db.create_all()

# Insert
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))

# Commit the changes
db.session.commit()

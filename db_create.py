from project import db
from project.models import BlogPost

# create the db and db tables
db.create_all()

# Insert
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("postgress", "setup local postgressss"))

# Commit the changes
db.session.commit()

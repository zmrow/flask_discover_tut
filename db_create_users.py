from project import db
from project.models import User

# insert data
db.session.add(User("zac", "zac@example.com", "nonottelling"))
db.session.add(User("admin", "ad@min.com", "admin"))

# commit the changes
db.session.commit()

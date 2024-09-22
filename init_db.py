from app import db
from app.models import Medication

# Create the database and tables
db.create_all()

print("Database initialized!")

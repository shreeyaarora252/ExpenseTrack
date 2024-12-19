from app import create_app, db
from app.models.user import User
from app.models.sms_mod import SMS

# Create the app
app = create_app()

# Create database tables
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")

if __name__ == '__main__':
    app.run(debug=True)

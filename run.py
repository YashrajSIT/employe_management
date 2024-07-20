from app.app import create_app ## Import create_app from app .app
from app.db_instance import db #importing db

app=create_app()  # Create the Flask application using the create_app function
# Checking if the script is being run directly or not
if __name__=='__main__':
        with app.app_context():
            db.create_all()
            # Run the Flask application in debug mode if true
        app.run(debug=True)
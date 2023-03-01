from auth_app import run
from auth_app import db
from auth_app.user.models import User
from auth_app import app
if __name__ == "__main__":
    db.create_all()
    run()
    app.run(debug=True)
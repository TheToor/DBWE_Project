from app.db.db import db
from app.models.User import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class AuthenticationController:    
    def try_create_user(self, email, name, password):
        user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none()
        if user is not None:
            return False
        
        new_user = User(email=email, name=name, password=bcrypt.generate_password_hash(password).decode('utf-8'))

        db.session.add(new_user)
        db.session.commit()

        return True
    
    def login(self, email, password):
        user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none()
        if user is None:
            return None
        
        if bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None

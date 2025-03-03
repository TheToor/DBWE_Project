from app.db.db import db
from app.models.User import User

class IndexController:
    def index(self):
        id = 1
        return db.get_or_404(User, id)

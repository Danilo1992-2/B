from datetime import datetime
from sqlalchemy.orm import sessionmaker
from entidade import User
from config import ENGINE


class NewUser:
    def __init__(self, name: str, document: str,
                 user: str, password: str):
        self.name: str = name
        self.document: str = document
        self.user: str = user
        self.password: str = password

    def create_new_user(self):
        user = User(name=self.name,
                    document=self.document,
                    user=self.user,
                    create_at=datetime.now,
                    password=self.password)
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        session.add(user)
        session.commit()


var = NewUser("danilo", "1331633323", "dtes", "1231312")
var.create_new_user()

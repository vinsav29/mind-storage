from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy.orm import sessionmaker, relationship

engine = sqlalchemy.create_engine("sqlite:///:memory:")
base = declarative_base()
session = sessionmaker(bind=engine)()


# a User has a single Car, so a Car can belong to many Users
class Config(base):
    __tablename__ = "configs"
    cid = Column(Integer, primary_key=True)
    model = Column(String)

    def __repr__(self):
        return "Car:" + self.model


Config.__table__.create(engine)


class Instance(base):
    __tablename__ = "airflow_instances"
    uid = Column(Integer, primary_key=True)
    username = Column(String)

    def __repr__(self):
        return "User:" + self.username

    instance_config_id = Column(Integer, ForeignKey("configs.cid"))
    instance_config = relationship("Config")


Instance.__table__.create(engine)

user_a = Instance(username="Andrew")
car_a = Config(model="Accord", cid=1)
user_a.instance_config_id = car_a.cid

user_b = Instance(username="Barbara")
# user_b.instance_config = car_a

print("Andrew's " + str(user_a.car))

print("Barbara's " + str(user_b.car))
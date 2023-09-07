from datetime import timedelta


class Config:
    DEBUG = True
    SECRET_KEY = 'kleo4309cSDDfdkei439dki489ejk3kj439iedoS$D$lsSS'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bektemir:bektemir2001@localhost:3306/face_rec_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

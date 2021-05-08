import os

class Config:
    pass

class DevelopmentConfig(Config):
    
    DEBUG = True
    file_path = os.path.abspath(os.getcwd())+"\Articles.db"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ file_path
    
config = {
    'development': DevelopmentConfig,
}
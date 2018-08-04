from app import create_app
from models import db
from config import DevelopConfig
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = create_app(DevelopConfig)
manger = Manager(app)
Migrate(app, db)
manger.add_command('db', MigrateCommand)


if __name__ == '__main__':
    # manger.run()
    app.run()




import unittest
from app import create_app,db
from  flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server

app = create_app('default')

manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('server', Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db)


if __name__ == '__main__':
    manager.run()


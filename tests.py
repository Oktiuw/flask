import os

os.environ['DATABASE_URL'] = 'sqlite://'
from datetime import datetime, timedelta
import unittest
from app import  db, Config, create_app
from app.models import User, Post


class TestConfig(Config):
    def __init__(self):
        self.TESTING = True


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self: object):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self: object):
        u = User(username='suzan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_abonnement(self: object):
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='suzan', email='suzan@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.abonnement.all(), [])
        self.assertEqual(u1.abonnes.all(), [])
        u1.abonner(u2)
        db.session.commit()
        self.assertTrue(u1.is_abonne(u2))
        self.assertEqual(u1.abonnement.count(), 1)
        self.assertEqual(u1.abonnement.first().username, 'suzan')
        self.assertEqual(u2.abonnes.count(), 1)
        self.assertEqual(u2.abonnes.first().username, 'john')
        u1.desabonner(u2)
        db.session.commit()
        self.assertFalse(u1.is_abonne(u2))
        self.assertEqual(u1.abonnement.count(), 0)
        self.assertEqual(u2.abonnes.count(), 0)

    def test_messages_abonnement(self: object):
        # Créer 4 utilisateurs
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='suzan', email='suzan@example.com')
        u3 = User(username='mary', email='mary@example.com')
        u4 = User(username='david', email='david@example.com')
        db.session.add_all([u1, u2, u3, u4])
        # Créer 4 messages
        now = datetime.utcnow()
        p1 = Post(body="post from john", timestamp=now + timedelta(seconds=1),
                  author=u1)
        p2 = Post(body="post from suzan", timestamp=now + timedelta(seconds=4),
                  author=u2)
        p3 = Post(body="post from mary", timestamp=now + timedelta(seconds=3),
                  author=u3)
        p4 = Post(body="post from david", timestamp=now + timedelta(seconds=2),
                  author=u4)
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()
        # fixer les abonnements
        u1.abonner(u2)  # john s'abonne à suzan
        u1.abonner(u4)  # john s'abonne à david
        u2.abonner(u3)  # suzan s'abonne à mary
        u3.abonner(u4)  # mary s'abonne à david
        db.session.commit()
        # Vérifier les messages de chacun
        f1 = u1.posts_abonnes().all()
        f2 = u2.posts_abonnes().all()
        f3 = u3.posts_abonnes().all()
        f4 = u4.posts_abonnes().all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])


if __name__ == '__main__':
    unittest.main(verbosity=2)

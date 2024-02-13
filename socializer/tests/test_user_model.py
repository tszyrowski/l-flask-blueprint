from application.users import models


def test_create_user_instance(session):
    """Create and save a user instance"""

    email = 'test@example.com'
    username = 'test_user'
    password = 'foobarbaz'

    user = models.User(email=email, username=username, password=password)
    session.add(user)
    session.commit()

    # Clear out the database after every run of hte test suite
    # but not depend on magic numbers
    assert user.id is not None

    assert user.followed.count() == 0
    assert user.newsfeed().count() == 0
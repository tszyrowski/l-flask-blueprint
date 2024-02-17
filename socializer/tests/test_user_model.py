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


def test_follow_user(session):
    """Create and save a user instance"""

    email = 'test_1@email.com'
    username = 'test_1'
    password = 'foobarbaz'

    user_1 = models.User(email=email, username=username, password=password)
    session.add(user_1)
    session.commit()

    email = 'test_2@email.com'
    username = 'test_2'
    password = 'foobarbaz'

    user_2 = models.User(email=email, username=username, password=password)
    session.add(user_2)
    session.commit()

    user_1.follow(user_2)
    session.commit()

    assert user_1.is_following(user_2)
    assert user_1.followed.count() == 1
    assert user_1.followed.first().id == user_2.id
    assert user_2.followers.count() == 1
    assert user_2.followers.first().id == user_1.id

    user_1.unfollow(user_2)
    session.commit()

    assert not user_1.is_following(user_2)
    assert user_1.followed.count() == 0
    assert user_2.followers.count() == 0
    
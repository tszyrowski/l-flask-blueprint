from bs4 import BeautifulSoup
from flask import get_flashed_messages, session as flask_session
import pytest
import sqlalchemy.orm.exc
from application.users.models import User
from application import flask_bcrypt_instance


def test_get_user_signup_page(client):
    response = client.get('/users/signup')
    assert response.status_code == 200
    assert b'Sign Up' in response.data

def test_signup_new_user(client, session):
    """Successfully signup a new user"""

    # Get the CSRF token
    get_response = client.get('/users/signup')
    html = get_response.data.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

    data = {
        'username': 'test-1',
        'email': 'test-1@example.com',
        'password': 'my_password',
        'csrf_token': csrf_token,
    }
    # response = client.post('/users/signup', data=data, follow_redirects=True)
    response = client.post('/users/signup', data=data, content_type='application/x-www-form-urlencoded', follow_redirects=True)

    # TODO: Check for the redirect
    # TODO: Check session for user_id

    # Redirect on successful login
    assert response.status_code == 200
    # assert b'<div><input type="submit" value="Sign Up"></div>' in response.data
    assert b'Socialiser' in response.data
    # print(response.headers['Location'])
    # assert response.headers['Location']

    # checks session created due to successful login
    # assert 'user_id' in flask_session

    # TODO: Check for messages
    # Ensure no flash messages indicating an error
    # assert 'User successfully created' in get_flashed_messages()

    # TODO: Check for user in database
    # user = User.query.filter_by(username=data['username']).one()

    # assert user.username == data['username']
    # assert user.email == data['email']
    # assert flask_bcrypt_instance.check_password_hash(
    #     user.password, data['password']
    # )

def test_signup_invalid_user(client):
    """Try to sign up with invalid data."""

    data = {'username': 'x', 'email': 'short@example.com',
            'password': 'a'}

    response = client.post('/users/signup', data=data)

    # With a form error, we still return a 200 to the client since
    # browsers are not always the best at handling proper 4xx response codes.
    assert response.status_code == 200

    # TODO: Work out correct 
    # assert b'must be between 3 and 40 characters long.' in response.data

def test_signup_invalid_user_missing_fields(client):
    """Try to sign up with missing email."""

    data = {'username': 'no_email', 'password': 'a great password'}
    response = client.post('/users/signup', data=data)

    assert response.status_code == 200
    assert b'This field is required' in response.data

    with pytest.raises(sqlalchemy.orm.exc.NoResultFound):
        User.query.filter_by(username=data['username']).one()

    data = {'username': 'no_password', 'email': 'test@example.com'}
    response = client.post('/users/signup', data=data)

    assert response.status_code == 200
    assert b'This field is required' in response.data

    with pytest.raises(sqlalchemy.orm.exc.NoResultFound):
        User.query.filter_by(username=data['username']).one()
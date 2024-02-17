import flask

def test_app(app):
    """This test gets app from contest.py"""
    assert isinstance(app, flask.Flask)
__all__ = ["user_followed_email"]

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def user_followed_email(user, **kwargs):
    logger.info(
        "User %s followed, ... signal emited", user.username
    )

from application import user_followed

def connect_handlers():
    user_followed.connect(user_followed_email)
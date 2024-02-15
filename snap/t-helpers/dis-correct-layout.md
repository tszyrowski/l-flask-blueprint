I have this directroy structure:
```
╰─➤  tree -I "*.pyc|__pycache__" .
.
├── application
│   ├── __init__.py
│   ├── snaps
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── snaps
│   │   │       ├── add.html
│   │   │       └── index.html
│   │   └── views.py
│   ├── templates
│   │   └── layout.html
│   └── users
│       ├── __init__.py
│       ├── models.py
│       ├── templates
│       │   └── users
│       │       ├── index.html
│       │       └── login.html
│       ├── views
│       └── views.py
├── create_db.py
├── instance
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── 0bc70664b911_added_password_field_to_user_model.py
├── populate_db.py
├── run.py
├── site.db
└── t-helpers
    └── dis-correct-layout.md

13 directories, 21 files
```
in my application/templates/layout.html:
```
<!DOCTYPE html>
<html>
  <head>
    <title>Snaps</title>
  </head>
    <body>
        <h1>Snaps</h1>
        {% for message in get_flashed_messages() %}
            <div class="flash">{{ message }}</div>
        {% endfor %}

        {% if not current_user.is_authenticated() %}
            <a href="{{ url_for('users.login') }}">Log in</a>
        {% else %}
            <a href="{{ url_for('users.logout') }}">Log out</a>
        {% endif %}
        <div class="content">

        {% block content %}{% endblock %}
        </div>
    </body>
</html>
```

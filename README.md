# Flask with Blueprints

[Based on Oreilly](https://learning.oreilly.com/library/view/flask-blueprints/9781784394783)

## Updating DB:

```
(vFlask.3.11) ╭─t@NumericalCatalyst ~/workspace_training/l-flask/l-flask-blueprint/snap  ‹main*› 
╰─➤  export FLASK_APP=run.py                                                                                                                                                                                                                              2 ↵
(vFlask.3.11) ╭─t@NumericalCatalyst ~/workspace_training/l-flask/l-flask-blueprint/snap  ‹main*› 
╰─➤  flask db migrate -m "Added password field to user model"
 * Ignoring a call to 'app.run()' that would block the current 'flask' CLI command.
   Only call 'app.run()' in an 'if __name__ == "__main__"' guard.
Error: Path doesn't exist: '/home/t/workspace_training/l-flask/l-flask-blueprint/snap/migrations'.  Please use the 'init' command to create a new scripts folder.
(vFlask.3.11) ╭─t@NumericalCatalyst ~/workspace_training/l-flask/l-flask-blueprint/snap  ‹main*› 
╰─➤  flask db init                                                                                                                                                                                                                                        1 ↵
 * Ignoring a call to 'app.run()' that would block the current 'flask' CLI command.
   Only call 'app.run()' in an 'if __name__ == "__main__"' guard.
  Creating directory '/home/t/workspace_training/l-flask/l-flask-blueprint/snap/migrations' ...  done
  Creating directory '/home/t/workspace_training/l-flask/l-flask-blueprint/snap/migrations/versions' ...  done
  Generating /home/t/workspace_training/l-flask/l-flask-blueprint/snap/migrations/env.py ...  done
  Generating /home/t/workspace_training/l-flask/l-flask-blueprint/snap/migrations/script.py.mako ...  done
  Generating /home/t/workspace_training/l-flask/l-flask-blueprint/snap/migrations/alembic.ini ...  done
  Generating /home/t/workspace_training/l-flask/l-flask-blueprint/snap/migrations/README ...  done
  Please edit configuration/connection/logging settings in '/home/t/workspace_training/l-flask/l-flask-blueprint/snap/migrations/alembic.ini' before proceeding.
(vFlask.3.11) ╭─t@NumericalCatalyst ~/workspace_training/l-flask/l-flask-blueprint/snap  ‹main*› 
╰─➤  flask db migrate -m "Added password field to user model"

 * Ignoring a call to 'app.run()' that would block the current 'flask' CLI command.
   Only call 'app.run()' in an 'if __name__ == "__main__"' guard.
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added column 'user.password'
INFO  [alembic.autogenerate.compare] Detected added column 'user.created_on'
  Generating /home/t/workspace_training/l-flask/l-flask-blueprint/snap/migrations/versions/0bc70664b911_added_password_field_to_user_model.py ...  done
(vFlask.3.11) ╭─t@NumericalCatalyst ~/workspace_training/l-flask/l-flask-blueprint/snap  ‹main*› 
╰─➤  
(vFlask.3.11) ╭─t@NumericalCatalyst ~/workspace_training/l-flask/l-flask-blueprint/snap  ‹main*› 
╰─➤  flask db upgrade

 * Ignoring a call to 'app.run()' that would block the current 'flask' CLI command.
   Only call 'app.run()' in an 'if __name__ == "__main__"' guard.
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 0bc70664b911, Added password field to user model

```
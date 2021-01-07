# 
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
pip install flask
python -c "import flask; print(flask.__version__)"

create hello.py
export FLASK_APP=hello
export FLASK_ENV=development
flask run

create app.py
export FLASK_APP=app
flask run


create template/index.html
create template/base.html
create static/css/style.css
create schema.sql
create init_db.py

python init_db.py



import sqlite3
from flask import Flask, render_template

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/lyrics', methods = ['POST', 'GET'])
def lyrics():
   gsd = "GSD DATA"
   render_template('lyrics.html')
   if request.method == 'POST':
      webscraping_url = request.form['search_url']
      return redirect(url_for('success', the_url = webscraping_url))
   else:
      webscraping_url = request.args.get('search_url')
      return redirect(url_for('success', the_url = webscraping_url))
    
@app.route('/success/<the_url>')
def success(the_url):
   return 'Search URL :  %s' % the_url

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

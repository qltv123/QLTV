from flask import Flask, render_template,request,redirect,url_for,session
from app2 import get_all, insert_data_book
from app3 import get_all2,insert_data_user
app = Flask(__name__)
app.secret_key = 'jjsdkfjkjdkfj515'


@app.route('/', methods = ['POST'])
def post_login():
    tk = request.form.get('namedn')
    mk = request.form.get('mkdn')
    if tk == "admin" and mk == "admin":
      session['namedn'] = request.form.get('namedn')
      return redirect(url_for("indexTC"))
    else:
      return "Login false"

@app.route('/AddDataBook', methods = ['POST'])
def post():
    book_mas = request.form.get('mas')
    book_name = request.form.get('name')
    book_price = int(request.form.get('price'))
    book_nxb = request.form.get('nxb')
    insert_data_book(book_mas,book_name,book_price,book_nxb)
    return redirect(url_for("indexS"))
  
@app.route('/AddCardUser', methods = ['POST'])
def posrUser():
   user_ma = request.form.get('ma')
   user_name = request.form.get('name')
   user_phone = request.form.get('phone')
   user_sex = request.form.get('sex')
   user_add = request.form.get('add')
   insert_data_user(user_ma,user_name,user_phone,user_sex,user_add)
   return redirect(url_for('indexKH'))

@app.route('/AddCardUser')
def indexKH():
  if 'namedn' in session:
        return render_template("indexKH.html", dulieu = get_all2())
  else:
        return redirect(url_for("index"))

@app.route('/AddDataBook')
def indexS():
    if 'namedn' in session:
        return render_template("indexS.html", dulieu = get_all())
    else:
        return redirect(url_for("index"))

@app.route('/TrangChu')
def indexTC():
  if 'namedn' in session:
      return render_template("indexTC.html", dulieu = get_all())
  else:
      return redirect(url_for("index"))

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
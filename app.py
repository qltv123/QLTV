from flask import Flask, render_template,request,redirect,url_for,session
from app2 import get_all, insert_data_book,delete_data_book,update_book_by_id,get_book_by_id
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

@app.route('/TrangChu', methods = ['POST'])
def post():
    book_name = request.form.get('name')
    book_nxb = request.form.get('nxb')
    book_sl = int(request.form.get('sl'))
    book_price = int(request.form.get('price'))
    insert_data_book(book_name,book_nxb,book_sl,book_price)
    return redirect(url_for("indexTC"))
  
# @app.route('/AddCardUser', methods = ['POST'])
# def posrUser():
#    user_ma = request.form.get('ma')
#    user_name = request.form.get('name')
#    user_phone = request.form.get('phone')
#    user_sex = request.form.get('sex')
#    user_add = request.form.get('add')
#    insert_data_user(user_ma,user_name,user_phone,user_sex,user_add)
#    return redirect(url_for('indexKH'))

@app.route('/edit_book/<book_id>',methods = ['POST'])
def put_book(book_id):
    bo_names = request.form.get('names')
    bo_nxb = request.form.get('nxb')
    bo_sl = int(request.form.get('sl'))
    bo_price = int(request.form.get('price'))
    update_book_by_id(book_id, bo_names, bo_nxb, bo_sl, bo_price)
    return redirect(url_for('indexTC'))
 
@app.route('/edit_book/<book_id>')
def func_name(book_id):
    bo = get_book_by_id(book_id) 
    return render_template('edit_book.html',book = bo)

@app.route('/AddCardUser')
def indexKH():
  if 'namedn' in session:
        return render_template("indexKH.html", dulieu = get_all2())
  else:
        return redirect(url_for("index"))

@app.route('/TrangChu')
def indexTC():
  if 'namedn' in session:
      return render_template("cate_list.html", dulieu = get_all())
  else:
      return redirect(url_for("index"))

@app.route('/delete_book/<book_id>')
def delete(book_id):
   delete_data_book(book_id)
   return redirect(url_for("indexTC"))

@app.route('/PFMC')
def index2():
   return render_template("index2.html")

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
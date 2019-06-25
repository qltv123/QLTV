from flask import Flask, render_template,request,redirect,url_for,session
from app2 import get_all, insert_data_book,delete_data_book,update_book_by_id,get_book_by_id,search_book
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

@app.route('/AddBook', methods = ['POST'])
def post():
    book_name = request.form.get('names')
    book_link = request.form.get('link')
    book_sl = request.form.get('sl')
    book_nxb = request.form.get('nxb')
    book_price = int(request.form.get('price'))
    insert_data_book(book_name,book_link,book_sl,book_nxb,book_price)
    return redirect(url_for("indexAB"))
  
@app.route('/AddCardUser', methods = ['POST'])
def posrUser():
   user_name = request.form.get('namek')
   user_sex = request.form.get('sex')
   user_bi = request.form.get('birth')
   user_cmt = request.form.get('cmt')
   user_job = request.form.get('job')
   user_le = request.form.get('level')
   user_wp = request.form.get('wp')
   user_phone = request.form.get('phone')
   user_ct = request.form.get('ct')
   user_ci = request.form.get('city')
   user_add = request.form.get('add')
   user_ti = request.form.get('time')
   insert_data_user(user_name,user_sex,user_bi,user_cmt,user_job,user_le,user_wp,user_phone,user_ct,user_ci,user_add,user_ti)
   return redirect(url_for('indexKH'))

@app.route('/edit_book/<book_id>',methods = ['POST'])
def put_book(book_id):
    bo_names = request.form.get('names')
    bo_nxb = request.form.get('nxb')
    bo_sl = int(request.form.get('sl'))
    bo_price = int(request.form.get('price'))
    update_book_by_id(book_id, bo_names, bo_nxb, bo_sl, bo_price)
    return redirect(url_for('indexAB'))
 
@app.route('/edit_book/<book_id>')
def func_name(book_id):
    bo = get_book_by_id(book_id) 
    return render_template('edit_book.html',book = bo)

@app.route('/AddCardUser')
def indexKH():
  if 'namedn' in session:
        return render_template("cate_list2.html", dulieu = get_all2())
  else:
        return redirect(url_for("index"))

@app.route('/TrangChu')
def indexTC():
  if 'namedn' in session:
      return render_template("cate_list3.html", dulieu = get_all())
  else:
      return redirect(url_for("index"))

@app.route('/AddBook')
def indexAB():
  if 'namedn' in session:
      return render_template("cate_list.html",dulieu = get_all())
  else:
      return redirect(url_for("index"))

@app.route('/delete_book/<book_id>')
def delete(book_id):
   delete_data_book(book_id)
   return redirect(url_for("indexAB"))

@app.route('/NQ')
def indexNQ():
      if 'namedn' in session:
            return render_template("cate_list4.html")
      else:
            return redirect(url_for("index"))

@app.route('/QD')
def indexQD():
      if 'namedn' in session:
            return render_template("cate_list5.html")
      else:
            return redirect(url_for("index"))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/out')
def method_name():
   del session["namedn"]
   return redirect(url_for("index"))

@app.route('/search',method=['post'])
def indexS(names):
      bo_names = request.form.get('names')
      search_book(bo_names)
      return redirect(url_for('indexAB'))

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
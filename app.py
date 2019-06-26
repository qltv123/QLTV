from flask import Flask, render_template,request,redirect,url_for,session
from app2 import get_all, insert_data_book,delete_data_book,update_book_by_id,get_book_by_id
from app3 import get_all2,insert_data_user
app = Flask(__name__)
app.secret_key = 'jjsdkfjkjdkfj515'


@app.route('/DN', methods = ['POST'])
def post_login():
    tk = request.form.get('namedn')
    mk = request.form.get('mkdn')
    if tk == "admin" or "ntduc" and mk == "admin" or "12051998":
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
      if 'namedn' in session:
            insert_data_book(book_name,book_link,book_sl,book_nxb,book_price)
            return redirect(url_for("indexAB"))
      else:
            return "Yêu cầu đăng nhập để thực hiện chức năng này"

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
      if 'namedn' in session:
            insert_data_user(user_name,user_sex,user_bi,user_cmt,user_job,user_le,user_wp,user_phone,user_ct,user_ci,user_add,user_ti)
            return redirect(url_for('indexKH'))
      else:
            return "Yêu cầu đăng nhập để thực hiện chức năng này"

@app.route('/edit_book/<book_id>',methods = ['POST'])
def put_book(book_id):
    bo_names = request.form.get('names')
    bo_li = request.form.get('link')
    bo_nxb = request.form.get('nxb')
    bo_sl = int(request.form.get('sl'))
    bo_price = int(request.form.get('price'))
    update_book_by_id(book_id,bo_names, bo_li, bo_nxb, bo_sl, bo_price)
    return redirect(url_for('indexAB'))
 
@app.route('/edit_book/<book_id>')
def func_name(book_id):
      if 'namedn' in session:
            bo = get_book_by_id(book_id) 
            return render_template('edit_book.html',book = bo)
      else:
            return "Yêu cầu đăng nhập để thực hiện chức năng này"

@app.route('/AddCardUser')
def indexKH():
      return render_template("cate_list2.html")
  

@app.route('/TrangChu')
def indexTC():
      return render_template("cate_list3.html")

@app.route('/AddBook')
def indexAB(): 
      return render_template("cate_list.html",dulieu = get_all())

@app.route('/delete_book/<book_id>')
def delete(book_id):
      if 'namedn' in session:
            delete_data_book(book_id)
            return redirect(url_for("indexAB"))
      else:
            return "Yêu cầu đăng nhập để thực hiện chức năng này"

@app.route('/NQ')
def indexNQ():
      return render_template("cate_list4.html")

@app.route('/QD')
def indexQD():
            return render_template("cate_list5.html")

@app.route('/IFU')
def indexIFU():
   return render_template("cate_list6.html",dulieu2 = get_all2())

@app.route('/DN')
def index():
    return render_template("index.html")

@app.route('/out')
def method_name():
   del session ['namedn']
   return redirect(url_for("indexTC"))




if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
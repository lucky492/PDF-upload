from flask import Flask,render_template,request,session,redirect,send_file
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import json
import os
from werkzeug.utils import secure_filename

web = Flask(__name__)

files = "templates\\config.json"
with open(files,'r') as f:
    param = json.load(f)['parameter']

if param['local_server'] == True :
    web.config['SQLALCHEMY_DATABASE_URI'] = param['local_uri']
else:
        web.config['SQLALCHEMY_DATABASE_URI'] = param['prod_uri']  ###prod means production

#### mysql://username:password@localhost/db_name - if we dont have any username or password in xampp username will be root and no password
web.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(web)
web.secret_key = 'secetkeybro'
web.config['UPLOAD_FOLDER'] = param['upload_location']



class blog(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    subtitle =db.Column(db.Text())
    content = db.Column(db.Text())
    file = db.Column(db.String(),nullable = False)
    date_created = db.Column(db.DateTime , default=datetime.utcnow)

class message(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    message = db.Column(db.Text())
    date_created = db.Column(db.DateTime , default=datetime.utcnow)

class special_books(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    special_books_data = db.Column(db.String())
    special_books_image = db.Column(db.String())
    special_books_name = db.Column(db.Text())
    special_books_content = db.Column(db.Text())
    date_created = db.Column(db.DateTime , default=datetime.utcnow)

class school_books(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    school_books_data = db.Column(db.String())
    school_books_image = db.Column(db.String())
    school_books_name = db.Column(db.Text())
    school_books_content =db.Column(db.String())
    date_created = db.Column(db.DateTime , default=datetime.utcnow)
    
class finance_books(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    finance_books_data = db.Column(db.String())
    finance_books_image = db.Column(db.String())
    finance_books_name =db.Column(db.Text())
    finance_books_content =db.Column(db.String())
    date_created = db.Column(db.DateTime , default=datetime.utcnow)

class uncategorised_books(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    uncategorised_books_data = db.Column(db.String())
    uncategorised_books_image = db.Column(db.String())
    uncategorised_books_name = db.Column(db.Text())
    uncategorised_books_content = db.Column(db.String())
    date_created = db.Column(db.DateTime , default=datetime.utcnow)


####### for paination
@web.route("/<int:page_num>")
def home2(page_num):
    blogs = blog.query.order_by(blog.date_created.desc()).paginate(per_page=param['no_of_blogs'],page=page_num, error_out=True)
    return render_template('index.html', blogs=blogs, param=param)

@web.route("/")
def home():
    blogs = blog.query.order_by(blog.date_created.desc()).paginate(per_page=param['no_of_blogs'], error_out=True)
    return render_template('index.html', blogs=blogs, param=param)


@web.route("/blog/<string:title>")
def blogs(title):
    blogs = blog.query.filter_by(title=title).first()
    return render_template('about.html',blogs=blogs,param=param)

@web.route("/about")
def about():
    return render_template('about.html',param=param)

@web.route("/store")
def store():
    return render_template('store.html')

@web.route("/contact")
def contact():
    return render_template('contact.html')

@web.route("/bookspdf")
def bookspdf():

    special_book = special_books.query.order_by(special_books.date_created.desc()).all()
    school_book = school_books.query.order_by(school_books.date_created.desc()).all()
    finance_book = finance_books.query.order_by(finance_books.date_created.desc()).all()
    uncate = uncategorised_books.query.order_by(uncategorised_books.date_created.desc()).all()

    return render_template('store_dropdown.html',special_book=special_book,school_book=school_book,finance_book=finance_book,uncate=uncate)




# ########display message
# @web.route("/bookspdf/comments" ,methods=['POST','GET'])
# def display_messages():
#     msg = message.query.all()
#     return render_template('message_display.html',msg=msg)


# ######   add comments
# @web.route("/bookspdf/comments" ,methods=['POST','GET'])
# def add_messages():
#     if request.method == 'POST':
#         name = request.files['name']
#         msg = request.form.get('message')

#         msg2 = message(name=name,message=msg)

#         db.session.add(msg2)
#         db.session.commit()
#         return redirect('/bookspdf/comments')






########################## search engine #############################





####search engine for books list
@web.route("/admin/books_list/search" ,methods=['POST','GET'])
def search():
    if request.method == 'POST':

        search = request.form.get('search')
        search2 = "%{}%".format(search)
        school_book = school_books.query.filter(school_books.school_books_name.like(search2)).all()
        special_book = special_books.query.filter(special_books.special_books_name.like(search2)).all()
        finance_book = finance_books.query.filter(finance_books.finance_books_name.like(search2)).all()
        uncate = uncategorised_books.query.filter(uncategorised_books.uncategorised_books_name.like(search2)).all()

        return render_template('admin_temp/school_books_list.html',school_book=school_book,special_book=special_book,finance_book=finance_book,uncate=uncate)


####search engine for school books
@web.route("/bookspdf/schoolbooks/search" ,methods=['POST','GET'])
def schoolbook_search():
    if request.method == 'POST':

        search = request.form.get('search2')
        search2 = "%{}%".format(search)
        school_book = school_books.query.filter(school_books.school_books_name.like(search2)).all()

        return render_template('search_school_books_list.html',school_book=school_book)


####search engine for special books
@web.route("/bookspdf/specialbooks/search" ,methods=['POST','GET'])
def specialbooks_search():
    if request.method == 'POST':

        search = request.form.get('search2')
        search2 = "%{}%".format(search)
        special_book = special_books.query.filter(special_books.special_books_name.like(search2)).all()

        return render_template('search_special_books_list.html',special_book=special_book)


####search engine for finance books
@web.route("/bookspdf/financebooks/search" ,methods=['POST','GET'])
def financebooks_search():
    if request.method == 'POST':

        search = request.form.get('search2')
        search2 = "%{}%".format(search)
        finance_book = finance_books.query.filter(finance_books.finance_books_name.like(search2)).all()

        return render_template('search_finance_books_list.html',finance_book=finance_book)


####search engine for uncategorised books
@web.route("/bookspdf/uncategorisedbooks/search" ,methods=['POST','GET'])
def uncategorisedbooks_search():
    if request.method == 'POST':

        search = request.form.get('search2')
        search2 = "%{}%".format(search)
        uncate = uncategorised_books.query.filter(uncategorised_books.uncategorised_books_name.like(search2)).all()

        return render_template('search_uncategorised_books_list.html',uncate=uncate)
    



#### Admins place ####






###########################   download files  #####################################
@web.route("/download/<string:name>")
def download(name):
    school_book=school_books.query.filter_by(school_books_data=name).first()
    try:
        path = os.path.join(web.config['UPLOAD_FOLDER'] ,school_book.school_books_data )
        print(path)
        return send_file(path, attachment_filename=school_book.school_books_data, as_attachment=True)
    except:
        return "file not exist"

@web.route("/download2/<string:name>")
def download2(name):
    special_book=special_books.query.filter_by(special_books_data=name).first()
    try:
        path = os.path.join(web.config['UPLOAD_FOLDER'] ,special_book.special_books_data )
        print(path)
        return send_file(path, attachment_filename=special_book.special_books_data, as_attachment=True)
    except:
        return "file not exist"

@web.route("/download3/<string:name>")
def download3(name):
    finance_book=finance_books.query.filter_by(finance_books_data=name).first()
    try:
        path = os.path.join(web.config['UPLOAD_FOLDER'] ,finance_book.finance_books_data )
        print(path)
        return send_file(path, attachment_filename=finance_book.finance_books_data, as_attachment=True)
    except:
        return "file not exist"

@web.route("/download4/<string:name>")
def download4(name):
    uncategorised_book=uncategorised_books.query.filter_by(uncategorised_books_data=name).first()
    try:
        path = os.path.join(web.config['UPLOAD_FOLDER'] ,uncategorised_book.uncategorised_books_data )
        print(path)
        return send_file(path, attachment_filename=uncategorised_book.uncategorised_books_data, as_attachment=True)
    except:
        return "file not exist"




##################### delete files from database and path where files are kept

@web.route("/deleteblog/<string:name>")
def delete_blog(name):
    blogs= blog.query.filter_by(title=name).first()

    ##### delete from path or folder
    try:
        path = os.path.join(web.config['UPLOAD_FOLDER'] ,blogs.file)
        os.remove(path)
    except : print("file not present")

    #####delete from database
    db.session.delete(blogs)
    db.session.commit()

    return redirect("/admin")


@web.route("/delete/<string:name>")
def delete1(name):
    special_book=special_books.query.filter_by(special_books_name=name).first()


    ##### delete from path or folder
    path = os.path.join(web.config['UPLOAD_FOLDER'] ,special_book.special_books_data )
    os.remove(path)

    path2 = os.path.join(web.config['UPLOAD_FOLDER'] ,special_book.special_books_image )
    os.remove(path2)


    #####delete from database
    db.session.delete(special_book)
    db.session.commit()

    return redirect("/admin/books_list")


@web.route("/delete2/<string:name>")
def delete2(name):
    school_book=school_books.query.filter_by(school_books_name=name).first()


    ##### delete from path or folder
    path = os.path.join(web.config['UPLOAD_FOLDER'] ,school_book.school_books_data )
    os.remove(path)

    path2 = os.path.join(web.config['UPLOAD_FOLDER'] ,school_book.school_books_image )
    os.remove(path2)


    #####delete from database
    db.session.delete(school_book)
    db.session.commit()

    return redirect("/admin/books_list")

@web.route("/delete3/<string:name>")
def delete3(name):
    finance_book=finance_books.query.filter_by(finance_books_name=name).first()


    ##### delete from path or folder
    path = os.path.join(web.config['UPLOAD_FOLDER'] ,finance_book.finance_books_data )
    os.remove(path)

    path2 = os.path.join(web.config['UPLOAD_FOLDER'] ,finance_book.finance_books_image )
    os.remove(path2)


    #####delete from database
    db.session.delete(finance_book)
    db.session.commit()

    return redirect("/admin/books_list")

@web.route("/delete4/<string:name>")
def delete4(name):
    uncategorised_book=uncategorised_books.query.filter_by(uncategorised_books_name=name).first()


    ##### delete from path or folder
    path = os.path.join(web.config['UPLOAD_FOLDER'] ,uncategorised_book.uncategorised_books_data )
    os.remove(path)
        
    path2 = os.path.join(web.config['UPLOAD_FOLDER'] ,uncategorised_book.uncategorised_books_image )
    os.remove(path2)


    #####delete from database
    db.session.delete(uncategorised_book)
    db.session.commit()

    return redirect("/admin/books_list")





####### data can only be entered by admin
@web.route("/admin" ,methods=['POST','GET'])
def admin_dashboard():
    ####Check if user is already logged in or forgot to logout previous time.
    ####Condition is if admin is already in session & session admin is = param['admin_user'] then directly come in.
    blogs = blog.query.all()
    if ('admin' in session and session['admin'] == param['admin_user']):
        return render_template('admin_temp/dashboard.html',param=param,blogs=blogs)
        
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        if (name == param['admin_user'] and password == param['password']):
            ####set session variable .session is the time between login and logout adn it stores data temporarily. 
            ####name will be stored in a temporary folder named admin.
            session['admin'] = name
            return render_template('admin_temp/dashboard.html',param=param,blogs=blogs)
        else:
            return redirect('/admin')

    return render_template('admin_temp/admin.html')



##########logout
@web.route("/logout")
def logout():
    session.pop('admin')
    return redirect('/admin')


####upload file and add blogs
@web.route("/admin/add_blog" ,methods=['POST','GET'])
def upload_blog():
    if request.method == 'POST':
        try:
            file = request.files['file1']
        except Exception as e : print(e)

        name = request.form.get('title')
        content = request.form.get('desc')
        subtitle = request.form.get('subtitle')

        ###save file in static folder
        try:
            file.save(os.path.join(web.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        except : print("no input")

        try:
            blogs = blog(title=name,subtitle=subtitle,content=content,file=file.filename)
        except : blogs = blog(title=name,subtitle=subtitle,content=content)

        db.session.add(blogs)
        db.session.commit()
        return redirect('/admin')

    return render_template('/admin_temp/add_blogs.html')



################### for books pdf ############################



###add books data in database
#### do not store data in data base instead store name of file in database(original)
@web.route("/admin/bookspdf/special_books" ,methods=['POST','GET'])
def special_book():
    if request.method == 'POST':
        file = request.files['file1']
        file2 = request.files['file2']
        name = request.form.get('title')
        content = request.form.get('desc')

        ###save image file in static folder
        file.save(os.path.join(web.config['UPLOAD_FOLDER'], secure_filename(file.filename)))

        ###save file in static folder
        file2.save(os.path.join(web.config['UPLOAD_FOLDER'], secure_filename(file2.filename)))


        book = special_books(special_books_data=file2.filename, special_books_image = file.filename, special_books_name=name, special_books_content=content)
        db.session.add(book)
        db.session.commit()
        return redirect('/admin/bookspdf')


@web.route("/admin/bookspdf/school_books" ,methods=['POST','GET'])
def school_book():
    if request.method == 'POST':
        file = request.files['file1']
        file2 = request.files['file2']
        name = request.form.get('title')
        content = request.form.get('desc')

        ###save file in static folder
        file.save(os.path.join(web.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        
        ###save file in static folder
        file2.save(os.path.join(web.config['UPLOAD_FOLDER'], secure_filename(file2.filename)))


        book = school_books(school_books_data=file2.filename, school_books_image = file.filename,school_books_name=name,school_books_content=content)
        db.session.add(book)
        db.session.commit()
        return redirect('/admin/bookspdf')


@web.route("/admin/bookspdf/finance_books" ,methods=['POST','GET'])
def finance_book():
    if request.method == 'POST':
        file = request.files['file1']
        file2 = request.files['file2']
        name = request.form.get('title')
        content = request.form.get('desc')

        ###save file in static folder
        file.save(os.path.join(web.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        
        ###save file in static folder
        file2.save(os.path.join(web.config['UPLOAD_FOLDER'], secure_filename(file2.filename)))

        book = finance_books(finance_books_data=file2.filename, finance_books_image = file.filename, finance_books_name=name, finance_books_content=content)
        db.session.add(book)
        db.session.commit()
        return redirect('/admin/bookspdf')


@web.route("/admin/bookspdf/uncategorised" ,methods=['POST','GET'])
def uncategorised():
    if request.method == 'POST':
        file = request.files['file1']
        file2 = request.files['file2']
        name = request.form.get('title')
        content = request.form.get('desc')

        ###save file in static folder
        file.save(os.path.join(web.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        
        ###save file in static folder
        file2.save(os.path.join(web.config['UPLOAD_FOLDER'], secure_filename(file2.filename)))

        book = uncategorised_books(uncategorised_books_data=file2.filename, uncategorised_books_image=file.filename, uncategorised_books_name=name, uncategorised_books_content=content)
        db.session.add(book)
        db.session.commit()
        return redirect('/admin/bookspdf')



###Manage books pdf
@web.route("/admin/bookspdf")
def admin_store():
    return render_template('admin_temp/admin_store.html')



@web.route("/admin/books_list")
def books_list():
    special_book = special_books.query.all()
    school_book = school_books.query.all()
    finance_book = finance_books.query.all()
    uncate = uncategorised_books.query.all()

    return render_template("admin_temp/books_list.html",special_book=special_book,school_book=school_book,finance_book=finance_book,uncate=uncate)


if __name__ == "__main__":
    web.run(debug=False,port=4400)
    
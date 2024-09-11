from crypt import methods

from app.books import books_blueprints
from flask import render_template, request, redirect, url_for
from app.models import Book, db
from app.books.form import BookForm
import os
from werkzeug.utils import secure_filename

@books_blueprints.route("/land",endpoint='land_book')
def landing():
    books=Book.query.all()
    return render_template("books/landing.html", books=books)




@books_blueprints.route("/show/<int:id>",endpoint='show_book')
def showing(id):
    books=Book.query.get(id)

    return render_template("books/detail.html", books=books)


@books_blueprints.route("/delete/<int:id>",endpoint='delete_book')
def deleting(id):
    books=Book.query.get(id)
    if books:
        db.session.delete(books)
        db.session.commit()
    return redirect(url_for('books.land_book'))



@books_blueprints.route("/create", endpoint='create_book',methods=['POST','GET'])
def creating():
    form = BookForm()
    if request.method =='POST':
        if form.validate_on_submit():
            if form.cover_photo.data:
                cover_photo=form.cover_photo.data
                cover_photo_name=secure_filename((cover_photo.filename))
                cover_photo_path=os.path.join('static/images/', cover_photo_name)
                cover_photo.save(cover_photo_path)
            books=Book(title=request.form['title'],
                        description=request.form['description'],
                        cover_photo=cover_photo_name,
                       num_page=request.form['num_page'])
            db.session.add(books)
            db.session.commit()
        # return redirect(url_for('books.landing'))
        return redirect(url_for('books.land_book'))
    return render_template('books/form/create.html', form=form)

@books_blueprints.route("/update/<int:id>", endpoint='update_book',methods=['POST','GET'])
def updating(id):
    books=Book.query.get(id)
    form = BookForm(obj=books)
    if request.method =='POST':
        if form.validate_on_submit():

            if form.cover_photo.data:
                cover_photo=form.cover_photo.data
                cover_photo_name=secure_filename((cover_photo.filename))
                cover_photo_path=os.path.join('static/images/', cover_photo_name)
                cover_photo.save(cover_photo_path)

            # books=Book.query.get(id)
            books.title=request.form['title']
            books.description=request.form['description']
            books.cover_photo=cover_photo_name
            books.num_page=form.num_page.data


            db.session.commit()

        # return redirect(url_for('books.landing'))
        return redirect(url_for('books.land_book'))
    return render_template('books/form/edit.html', form=form)

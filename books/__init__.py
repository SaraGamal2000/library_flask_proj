from flask import Blueprint

books_blueprints=Blueprint("books",__name__, url_prefix="/books")

from  app.books import views
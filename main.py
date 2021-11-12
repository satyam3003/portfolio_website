from flask import Flask, Response, render_template, redirect, url_for, flash, request
from forms import Exp, Pro, Awa, Cert
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sfnsviuh7rvherv4jjk4Wldcsdsdjv'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False, unique=True)
    img = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=True)


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False, unique=True)
    img = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(500), nullable=True)
    body = db.Column(db.Text, nullable=True)


class Awards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False, unique=True)
    img = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(500), nullable=True)
    body = db.Column(db.Text, nullable=True)


class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False, unique=True)
    img = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(500), nullable=True)
    body = db.Column(db.Text, nullable=True)


db.create_all()
db.session.commit()


def save_image(picture_file):
    picture = picture_file.filename
    picture_path = os.path.join(app.root_path, 'static/uploaded_images', picture)
    picture_file.save(picture_path)
    return picture


@app.route('/')
def homepage():
    experience = Experience.query.all()
    awards = Awards.query.all()
    projects = Projects.query.all()
    certificate = Certificate.query.all()

    return render_template('index.html', experience=experience, awards=awards, projects=projects,
                           certificate=certificate)


@app.route('/add/experience', methods=["POST", "GET"])
def form_exp():
    form = Exp()
    if form.validate_on_submit() and request.method == "POST":
        pic = request.files['file']
        image_file = save_image(pic)
        new_experience = Experience(
            title=form.title.data,
            body=form.body.data,
            img=image_file)
        db.session.add(new_experience)
        db.session.commit()
        return redirect(url_for("homepage"))
    return render_template("form.html", form=form, title='Experience')


@app.route('/add/project', methods=["POST", "GET"])
def form_pro():
    form = Pro()
    if form.validate_on_submit() and request.method == "POST":
        pic = request.files['file']
        image_file = save_image(pic)
        new_project = Projects(
            title=form.title.data,
            link=form.link.data,
            body=form.body.data,
            img=image_file)

        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("homepage"))
    return render_template("form.html", form=form, title='Project')


@app.route('/add/award', methods=["POST", "GET"])
def form_awa():
    form = Awa()
    if form.validate_on_submit() and request.method == "POST":
        pic = request.files['file']
        image_file = save_image(pic)
        new_award = Awards(
            title=form.title.data,
            link=form.link.data,
            body=form.body.data, img=image_file)

        db.session.add(new_award)
        db.session.commit()
        return redirect(url_for("homepage"))
    return render_template("form.html", form=form, title='Award')


@app.route('/add/certificate', methods=["POST", "GET"])
def form_cert():
    form = Cert()
    if form.validate_on_submit() and request.method == "POST":
        pic = request.files['file']
        image_file = save_image(pic)
        new_cert = Certificate(
            title=form.title.data,
            link=form.link.data,
            body=form.body.data, img=image_file)

        db.session.add(new_cert)
        db.session.commit()
        return redirect(url_for("homepage"))
    return render_template("form.html", form=form, title='Certificate')


if __name__ == "__main__":
    app.run(debug=True)

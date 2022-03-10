from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged In Successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.about'))
            else:
                flash('Wrong Credentials', category='error')
        else:
            flash('Email does not Exist', category='error')
    
    return render_template('login.html', user=current_user)



@auth.route('/logout')
@login_required
def logout():
    logout_user
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        fullname = request.form.get('fullname')
        pass1 = request.form.get('pass1')
        pass2 = request.form.get('pass2')


        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exist', category='error')
        elif len(email) < 4:
            flash("Length of email should be greated than 3", category='error')
        elif len(fullname) < 2:
            flash("length of name should be greater than 1", category='error')
        elif len(pass1) < 5:
            flash("Password length should be greater than 4", category='error')
        elif pass1 != pass2:
            flash("Password doesn't match", category='error')
        else:
            new_user = User(email=email, fullname=fullname, password=generate_password_hash(pass1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account Created!!!", category='success')
            return redirect(url_for('views.home'))

    return render_template('register.html', user=current_user)


@auth.route('/about')
def about():
    return '<p>about</p>'
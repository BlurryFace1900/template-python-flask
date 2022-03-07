from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return '<p>logout</p>'


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        fullname = request.form.get('fullname')
        pass1 = request.form.get('pass1')
        pass2 = request.form.get('pass2')

        if len(email) < 4:
            flash("Length of email should be greated than 3", category='error')
        elif len(fullname) < 2:
            flash("length of name should be greater than 1", category='error')
        elif len(pass1) < 5:
            flash("Password length should be greater than 4", category='error')
        elif pass1 != pass2:
            flash("Password doesn't match", category='error')
        else:
            flash("Account Created!!!", category='success')


    return render_template('register.html')


@auth.route('/about')
def about():
    return '<p>about</p>'
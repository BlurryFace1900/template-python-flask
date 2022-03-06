from flask import Blueprint, render_template, request

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

    
    return render_template('register.html')


@auth.route('/about')
def about():
    return '<p>about</p>'
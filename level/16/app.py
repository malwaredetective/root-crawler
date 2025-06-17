from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

USERNAME = "hacker"
PASSWORD = "iwantACC3$$totheDEMO!"

@app.route('/demo', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('welcome'))
        else:
            return render_template('login.html', error="Invalid credentials. Please try again.")
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

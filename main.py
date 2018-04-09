from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html', title = "Signup!")

@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verpassword = request.form['verpassword']
    email = request.form['email']
    errordetected = False
    usererror =''
    passerror=''
    verpasserror=''
    emailerror=''
 
    if username == '' or len(username) < 3 or len(username) > 20 or ' ' in (username):
        usererror = "That's not a valid username"
        errordetected = True
    if password == '' or len(password) < 3 or len(password) > 20 or ' ' in (password):
        passerror = "That's not a valid password"
        errordetected = True
    if verpassword != password:
        verpasserror = "Passwords don't match"
        errordetected = True
    if email != '':
        if "@" not in email or "." not in email or len(email) < 3 or len(email) > 20:
            emailerror = "That's not a valid email"
            errordetected = True
    if errordetected == True:        
        return render_template('signup.html', usererror=usererror, passerror=passerror, verpasserror=verpasserror, emailerror=emailerror)
    else:
        return render_template('welcome.html', title="Welcome!", username=username)

app.run()
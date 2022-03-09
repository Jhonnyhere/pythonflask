from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message
 
app = Flask(__name__)

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "jhonnybajaj@gmail.com"
app.config['MAIL_PASSWORD'] = "Bajaj@123"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

app.secret_key = 'vxvxvgcbf345jhjdc'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://actecal:actecal12345@ACTECALSERVER:3306/clientdata'

db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")

class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(35))
   email = db.Column(db.String(50))
   message = db.Column(db.String(100))

   def __init__(self, name, email, message):
    self.name = name
    self.email = email
    self.message = message
       
 
@app.route('/show')
def show_all():
   return render_template('show_all.html', students = students.query.all() )


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        clientdata=students(name=name, email=email,message=message)                 
        db.session.add(clientdata)
        db.session.commit()
        mail.send_message(
            sender= email,
            recipients=[app.config['MAIL_USERNAME']],
            body= message
            )
        flash('Record was successfully added')
        return redirect(url_for('show_all'))
    return render_template('contact.html')

@app.route("/price")
def price():
    return render_template("price.html")

@app.route("/services")
def services():
    # j = open('video.json')

    # videos = json.load(j) # or from database mysql
    title="My videos"
    return render_template("services.html",title=title)


@app.route("/subscribe")
def subscribe():
    return render_template("subscribe.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/works")
def works():
    return render_template("works.html")

@app.route("/about")    
def about():
    return render_template("about.html")


if __name__ =="__main__":
    db.create_all()
    app.run(debug=True,port=8000)


from flask import Flask , render_template , abort ,request,redirect,url_for
from model import db , save_db

app = Flask(__name__)

@app.route("/")
def home():
    return (render_template("home.html"))


@app.route("/about")
def about():
    return ("student_data")

@app.route("/team")
def team():
    return ("team_detail")

@app.route("/<int:index>")
def detail(index):
    try:
        registration = db[index]
        return render_template("detail.html", registration=registration,index=index,max_index=len(db)-1)
    except IndexError:
        abort(401)

@app.route("/registration", methods=["GET","POST"])
def registration():
    if request.method == "POST":
        card = {"name": request.form["name"],
                "father_name": request.form["father_name"],
                "address": request.form["address"],
                "address2": request.form["address2"],
                "city": request.form["city"],
                "state": request.form["state"],
                "zip": request.form["zip"]}
        db.append(card)
        save_db()
        return redirect( url_for("detail", index=len(db)-1))
    else:
        return render_template("form.html")

    
if __name__ == "__main__" :
    app.run(debug=True,port=2000)
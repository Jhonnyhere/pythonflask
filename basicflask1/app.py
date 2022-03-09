from flask import Flask , render_template , abort ,request,redirect,url_for
from model import data , save, save_data

app = Flask(__name__)

@app.route("/")
def home():
    return (render_template("basicForm.html"))

@app.route("/<int:index>")
def detail(index):
    try:
        form = data[index]
        return render_template("basicForm.html", data=data,index=index,max_index=len(data)-1)
    except IndexError:
        abort(401)
        
        
@app.route("/data", methods=["GET","POST"])
def data():
        if request.method == "POST":
            info = {"name": request.form["name"],
                    "father_name": request.form["father_name"],
                    "dob": request.form["dob"],
                    "gender": request.form["gender"],
                    "address": request.form["address"],
                    "mobile_no": request.form["mobile"],
                    "email": request.form["email"]}
            data.append()
            save_data()    
            return redirect( url_for("detail"))
        else:
            return render_template("basic.form.html")
    

    
if __name__ == "__main__" :
    app.run(debug=True)    
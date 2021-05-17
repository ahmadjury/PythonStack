from flask import Flask, render_template ,request
from werkzeug.utils import redirect
app = Flask(__name__)   

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/result',methods = ["POST"])
def result():
    name = request.form["name"]
    Dojo_Location = request.form["Dojo_Location"]
    Favorite_Language = request.form["Favorite_Language"]
    comment = request.form["comment"]
    return render_template("results.html", name = name, Dojo_Location=Dojo_Location
                                            , Favorite_Language=Favorite_Language
                                                ,comment=comment)



if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def index0():
#     return render_template("index.html",num_square =3,square_color="aqua")

# @app.route('/play/<num>')
# def index(num):
#     return render_template("index.html",num_square =int(num))

# @app.route('/play/<num>/<color>')
# def index1(num,color):
#     return render_template("index.html",num_square =int(num),square_color=color)

@app.route('/')
@app.route('/play/<num>')
@app.route('/play/<num>/<color>')
def index1(num = 3,color ="aqua"):
    return render_template("index.html",num_square =int(num),square_color=color)




if __name__=="__main__":
    app.run(debug=True)
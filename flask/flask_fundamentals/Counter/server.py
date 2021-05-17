from types import MethodDescriptorType
from flask import Flask, render_template ,request,session
from werkzeug.utils import redirect
app = Flask(__name__) 
app.secret_key="mahmoud anabousi"

@app.route('/')
def index():
    if "count" in session:
        session["count"]+=1
    else:
        session["count"]=1
    
    if "count2" in session:
        session["count2"]+=1
    else:
        session["count2"]=1
    
    return render_template("index.html",count=session["count"],count2=session["count2"])

@app.route('/destroy')
def destroy():
    session.clear()	
    return redirect ('/')


@app.route('/add2')
def add2():
    session["count"]+=1   
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop("count")
    return redirect('/')

# @app.route('/addnum', methods = ['POST'])
# def add():
#     num=request.form['num']
#     session["count"]+=int(num)
#     return render_template("index.html",count=session["count"],count2=session["count2"]) 



    
if __name__ == "__main__":
    app.run(debug=True)
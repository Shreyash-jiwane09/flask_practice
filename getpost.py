from flask import Flask,render_template,request


app = Flask(__name__)

@app.route("/form",methods = ['GET','POST'])
def form():
    if request.method == "POST":
        name = request.form['name']
        mobile = request.form['mobile']
        return f"Hello myself {name} and my contact number is {mobile}"
    return render_template("form.html")

#variable rule
#Jinja2 Template engine 
"""
{{}} Expression to print output in html
{%....%} conditions .for loop
{#...#}single line comment  
"""
@app.route("/sucess/<int:score>")
def marks(score):
    res = ""
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"
    return render_template('result.html',results = res)



if __name__ == "__main__":
    app.run(debug = True)
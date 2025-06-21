from flask  import Flask,redirect,url_for,request,render_template
app=Flask(__name__)

@app.route("/")
def home():
  return render_template("hii.html")

@app.route("/add",methods=["GET","POST"])
def add():
  if request.method=="POST":
    num1=request.form.get("num1",type=int)
    num2=request.form.get("num2",type=int)
    return f"the addition is {num1+num2}"
  return render_template("add.html")

@app.route("/subtract", methods=["GET", "POST"])
def subtract():
    if request.method == "POST":
      num1 = request.form.get("num1", type=float)
      num2 = request.form.get("num2", type=float)
      return f"<h1>The result of subtraction is {num1 - num2}</h2>"
    return render_template("subtract.html")

@app.route("/multiply", methods=["GET", "POST"])
def multiply():
    if request.method == "POST":
      num1 = request.form.get("num1", type=float)
      num2 = request.form.get("num2", type=float)
      return f"The result of multiplication is {num1 * num2}"
    return render_template("multiply.html")

@app.route("/divide", methods=["GET", "POST"])
def divide():
    if request.method == "POST":
      num1 = request.form.get("num1", type=float)
      num2 = request.form.get("num2", type=float)
      if num2 == 0:
        return "Division by zero is not allowed."
      return f"The result of division is {num1 / num2}"
    return render_template("divide.html")



































if __name__ == '__main__':
  app.run(debug=True)
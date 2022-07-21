from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
        return render_template("index.html")


@app.route('/about.html', methods =['GET', 'POST'])
def about():
    if request.method == 'GET':
        return render_template("about.html")


@app.route('/form.html', methods = ['GET', 'POST'])
def func_form():
    if request.method == 'GET':
        return render_template("form.html")
    else:
        if request.method == 'POST':
            return render_template("result.html")
    

@app.route('/result.html', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        return render_template("/result.html")


@app.route('/index.html', methods = ['GET', 'POST'])
def functie2():
    if request.method == 'GET':
        return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("FailPage.html")

if __name__ == '__main__':
    app.run(debug = True)

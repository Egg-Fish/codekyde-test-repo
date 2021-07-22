from quadratic import quadratic
from triangle import triangle
from flask import Flask, render_template, request, send_file

app = Flask(__name__)
app.config["SECRET_KEY"] = "sussybaka"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        a = int(request.form["a"])
        b = int(request.form["b"])
        c = int(request.form["c"])

        quadratic_result = quadratic(a, b, c)
        triangle_result = triangle(a, b, c)

        print(quadratic_result, triangle_result)
        return render_template("result.html", quadratic_result=quadratic_result, triangle_result=triangle_result)

if __name__ == '__main__':
    app.run(host='localhost', port=80)

    
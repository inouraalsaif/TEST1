from flask import Flask, render_template, request


print('hello')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('basic.html')

@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['search']
    print(name)
    return render_template('header.html',n=name)
if __name__ == '__main__':
    app.run(debug=True)
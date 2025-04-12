from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login/login.html')

@app.route('/Note')
def Note():
    return "Note"

if __name__=='__main__':
    app.run(debug=True) #Hay que eliminar debug=True
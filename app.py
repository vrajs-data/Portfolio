from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    # return render_template('projects.html')
    return "Projects page works!"

@app.route('/test')
def test():
    return "Flask is working!"
    
if __name__ == '__main__':
    app.run(debug=True)

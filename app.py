# flask application entry point
from flask import Flask, render_template

app = Flask(__name__, 
            template_folder='frontend/templates',
            static_folder='frontend/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    # Placeholder for now
    return render_template('index.html', success="Backend not implemented yet!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
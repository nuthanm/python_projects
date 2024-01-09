from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculatebmi', methods=['POST'])
def calculate():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])

        # BMI Calculation
        bmi = weight / (height * height)

        return render_template('index.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        operation = request.form['operation']
        num1 = float(request.form['num1'])
        num2 = float(request.form.get('num2', 0))
        result = None

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
        elif operation == 'square':
            result = num1 ** 2
        elif operation == 'sqrt':
            result = math.sqrt(num1)
        elif operation == 'sin':
            result = math.sin(math.radians(num1))
        elif operation == 'cos':
            result = math.cos(math.radians(num1))
        elif operation == 'tan':
            result = math.tan(math.radians(num1))

        return render_template('calculator.html', result=result)
    except Exception as e:
        return render_template('calculator.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

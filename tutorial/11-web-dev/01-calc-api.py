from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the calculator
html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculator</title>
    </head>
    <body>
        <h2>Simple Calculator</h2>
        <form method="POST">
            <input type="text" name="num1" placeholder="Number 1" required>
            <input type="text" name="num2" placeholder="Number 2" required>
            <input type="submit" value="Calculate Sum">
        </form>
        {% if result %}
            <h3>Result: {{ result }}</h3>
        {% endif %}
    </body>
    </html>
'''

@app.route('/', methods=['GET', 'POST'])
def calculate():
    result = None
    if request.method == 'POST':
        # Extract numbers from form data
        num1 = request.form.get('num1', type=float)
        num2 = request.form.get('num2', type=float)
        result = num1 + num2
    return render_template_string(html, result=result)

if __name__ == '__main__':
    app.run(debug=True)

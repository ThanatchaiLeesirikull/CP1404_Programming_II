from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def convert_celsius_to_fahrenheit(Celsius):
    return (Celsius * 9 / 5) + 32


@app.route('/')
def introduction():
    return "Welcome to the Celsius to Fahrenheit Converter!"


@app.route('/convert/<float:celsius>')
def convert_to_fahrenheit(celsius):
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    result_text = f"{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit."
    return result_text


if __name__ == '__main__':
    app.run()

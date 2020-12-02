from app import app
from modules.calculator import *

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/add/<num1>/<num2>')
def add_my_num(num1, num2):
    return f"the answer is {add(int(num1),int(num2))}"

@app.route('/subtract/<num1>/<num2>')
def subtract_my_num(num1, num2):
    return f"the answer is {subtract(int(num1),int(num2))}"

@app.route('/multiply/<num1>/<num2>')
def multiply_my_num(num1, num2):
    return f"the answer is {multiply(int(num1),int(num2))}"

@app.route('/divide/<num1>/<num2>')
def divide_my_num(num1, num2):
    return f"the answer is {divide(int(num1),int(num2))}"





   
    



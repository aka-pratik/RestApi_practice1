from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/') # a decorator provided by flask to assign url in our app to functions easily
def hello_world():
    return 'Hello, World!'

@app.route('/sum', methods = ['POST'])
def sum():
    if (request.method == 'POST'):
        operation = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']
        if (operation == "add"):
            r = num1 + num2
            result = f"The sum of {num1} and {num2} is {r}"
        return jsonify(result)
@app.route('/square/<int:n>')
def square(n):
    # return str(n**2) #returned value must be a string, dictionary, tuple, etc. but can't be an int
    result = {"Given no." : n,
              "Squared value" : n**2,
              "Giving output" : True
    }
    return jsonify(result) #converts the object into proper json structure


@app.route('/testget', methods=['GET'])
def testgetapi():
    return "I am from GET api"

@app.route('/testpost', methods=['POST'])
def testpostapi():
    return "I am from POST api"

app.run(debug= True)
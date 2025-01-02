from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/armstrong/<int:n>')
def armstrong_route(n):
    return armstrong(n)

def armstrong(n):
    sum = 0  # starting from zero
    order = len(str(n))  # for get a number from the given input
    copy_n = n  # for not getting less then zero
    while n > 0:  # the loop will run until the number is greater than zero
        digit = n % 10
        sum = sum + digit ** order
        n = n // 10
    if sum == copy_n:
        print(f"{copy_n} is an armstrong number")
        result = {
            "number": copy_n,
            "is_armstrong": True,
            "server": "123.233.233.12",
            "Message":"this is a armstrong number"
        }
    else:
        print(f"{copy_n} is not an armstrong number")
        result = {
            "number": copy_n,
            "is_armstrong": False,
            "server": "123.233.233.12",
            "Message":"this is not a armstrong number"
        }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
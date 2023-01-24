from flask import Flask,request, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/num")
def num():
  data = request.args
  req_number = data['num']
  number = int(req_number)+100
  return jsonify({'num':  str(number)})

if __name__ == "__main__":
    app.run()

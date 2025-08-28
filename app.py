from flask import flask 

app =flask(__name__)

@app.route('/welcome')
def hello():
  return "everythings working phhh!"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_cloud():
  return 'Hello from Mahara ECS Container. 2nd Time'

app.run(host='0.0.0.0')

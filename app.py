from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def index():
    return 'om namah shivaya'
if __name__ =="__main__":
    app.run()
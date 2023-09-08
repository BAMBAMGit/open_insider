from flask import Flask, render_template
from myscript import result, mydate, df

app = Flask(__name__)

@app.route('/')
def index():
    # Your Python code goes here
    
    result = "hello world"
    return render_template('index.html', result=result) #, mydate=mydate, df=df)

if __name__ == '__main__':
    app.run(debug=True)

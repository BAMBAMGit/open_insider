from flask import Flask, render_template
from api.myscript import result, mydate, df

app = Flask(__name__)

@app.route('/')
def index():
    # Your Python code goes here
    
    return render_template('index.html', result=result, mydate=mydate, df=df)

if __name__ == '__main__':
    app.run(debug=True)

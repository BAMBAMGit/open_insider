from flask import Flask, render_template
from api.datetime_helper import date_reformatted_start
from api.scrape_and_store_df import table_html

app = Flask(__name__)

@app.route('/')
def home():
    # Your Python code goes here
    
    # return "hello world"

    return render_template('index.html', result="hello world!!!", mydate=date_reformatted_start, df=table_html)

# if __name__ == '__main__':
#     app.run()
    # app.run(debug=True)

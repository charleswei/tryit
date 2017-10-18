from flask import Flask,render_template
import pandas as pd

app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
     df = pd.read_csv('raycom.csv')
     #a = str(len(df))
     return render_template('form.html',user=df.Group[1])

if __name__ == '__main__':
   app.run()



from flask import Flask,request,render_template
import pickle
import pandas as pd
import sklearn

app = Flask(__name__)

kodel = pickle.load(open('score1.pkl','rb'))


@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')





@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        hours = float(request.form['hours'])

        prediction = kodel.predict([[hours]])
        output = round(prediction[0][0],2)  

        return render_template('show.html',text='Your percentage is {}%'.format(output))
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)

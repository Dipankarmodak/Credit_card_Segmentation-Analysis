from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('cluster_model.joblib')



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        Monthly_avg_purchase= float(request.form["month_avg_purchase"])
        Monthly_avg_cash= float(request.form["month_avg_cash"])
        Limit_usage= float(request.form["limit_usage"])
        Payment_ratio= float(request.form["payment_ratio"])
        
        Type_of_purchase=request.form['type_of_purchase']
        if(Type_of_purchase=='No_purchase'):
           No_purchase = 1
           One_of_purchase = 0
           Installment_purchase = 0
           Both_purchase = 0
          
        elif (Type_of_purchase=='One_of_purchase'):
           No_purchase = 0
           One_of_purchase = 1
           Installment_purchase = 0
           Both_purchase = 0

        elif (Type_of_purchase=='Installment_purchase'):
            No_purchase = 0
            One_of_purchase = 0
            Installment_purchase = 1
            Both_purchase = 0
            
        elif (Type_of_purchase=='Both_purchase'):
            No_purchase = 0
            One_of_purchase = 0
            Installment_purchase = 0
            Both_purchase = 1
            
        else:
            No_purchase = 0
            One_of_purchase = 0
            Installment_purchase = 0
            Both_purchase = 0
           
        prediction=model.predict([[
                    Monthly_avg_purchase,
                    Monthly_avg_cash,
                    Limit_usage,
                    Payment_ratio,
                    No_purchase ,
                    One_of_purchase ,
                    Installment_purchase ,
                    Both_purchase
                ]])
        
        output=prediction[0]
        
        return render_template('home.html',prediction_text="The customer belongs to group {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
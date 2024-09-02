# Importing packages
from src.components.create_custom_data import CustomData
from src.pipelines.predict_pipeline import PredictPipeline
from flask import Flask, render_template, jsonify, request

# Instantiating the Flask app
app = Flask(__name__)

# Creating the home page
@app.route('/')
def index():
    '''
    This function creates the home page. 
    '''
    return render_template('index.html')

# Creating the function to predict datapoints
@app.route('/predict.html', methods=['GET', 'POST'])
def predict_datapoint():
    '''
    This function will display the prediction landing page if the method is "GET".
    If the method is "POST", the function will run the prediction.
    '''
    # Display the prediction landing page if request method is "GET"
    if request.method == "GET":
        return render_template('predict.html')
    else:
        # If the request method is not "GET", run the prediction
        data = CustomData(
            carat = float(request.form.get('carat')),
            cut = str(request.form.get('cut')),
            color = str(request.form.get('color')),
            clarity = str(request.form.get('clarity')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z'))
        )
        
        # Creating a dataframe from the custom data
        df = data.create_dataframe()
        
        # Instantiating the prediction pipeline and making predictions
        predictions = PredictPipeline()
        preds = predictions.predict(df)
        
        return render_template('predict.html', results=preds, pred_df=df)
    
# Creating the function to define an API call
def predicti_api():
    '''
    This function will create an api and return the predictions in as a
    JSON file.
    '''
    # Creating the api
    if request.method == "POST":
        data = CustomData(
            carat = float(request.form.get('carat')),
            cut = str(request.form.get('cut')),
            color = str(request.form.get('color')),
            clarity = str(request.form.get('clarity')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z'))
        )
        
         # Creating a dataframe from the custom data
        df = data.create_dataframe()
        
        # Instantiating the prediction pipeline and making predictions
        predictions = PredictPipeline()
        preds = predictions.predict(df)
        
        # Creating a dictionary to convert to a json format
        preds_dict = {'Prediction': preds}
        
        return jsonify(preds_dict)


# Running the script
if __name__ == '__main__':
    app.run(debug=True)
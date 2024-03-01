
from logger_file.logger import logger
import sys
from flask import Flask , render_template, request
import numpy as np
from Exception_file.exception import CustomException
from src.Titanic_Survival_Prediction_with_MLflow.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)


@app.route('/predict', methods = ['POST', 'GET'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    
    else:
        try:
            Pclass = int(request.form['Pclass'])
            Sex = request.form['Sex']
            Age = int(request.form['Age'])
            SibSp = int(request.form['SibSp'])
            Parch = int(request.form['Parch'])
            Fare = int(request.form['Fare'])
            Embarked = str(request.form['Embarked'])



            data = [Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]


            data = np.array(data).reshape(1, 7)

            obj = PredictionPipeline()
            results = obj.predict(data)



            return render_template('index.html', results = results)
        
        except Exception as e:
            raise CustomException(e , sys)
        


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
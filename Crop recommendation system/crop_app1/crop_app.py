from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/Predict')
def prediction():
    return render_template('Index.html')

@app.route('/form', methods=["POST"])
def brain():
    Nitrogen = float(request.form['Nitrogen'])
    Phosphorus = float(request.form['Phosphorus'])
    Potassium = float(request.form['Potassium'])
    Temperature = float(request.form['Temperature'])
    Humidity = float(request.form['Humidity'])
    Ph = float(request.form['ph'])
    Rainfall = float(request.form['Rainfall'])
     
    values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]
    
    if 0 < Ph <= 14 and Temperature < 100 and Humidity > 0:
        try:
            import joblib
            model = joblib.load('crop_app1/crop_app')

            arr = [values]
            acc = model.predict(arr)
            return render_template('prediction.html', prediction=str(acc))
        except FileNotFoundError:
            return "Model file not found. Please ensure that the model file 'crop_app' exists."
    else:
        return "Sorry...  Error in entered values in the form. Please check the values and fill it again."

if __name__ == '__main__':
     app.run(debug=True, port=8080)

from flask import Flask,render_template,request
from source.main_project.pipeline.predict_pipeline import UserData,PredicPipeline

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('income.html')

@app.route('/predict',methods=['POST'])
def do_prediction():
    data = UserData(
    age=request.form.get('age'),
    workclass=request.form.get('workclass'),
    education=request.form.get('education'),
    marital=request.form.get('marital-status'),
    occupation=request.form.get('occupation'),
    relationship=request.form.get('relationship'),
    race=request.form.get('race'),
    gender=request.form.get('gender')
    )
    user_df = data.get_data_as_df()

    predict_pipe = PredicPipeline()
    results = predict_pipe.predict(user_df)

    msg = 'Income is greater than $50k' if results == 1 else 'Income is less than $50k'

    return render_template('income.html',text = msg)

if __name__ == "__main__":
    app.run(debug=True)
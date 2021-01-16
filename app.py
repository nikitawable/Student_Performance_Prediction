from flask import flask,render_template_request
import pickle
import numpy as np
app=Flask(__name__)

model=pickl(e.load(open('model.pkl','rb'))
@app.route('/')
def home (): 
    return render_template('studentperformance.html')

@app.route('/predict',methods=['POST']) 
def predict ():

    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction=model.predict_proba(final)
    output=round(prediction[0],2)
    return render_template(studentperformance.html,prediction_text='Student Performance should be $ {}'.format(output))
if __name__=='__main__':
    app.run()
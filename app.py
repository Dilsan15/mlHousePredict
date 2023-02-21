from flask import Flask, render_template, request

import utils

app = Flask(__name__)


# GET form data, put it through the model, and return the prediction

@app.route('/', methods=['GET', 'POST'])
def input_page():

    if request.method == 'POST':
        print(request.form)
        return render_template('index.html', prediction=utils.predict_input(request.form))

    elif request.method == 'GET':
        return render_template('index.html')



# Run App
if __name__ == '__main__':
    app.run()


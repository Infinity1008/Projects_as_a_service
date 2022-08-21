from flask import Flask, request, Response, jsonify, render_template, flash, url_for,redirect
from custom_functions import detect_language_properties_from_predictions,detect_language_from_code
import argparse
from forms import Languageinput
import pdb

########################################################################
# Getting the location of the model from the user
parser = argparse.ArgumentParser(description='Please give the location of the model')
parser.add_argument('location', metavar='Location', type=str, help='Location of the model')

args = parser.parse_args()
location = args.location
print(location)
########################################################################

# Loading the model
import fasttext

PRETRAINED_MODEL_PATH = location
model = fasttext.load_model(PRETRAINED_MODEL_PATH)


########################################################################

app = Flask(__name__)
app.config['SECRET_KEY'] = '9321d167db0ab08ddaedbee0c45ebeba'

@app.route('/',methods=['POST','GET'])
@app.route('/home',methods=['POST','GET'])
def home():
    form = Languageinput()
    if form.validate_on_submit():
        text = form.lang_input.data

        value = model.predict(text)
        print(value)

        # loading model and giving output
        lang_code, confidence = detect_language_properties_from_predictions(value)
        print(lang_code, confidence)

        lang_name_full = detect_language_from_code(lang_code)
        print(lang_name_full)
        flash(f'Language code: {lang_code}      |      Confidence: {confidence}      |      Language Full name: {lang_name_full}','success')
        return render_template('home.html', form = form)

    return render_template('home.html',form=form)

@app.route('/detect_language', methods=['POST'])
def detect_language():
    # Reading the data
    print('Hit Confirmed')
    req_data = request.get_data()

    print('Data read')
    req_data_string = req_data.decode()

    # Get prediction from model
    value = model.predict(req_data_string)
    print(value)

    # loading model and giving output
    lang_code, confidence = detect_language_properties_from_predictions(value)
    print(lang_code,confidence)

    lang_name_full = detect_language_from_code(lang_code)
    print(lang_name_full)

    return jsonify(lang_code=lang_code, confidence=confidence, lang_full_name=lang_name_full)



@app.route('/help', methods=['POST', 'GET'])
def help():
    about = 'This service will give you a language code, language name and a confidence probability of the prediction'
    exp_input_desp = 'This service is expecting inputs to be a string'
    exp_output_desp = 'The output is a json with three keys being, (lang_code, confidence, lang_name_full)'
    exp_input_example = "result = requests.post(url=address, data=Your string here)"
    exp_output_example = 'Json with 3 keys (lang_code, confidence, lang_name_full)'
    if_you_want_to_try_it_out = '''
        import requests
        server_address = 'http://address_here with port/detect_language'
        result = requests.post(url=server_address, data=Your string here)
        print("Response recieved")
        result.json()
        '''
    return jsonify(about=about, expected_input=exp_input_desp, expected_output=exp_output_desp,
                   input_eg=exp_input_example, output_eg=exp_output_example,
                   if_you_want_to_try_it_out=if_you_want_to_try_it_out)

if __name__ == '__main__':
    # Loading the models
    app.run(host='0.0.0.0',debug=True)
    # host='0.0.0.0', debug=True, port=50500
    # href = "{{ }}"

# todo make it so that when you input text in the browser and enter that the text doesn't go away

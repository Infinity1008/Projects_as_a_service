import numpy as np
from flask import Flask, request, Response, jsonify
from custom_functions import load_glove_model, np_array_to_byte_array
import argparse
import re

########################################################################
# Getting the location of the model from the user
parser = argparse.ArgumentParser(description='Please give the location of the model')
parser.add_argument('location', metavar='Location', type=str,help='Location of the model')


args = parser.parse_args()
location = args.location
print(location)
########################################################################

# Loading the model
model = load_glove_model(location)

########################################################################

app = Flask(__name__)

@app.route('/vectorizer_word', methods=['POST'])
def vectorizer_word():
    # Reading the data
    print('Hit Confirmed')
    req_data = request.get_data()

    print('Data read')
    req_data_string = req_data.decode()

    # Making sure it's lower case, otherwise the model will throw an error
    req_data_string = req_data_string.lower()

    # Splits at space
    tokens = re.findall("[\w']+", req_data_string)

    # loading model and giving output
    try:
        vector = model[tokens[0]]
    except:
        vector = np.array(0)

    byte_array = np_array_to_byte_array(vector)

    return Response(response=byte_array, status=200, mimetype="application/octet_stream")

@app.route('/vectorizer_sentence', methods=['POST'])
def vectorizer_sentence():
    # Reading the data
    print('Hit Confirmed')
    req_data = request.get_data()

    print('Data read')
    req_data_string = req_data.decode()

    # Making sure it's lower case, otherwise the model will throw an error
    req_data_string = req_data_string.lower()

    # Splits at space
    tokens = re.findall("[\w']+", req_data_string)

    vector_list = []
    for i in tokens:
        try:
            vector = model[i]
            vector_list.append(vector)
        except:
            vector = np.array(0)
            vector_list.append(vector)

    vector_list = np.array(vector_list)
    byte_array = np_array_to_byte_array(vector_list)

    return Response(response=byte_array, status=200, mimetype="application/octet_stream")



@app.route('/help', methods=['POST','GET'])
def help():
    about = 'This service will give give you one vector for one word. Or it you send a sentence, it will give you 1 vector per word ' \
                'You can send one word at a time with the header of data in your request and it will return an ' \
                'byte array that you have to convert to numpy array, ' \
                'that numpy array contains the word vector of the word that you sent in the request.' \
            'Or if you send a sentence, it will give you 1 vector per word, for any word whose vector is not available in the model.' \
            'A numpy array with value 0 will be sent bacl'

    exp_input_desp = 'This service is expecting inputs to be a string'
    exp_output_desp = 'The output is a numpy array converted into byte array for all the words given in the input converted into vectors and saved in a byte array format'
    exp_input_example = "result = requests.post(url=aws_address, data=Your string here)"
    exp_output_example = 'Numpy array saved as a Byte array, open this with numpy loads and io.BytesIO'
    if_you_want_to_try_it_out = '''
        import requests
        import io
        import numpy as np

        def np_array_to_byte_array(x):
            bytestream = io.BytesIO()
            np.save(bytestream, x)
            temp = bytestream.getvalue()
            return temp

        def byte_array_to_np_array(x):
            temp = np.load(io.BytesIO(x),allow_pickle=True)
            return temp

        
        server_address = 'http://address_here with port/vectorizer_word'

        result = requests.post(url=server_address, data=Your string here)
        print("Response recieved")


        result = byte_array_to_np_array(result.content)
        result
        '''
    return jsonify(about=about, expected_input=exp_input_desp, expected_output=exp_output_desp,
                   input_eg=exp_input_example, output_eg=exp_output_example,
                   if_you_want_to_try_it_out=if_you_want_to_try_it_out)


if __name__ == '__main__':
    # Loading the models
    app.run(host='0.0.0.0')
    # host='0.0.0.0', debug=True, port=50500


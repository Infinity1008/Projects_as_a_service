# Language_detection
A language detection service that you can run in a python environment or a docker container, where you can send in some text and get back the language it is in!

## Installation
To install the project and run within a python3 virtual environment, create a python virtual environment and do as instructed below  
```
git clone https://github.com/Infinity1008/Language_detection.git
pip install requirements.txt
```
## Fasttext Model
To get the fasttext language detection model from facebook website, use this [link](https://fasttext.cc/docs/en/language-identification.html#content), or you can download directly from [here](https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin).

## To run the flask server
Then run the flask server while giving it the model location 
```
python3 main.py model_location
```

## Usage
You can access the service via a **web browser** on your local ip with the port 5000 on the [127.0.0.1:5000](127.0.0.1:5000). It will look like this
![Language_detection_demo_image](static/images/Language_detection_demo.png?raw=true "Language Detection Demo")
For some input it will return 3 values.
1. **Language Code** - This is the language code for the detected language
2. **Confidence** - This is how sure the model is that the predicted language code is correct, you can set a threshold value here and filter unsure results on client end.
3. **Language full name** - This is using a separate library [pycountry](https://pypi.org/project/pycountry/) that is converting the code into full language name.

![Language_detection_demo_image](static/images/Language_detection_demo_running.png?raw=true "Language Detection Demo")

Trying out some other languages 

![Language_detection_demo_image](static/images/Language_detection_demo_french.png?raw=true "Language Detection Demo")

### To access via API's
Use python3 requests library or any other way you want to access this api service.
Example
```
import requests
address = 'http://127.0.0.1:5000/detect_language'
result = requests.post(address,data='What are you doing')
result.json()
```

The result will look like this
```
{'confidence': 0.9973926544189453, 'lang_code': 'en', 'lang_full_name': 'English'}
```

To get help about how to access the service there is a help address that you can put a get request on.
```
import requests
address = 'http://127.0.0.1:5000/help'
result = requests.get(url=address)
result.json()
```

# To access via Docker
You can build a docker image with the dockerfile after cloneing the repo. Like this
```
docker build Language_detection -t nameofyourcontainer
```
Then run the container and bind the port 5000 of the container to any port of your machine if you wish to access it locally.
Run the container like this

```
docker run -it -p 5000:5000 nameofyourcontainer
```
This will run the container in attached mode, if you wish to run deattached, just remove the `-it` flags from the command.
## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

 
## License
MIT License


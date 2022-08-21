# Glove vectorisation server

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [To access the service using API calls](#to-access-the-service-using-api-calls)
* [To access via a docker container](#to access via a docker container)

## General info
This is a glove word vectoriser server, where you can send a word/sentence to get the vectors. If you don't want to set up the model and all the code that comes with that yourself, you can just use this service using python3 or use the docker container to do POST request on and get vector embeddings. You can then use these vector embedding to do whatever you wish. (Similarity, closenes, average, weighted average etc.)

## Where to get the models from
You can get different glove models from the [stanford nlp website](https://nlp.stanford.edu/projects/glove/), some of the links are here:
* [glove.6B.zip](https://nlp.stanford.edu/data/glove.6B.zip) Wikipedia 2014 + Gigaword 5 (6B tokens, 400K vocab, uncased, 50d, 100d, 200d, & 300d vectors, 822 MB)
* [glove.42B.300d.zip](https://nlp.stanford.edu/data/glove.42B.300d.zip) Common Crawl (42B tokens, 1.9M vocab, uncased, 300d vectors, 1.75 GB)
* [glove.840B.300d.zip](https://nlp.stanford.edu/data/glove.840B.300d.zip) Common Crawl (840B tokens, 2.2M vocab, cased, 300d vectors, 2.03 GB)
* [glove.twitter.27B.zip](https://nlp.stanford.edu/data/glove.twitter.27B.zip) Twitter (2B tweets, 27B tokens, 1.2M vocab, uncased, 25d, 50d, 100d, & 200d vectors, 1.42 GB)

Download the model of your choice, unzip it and then select the path of the model version you are going to use, 
whichever version of the model you will use, it will give back the vectors accordingly. If you use the model with 50 vector size, it will return a word vector of size 50. 
There are options for vector size of 50,100,200,300


## Technologies
Project is created with:
* Python3
* Flask
* Requests
	
## Setup
To run this project, clone it to a local repository, make a python3 environment with requirements.txt and run the flask_server.py file with the location on the model as shown:

```
python3 flask_server.py model_location_here
```
Whatever model size you choose(50,100,200,300), you will get the vector of the same size back.

## To access the service using API calls
You can then access the flask server on you localhost port 5000, with python library request or any other way you wish.

**If you send words which have no vectors in the model, you will get a numpy array with 0 in it.
Example(Numbers, 'abchdf' etc)

**For a single word**
```
import requests
address = 'http://127.0.0.1:5000/vectorizer_word'
result = requests.post(url=address, data='words')
byte_array = result.content
```
The result you will get here is going to be a byte array, you will need to convert the byte array to numpy array for further use

Note: If you send a sentence in the word vector service, it will just going to give you the vector for the first word.

**For a sentence**

```
import requests
address = 'http://127.0.0.1:5000/vectorizer_sentence'
result = requests.post(url=address, data='Your sentence here')
byte_array = result.content
```

The result if going to be numpy array of all the word vectors in your sentence.
If there is a word for which no vector is found, it will return a numpy array with 0.

**To load the byte array**
```
import io
import numpy as np
numpy_array = np.load(io.BytesIO(byte_array),allow_pickle=True)
```
This numpy arrays are going to be vector of the words you sent in the POST request

## To access via a docker container
Build the docker file with 
```
git clone https://github.com/Infinity1008/Glove_vectorizer_service.git
docker build Glove_vectorizer -t nameofyourcontainer
```

You can select model with 50,100,200,300 vectors. Just specify the model name at the time of running the image.

**Like this**

Model that gives vector of 50D

```
docker run nameofyourcontainer glove.6B.50d.txt
```
**or**

Model that gives vector of 300D
```
docker run nameofyourcontainer glove.6B.300d.txt
```
and so on. If you don't specify any model name, it will use the model with 100D vectors 

To access the container on a specific port, use docker run command and bind the port 5000 of your container to 
any port you want and access the service on the same port. Here i have bound the port 5000 of container
to the port 5000 of the local machine

```
docker run -p 5000:5000 nameofyourcontainer glove.6B.100d.txt 
```
You can now access the API services on **http://127.0.0.1:5000/vectorizer_word** and so on.

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

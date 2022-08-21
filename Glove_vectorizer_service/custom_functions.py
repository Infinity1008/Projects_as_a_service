import numpy as np
import io

# Loading model
def load_glove_model(File):
    print("Loading Glove Model")
    glove_model = {}
    with open(File,'r') as f:
        for line in f:
            split_line = line.split()
            word = split_line[0]
            embedding = np.array(split_line[1:], dtype=np.float64)
            glove_model[word] = embedding
    print(f"{len(glove_model)} words loaded!")
    return glove_model

# Code for converting the response vector array to byte array
def np_array_to_byte_array(x):
    bytestream = io.BytesIO()
    np.save(bytestream, x)
    temp = bytestream.getvalue()
    return temp

# Code for converting the byte array to response vector array
def byte_array_to_np_array(x):
    temp = np.load(io.BytesIO(x),allow_pickle=True)
    return temp

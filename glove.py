__author__ = "Younes Karimi"
__email__ = "younes@psu.edu"
__description__ = "This file contains functions for loading the pretrained GloVe model"

from collections import OrderedDict
import  numpy as np

def load_glove_model(glove_file, dimension):
    """Loads a local GloVe pre-trained model into an ordered dictionary"""
    print("Loading GloVe Model...")
    f = open(glove_file,'r')
    model = OrderedDict()
    for line in f:
        splitLine = line.split()
        if len(splitLine) != dimension+1:
            print('Skipping this word from the model: "%s"' % splitLine[0])
            continue
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    return model
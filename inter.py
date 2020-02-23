import io
import os

# Imports the Google Cloud client library
from datetime import datetime 
import requests


from google.cloud import vision
from google.cloud.vision import types
import matplotlib.pyplot as plt 
import cv2

import torch
from torchtext import data
from torchtext import datasets
import random
import numpy as np

from har import CNN
from har import CNN1d

import torch.nn as nn
import torch.nn.functional as F

import spacy
nlp = spacy.load('en')

SEED = 1234

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True


import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
import matplotlib.pyplot as plt 
import cv2


class SentimentalAnalysis():
    def __init__(self):
        self.TEXT = data.Field(tokenize = 'spacy', batch_first = True)
        self.LABEL = data.LabelField(dtype = torch.float)

        self.train_data, self.test_data = datasets.IMDB.splits(TEXT, LABEL)

        self.train_data, self.valid_data = self.train_data.split(random_state = random.seed(SEED))

        self.MAX_VOCAB_SIZE = 25_000

        self.TEXT.build_vocab(self.train_data, 
                    max_size = MAX_VOCAB_SIZE, 
                    vectors = "glove.6B.100d", 
                    unk_init = torch.Tensor.normal_)

        self.LABEL.build_vocab(self.train_data)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = CNN(25002, 100, 100, [3,4,5], 1, 0.5, 1).to(device)
        # loading our pre trained model
        self.model.load_state_dict(torch.load('tut4-model-udcnn.pt'))
    
    def predict_sentiment(self, sentence, min_len = 5):
        self.model.eval()
        tokenized = [tok.text for tok in nlp.tokenizer(sentence)]
        if len(tokenized) < min_len:
            tokenized += ['<pad>'] * (min_len - len(tokenized))
        indexed = [self.TEXT.vocab.stoi[t] for t in tokenized]
        tensor = torch.LongTensor(indexed).to(device)
        tensor = tensor.unsqueeze(0)
        prediction = torch.sigmoid(self.model(tensor))
        return prediction.item()



from google.cloud import storage
class DataCollection():
    def __init__(self):
        self.n = 0
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="tarunG.json"
        self.client = storage.Client()
        try:
            self.bucket = client.get_bucket('therapyhack')
        except:
            print("some thing is wrong with bucket")
    
    def listand_down_files(self):
        """List all files in GCP bucket."""
        self.n +=1
        files = self.bucket.list_blobs()
        
        
    #     fileList = [file.name for file in files]
        for f in files:
            print(f.name)
            with open(f.name + "/" +f.name+str(self.n)+".csv", "wb") as file_obj:
                f.download_to_file(file_obj)
        return True

    def delete_files(self):
        pass


    def detect_presence(self):
        pass



    class SentimentalAnalysisVisual():
        def __init__(self):

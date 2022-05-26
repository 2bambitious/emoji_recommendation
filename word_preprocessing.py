import re
import pandas as pd
from matplotlib.pyplot import get
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder

class MyTokenizer:
    def __init__(self):
        self.train_path = get_path('archive/train.txt')
        self.test_path = get_path('archive/test.txt')
        self.X_train, _ = pre_processing(self.train_path)
        self.X_test, _ = pre_processing(self.test_path)
        self.tokenizer = Tokenizer()
        self.tokenizer.fit_on_texts(pd.concat([self.X_train, self.X_test], axis = 0))

    def myTokenizer(self):
        return self.tokenizer


class MyLabelEncoder:
    def __init__(self):
        self.encoder = LabelEncoder()

        df = pd.read_csv('archive/train.txt', names=['Text', 'Emotion'], sep=';')
        y = df['Emotion']

        self.encoder.fit(y)

    def myLabelEncoder(self):
        return self.encoder



def get_path(text):
    path =text
    return path

def clean(text):
    text = re.sub(r'[^a-zA-Z ]', '', text)
    text = text.lower()
    return text    


def pre_processing(path):
    df = pd.read_csv(path, names=['Text', 'Emotion'], sep=';')
    X = df['Text'].apply(clean)
    y = df['Emotion']

    temp = MyLabelEncoder()
    labelEncoder = temp.myLabelEncoder()
    y = labelEncoder.transform(y)
    y = to_categorical(y)
    
    return X, y

def pre_for_predict(text):
    temp = MyTokenizer()
    tokenizer = temp.myTokenizer()
    text = clean(text)
    text = tokenizer.texts_to_sequences([text])
    text = pad_sequences(text, maxlen=256, truncating='pre')
    return text



    


    





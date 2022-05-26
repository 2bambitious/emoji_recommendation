import re
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from word_preprocessing import get_path, clean, pre_processing, MyTokenizer
from model import SentimentalClassification

train_path = get_path('archive/train.txt')
test_path = get_path('archive/test.txt')
val_path = get_path('archive/val.txt')



X_train, y_train = pre_processing(train_path)
X_test, y_test = pre_processing(test_path)
X_val, y_val = pre_processing(val_path)

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


#tokenizer = Tokenizer()
#tokenizer.fit_on_texts(pd.concat([X_train, X_test], axis=0))
temp = MyTokenizer()
tokenizer = temp.myTokenizer()

train_seq = tokenizer.texts_to_sequences(X_train)
test_seq = tokenizer.texts_to_sequences(X_test)
val_seq = tokenizer.texts_to_sequences(X_val)

X_train = pad_sequences(train_seq, maxlen=256, truncating='pre')
X_test = pad_sequences(test_seq, maxlen=256, truncating='pre')
X_val = pad_sequences(val_seq, maxlen=256, truncating='pre')

vocabSize = len(tokenizer.index_word) + 1

maxlen = X_train.shape[1]
embedding_size = 200
filters = 128

clf = SentimentalClassification(vocabSize, embedding_size, maxlen, filters=filters, lstm_size=128)
print(clf.model.summary())
clf.compile_model()
with tf.device("/device:GPU:0"):
    fit= clf.model.fit(X_train,
                        y_train,
                        validation_data=(X_val, y_val),
                        verbose=1,
                        batch_size=256,
                        epochs=30,
                        callbacks=[clf.early_stop]
                    )

clf.model.evaluate(X_test, y_test, verbose=1)

#clf.model.save('SentimentalClassification.h5')
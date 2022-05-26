import numpy as np
import tensorflow as tf
import pandas as pd
from word_preprocessing import pre_for_predict, MyLabelEncoder
from emojiPrint import return_image


def predict(text, model):
    temp = MyLabelEncoder()
    encoder = temp.myLabelEncoder()
    text = pre_for_predict(text)
    result = encoder.inverse_transform(np.argmax(model.predict(text), axis=-1))[0]
    return result
    


if __name__ == "__main__":

    model = tf.keras.models.load_model('SentimentalClassification.h5')
    print("When you want to finish, input 'terminate'")
    while(True):
        text = input()
        if (text == "terminate"):
            print("chatting is finished")
            break
        sentiment = predict(text, model)
        return_image(sentiment)


    




import tensorflow

class SentimentalClassification(tensorflow.keras.Model):
    def __init__(self, vocabSize, embedding_size, input_length, kernel_size = 5, filters = 64, pool_size = 4, lstm_size = 70):
        super(SentimentalClassification, self).__init__(name='')
        self.model = tensorflow.keras.models.Sequential(
            [
                tensorflow.keras.layers.Embedding(vocabSize, embedding_size, input_length=input_length),
                tensorflow.keras.layers.Dropout(0.5),
                tensorflow.keras.layers.Conv1D(filters, kernel_size ,padding='valid', activation='relu', strides=1),
                tensorflow.keras.layers.MaxPooling1D(pool_size = pool_size),
                tensorflow.keras.layers.LSTM(lstm_size),
                tensorflow.keras.layers.Dense(6),
                tensorflow.keras.layers.Activation('softmax')
            ]
        )

        self.early_stop = tensorflow.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
    
    def summary(self):
        print(self.model.summary())

    def compile_model(self):
        nadam = tensorflow.keras.optimizers.Nadam()
        self.model.compile(loss='categorical_crossentropy', optimizer=nadam, metrics=['accuracy'])



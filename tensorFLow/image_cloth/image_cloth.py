#from __future__ import absolute_import，division,print_function,unicode_literals

import tensorflow as tf
from tensorflow import keras

import numpy as np
#import maplotlib.pyplot as plt

print(tf.__version__)
class_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
fashion_mnist = keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()

print("train_images numbers:",train_images.shape)

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential(
    [
        keras.layers.Flatten(input_shape=(28,28)),
        keras.layers.Dense(128,activation='relu'),
        keras.layers.Dense(10,activation='softmax')
    ]
)

model.compile(optimizer='adam',
                                loss='sparse_categorical_crossentropy',
                                metrics=['accuracy'])

model.fit(train_images,train_labels,epochs=10)

test_loss,test_acc =  model.evaluate(test_images,test_labels,verbose=2)
print('\nTest accuracy:',test_acc)

predictions = model.predict(test_images)

print('predict first image:',np.argmax(predictions[0]),'the label is ',test_labels[0])






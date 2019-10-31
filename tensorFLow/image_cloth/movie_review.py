import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds

print("version:",tf.__version__)
print('Eager mode:',tf.executing_eagerly())
print('Hub version:',hub.__version__)

train_validation_split = tfds.Split.TRAIN.subsplit([6,4])

(train_data,validation_data),test_data = tfds.load(
    name = 'imdb_reviews',
    split = (train_validation_split,tfds.Split.TEST),
    as_supervised = True
)

train_examples_batch ,train_labels_batch = next(iter(train_data.batch(10)))

embeding = 'https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1'
hub_layer = hub.KerasLayer(embeding,input_shape=[],dtype=tf.string,trainable = True)
hub_layer(train_examples_batch[:3])

model = tf.Keras.Sequential()
model.add(hub_layer)
model.add(tf.Keras.layers.Dense(16,activation='relu'))
model.add(tf.Keras.layers.Dense(1,activation='sigmoid'))

model.summary()

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

history = model.fit(train_data.shuffle(10000).batch(512),
                                        epochs = 20,
                                        validation_data = validation_data.batch(512),
                                        verbose=1)

results = model.evaluate(test_data.batch(512),verbose=2)
for name,value in zip(model.metrics_names,results):
    print("%s:%.3f" %(name,value))



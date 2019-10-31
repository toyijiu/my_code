import tensorflow as tf
import numpy as np
from cnn import *
class MNISTLoader():
    def __init__(self):
        mnist = tf.keras.datasets.mnist

        (self.train_data,self.train_label),(self.test_data,self.test_label) = mnist.load_data()

        self.train_data = np.expand_dims(self.train_data.astype(np.float32)/255.0,axis = -1)
        self.test_data = np.expand_dims(self.test_data.astype(np.float32)/255.0,axis = -1)
        self.train_label = self.train_label.astype(np.int32)
        self.test_label = self.test_label.astype(np.int32)
        self.num_train_data,self.num_test_data = self.train_data.shape[0],self.test_data.shape[0]

    def get_batch(self,batch_size):
        index = np.random.randint(0,np.shape(self.train_data)[0],batch_size)
        return self.train_data[index,:],self.train_label[index]

if __name__ == "__main__":
    num_epochs = 5
    batch_size = 50
    learning_rate = 0.001

    model = CNN()
    data_loader = MNISTLoader()
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

    num_batchs = int(data_loader.num_train_data // batch_size*num_epochs)

    for batch_index in range(num_batchs):
        x,y = data_loader.get_batch(batch_size)

        #求导
        with tf.GradientTape() as tape:
            #获取预测label
            y_pred = model(x)
            #根据预测label和实际label计算loss
            loss = tf.keras.losses.sparse_categorical_crossentropy(y_true = y,y_pred = y_pred)
            loss = tf.reduce_mean(loss)
            print("batch:%s,loss %f" %(batch_index,loss.numpy()))
        
        #根据loss，求导更新model各个参数
        grads = tape.gradient(loss,model.variables)
        optimizer.apply_gradients(grads_and_vars = zip(grads,model.variables))
    
    #评估器评估model在test数据上的性能
    sparse_categorical_accuracy = tf.keras.metrics.SparseCategoricalAccuracy()
    num_batchs = int(data_loader.num_test_data // batch_size)
    for batch_index in range(num_batchs):
        start_index,end_index = batch_size*batch_index,batch_size*(batch_index+1)

        y_pred = model.predict(data_loader.test_data[start_index:end_index])
        sparse_categorical_accuracy.update_state(y_true=data_loader.test_label[start_index:end_index],y_pred=y_pred)
    
    print("test accuracy:%f" %sparse_categorical_accuracy.result())

        

            
    


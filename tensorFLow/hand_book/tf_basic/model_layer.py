import tensorflow as tf

x = tf.constant([[1.,2.,3.],[4.,5.,6.]])
y = tf.constant([[10.],[20.]])

class Linear(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.dense = tf.keras.layers.Dense(     #全连接层
            units = 1,  #输出张量的维度
            activation = None,  #设置激活函数
            kernel_initializer = tf.zeros_initializer(), #权重矩阵变量的初始化器
            bias_initializer = tf.zeros_initializer()   #偏置向量bias的初始化器
        )
    
    def call(self,input):
        output = self.dense(input)  #调用之前定义的全连接层,实现线性变换,d对输入进行线性变换+激活函数
        return output

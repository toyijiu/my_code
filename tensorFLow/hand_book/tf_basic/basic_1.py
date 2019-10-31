import tensorflow as tf

random_float = tf.random.uniform(shape=())
zero_vector = tf.zeros(shape=(2),dtype=tf.int32)

A = tf.constant([[1,2],[3,4]])
B = tf.constant([[5,6],[7,8]])


print(A.shape)
print(A.dtype)
print(A.numpy())
print(zero_vector.dtype)
print(tf.add(A,B))
print(tf.matmul(A,B))

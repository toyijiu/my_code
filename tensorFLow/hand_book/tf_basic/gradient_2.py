import tensorflow as tf

x = tf.constant([[1.,2.],[3.,4.]])
y = tf.constant([[1.],[2.]])
w = tf.Variable(initial_value = [[1.],[2.]])
b = tf.Variable(initial_value = 1.)

with tf.GradientTape() as tape:
    L = 0.5*tf.reduce_sum(tf.square(tf.matmul(x,w)+b-y))
    w_grad,b_grad = tape.gradient(L,[w,b])

    print(L.numpy())
    print(w_grad.numpy())
    print(b_grad.numpy())
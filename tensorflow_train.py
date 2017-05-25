import numpy as np
import tensorflow as tf

#Model Parameters
w=tf.Variable([0.3],tf.float32)
b=tf.Variable([-0.3],tf.float32)

#Model input
X=tf.placeholder(tf.float32)
y=tf.placeholder(tf.float32)


linear_model=w*X+b
#training data
x_train=[1,2,3,4,5]
y_train=[0,-1,-2,-3,-4]
#loss
loss=tf.reduce_sum(tf.square(y-linear_model))

#optimizer
optimizer=tf.train.GradientDescentOptimizer(0.01)
train=optimizer.minimize(loss)

#training loop
init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)

for i in range(1000):
    sess.run(train,{X:x_train,y:y_train})
    curr_W,curr_b,curr_loss=sess.run([w,b,loss],{X:x_train,y:y_train})
    print("W:%s   b:%s   loss:%s"%(curr_W,curr_b,curr_loss))


curr_W,curr_b,curr_loss=sess.run([w,b,loss],{X:x_train,y:y_train})
print("W:%s   b:%s   loss:%s"%(curr_W,curr_b,curr_loss))

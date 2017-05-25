import tensorflow as tf
w=tf.Variable([0.3],tf.float32)
b=tf.Variable([-0.3],tf.float32)

x=tf.placeholder(tf.float32)
y=tf.placeholder(tf.float32)
linear_model=w*x+b
squared_delta=tf.square(linear_model-y)
loss=tf.reduce_sum(squared_delta)
init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)
#initialize all the varibales


print(sess.run(loss,{x:[1,2,3,4,5],y:[0,-1,-2,-3,-4]})) #calulate the linear_model with x provided

fixw=tf.assign(w,[-1.0])
fixb=tf.assign(b,[1.0])
sess.run([fixw,fixb])

print(sess.run(loss,{x:[1,2,3,4,5],y:[0,-1,-2,-3,-4]}))

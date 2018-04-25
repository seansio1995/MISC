import tensorflow as tf
a=tf.placeholder(tf.float32)
b=tf.placeholder(tf.float32)
adder=tf.add(a,b)

adder_triple=tf.multiply(adder,3)
sess=tf.Session()
print(sess.run(adder,{a:1,b:2}))
print(sess.run(adder,{a:10,b:12}))
print(sess.run(adder_triple,{a:10,b:12}))

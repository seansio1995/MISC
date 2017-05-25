
import tensorflow as tf

node1=tf.constant(3,tf.float32)
node2=tf.constant(4,tf.float32)
# print(node1,node2)

sess=tf.Session()
# print(sess.run([node1,node2]))

#export TF_CPP_MIN_LOG_LEVEL=2 if producce warnings.
node3=tf.add(node1,node2)
print(sess.run(node3))

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
sess = tf.InteractiveSession()

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

x = tf.placeholder(tf.float32, shape=[None, 784])
y_ = tf.placeholder(tf.float32, shape=[None, 10])


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)
def bias_variable(shape):
    initial = tf.constant(0.1,shape=shape)
    return tf.Variable(initial)
    
def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

#initiate these convol;utional networks
#first two digits are the area of the patch
#next digit is number of input channels
#last digit is output channels
W_conv1 = weight_variable([5,5,1,32])
#the bias is a column vector of 32 since the first layer has 32 outputs
b_conv1 = bias_variable([32])

#flattens the 784 column vector into a 28X28 matrix with 1 color channel
x_image = tf.reshape(x, [-1,28,28,1])

#creates a network based on the input (x_image) and the weight patch 5x5, 1 in 32 out
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
#reduces the image to a 14x14 matrix
h_pool1 = max_pool_2x2(h_conv1)

#creating the second convolutional layer
#5x5 patch with 32 input channels and 64 output channles
W_conv2 = weight_variable([5, 5, 32, 64])
#64 biases for the 64 outputs of the patch, corresponds to 64 features
b_conv2 = bias_variable([64])

#create the layer based on the patch and the biases using the first layer as the input
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
#reduce the image size again to a 7x7
h_pool2 = max_pool_2x2(h_conv2)

#create a fully connected layer where each pixel of the reduced image is connected to the output of the second layer
#have 1024 outputs
W_fc1 = weight_variable([7 * 7 * 64, 1024])
#biases for those outputs
b_fc1 = bias_variable([1024])

#flatten the thing
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
#create a final rectified layer
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

#create the output layer
y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

#run all of the data through the network in steps
cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
sess.run(tf.global_variables_initializer())
for i in range(20000):
  batch = mnist.train.next_batch(50)
  if i%100 == 0:
    train_accuracy = accuracy.eval(feed_dict={
        x:batch[0], y_: batch[1], keep_prob: 1.0})
    print("step %d, training accuracy %g"%(i, train_accuracy))
  train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

print("test accuracy %g"%accuracy.eval(feed_dict={
    x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))



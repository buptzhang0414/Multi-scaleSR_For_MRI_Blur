import sys
import numpy as np
import tensorflow as tf
import tensorflow.contrib.slim as slim

if sys.version_info.major == 3:
    xrange = range


def im2uint8(x):
    if x.__class__ == tf.Tensor:
        return tf.cast(tf.clip_by_value(x, 0.0, 1.0) * 255.0, tf.uint8)
    else:
        t = np.clip(x, 0.0, 1.0) * 255.0
        return t.astype(np.uint8)


# def ResnetBlock(x, dim, ksize, scope='rb'):
#     with tf.variable_scope(scope):
#         net = slim.conv2d(x, dim, [ksize, ksize], scope='conv1')
#         net = slim.conv2d(net, dim, [ksize, ksize], activation_fn=None, scope='conv2')
#         return net + x



# def ResnetBlock(x, dim, ksize, scope='rb'):
#     with tf.variable_scope(scope):
#         # net = slim.conv2d(x, dim, [ksize, ksize], scope='conv1')
#         # net = slim.conv2d(net, dim, [ksize, ksize], activation_fn=None, scope='conv2')
#         x1 = slim.conv2d(x, dim, [ksize, ksize], scope='conv1')
#         x2 = slim.conv2d(x1, dim, [ksize, ksize],activation_fn = tf.nn.relu, scope='conv2')
#         x2 = slim.conv2d(x2, dim, [ksize, ksize], scope='conv3')
#         x3 = x1+x2
#         x3 = tf.nn.relu(x3)
#         x4 = slim.conv2d(x3, dim, [ksize, ksize],activation_fn = tf.nn.relu, scope='conv4')
#         x4 = slim.conv2d(x4, dim, [ksize, ksize], scope='conv5')
#         x5 = x3+x4
#         x6 = slim.conv2d(x5, dim, [ksize, ksize], scope='conv6')
#         return x6 + x


def ResnetBlock(x, dim, ksize, scope='rb'):
    with tf.variable_scope(scope):
        # net = slim.conv2d(x, dim, [ksize, ksize], scope='conv1')
        # net = slim.conv2d(net, dim, [ksize, ksize], activation_fn=None, scope='conv2')
        x1 = slim.conv2d(x, dim, [ksize, ksize], scope='conv1')
        x2 = slim.conv2d(x1, dim, [ksize, ksize],activation_fn = tf.nn.relu, scope='conv2')
        x2 = slim.conv2d(x2, dim, [ksize, ksize], scope='conv3')
        x3 = x1+x2
        x3 = tf.nn.relu(x3)
        x4 = slim.conv2d(x3, dim, [ksize, ksize],activation_fn = tf.nn.relu, scope='conv4')
        x4 = slim.conv2d(x4, dim, [ksize, ksize], scope='conv5')
        x5 = x3+x4
        x6 = slim.conv2d(x5, dim, [ksize, ksize], scope='conv6')
        return x6 + x


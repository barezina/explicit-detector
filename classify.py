import os
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

from nudenet import NudeClassifier
classifier = NudeClassifier()

print('')
print('')
print('TEST RESULT')
print('********************************************')
print('')

print(classifier.classify('/nsfw/one.jpg'))

print('')
print('********************************************')
print('')

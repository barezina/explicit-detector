import os
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

from nudenet import NudeClassifier
classifier = NudeClassifier()

result = classifier.classify('/nsfw/one.jpg')
result2 = classifier.classify('/nsfw/two.xjpg')

print('')
print('')
print('TEST RESULTS:')
print('********************************************')
print('')

print('one.jpg')
print(result)
print('')
print('two.xjpg')
print(result2)

print('')
print('********************************************')
print('')

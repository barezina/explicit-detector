import os
import json
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

from nudenet import NudeDetector
detector = NudeDetector()

# Performing detection
result = detector.detect('/nsfw/one.jpg')
result2 = detector.detect('/nsfw/two.xjpg')

print('')
print('')
print('TEST RESULTS:')
print('********************************************')
print('')

print('one.jpg')
print(result)
print('')
print('two.jpg')
print(result2)

print('')
print('********************************************')
print('')

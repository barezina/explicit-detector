from nudenet import NudeClassifier
classifier = NudeClassifier()
print(classifier.classify('/nsfw/one.jpg'))
print(classifier.classify('/nsfw/two.jpg'))

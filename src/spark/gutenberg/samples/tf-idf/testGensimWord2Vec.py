# -*- coding: utf-8 -*-
 
 
from gensim.models import word2vec
import logging

import os
import gensim
class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

sentences = MySentences('/ezroot/download/books2') # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences,workers=4)

sim1 = model.wv.similarity(u"Lord",u"God")
print(sim1)

for i in model.wv.most_similar(u"Lord"):
    print(i[0],i[1])


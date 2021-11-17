from gensim.models import Word2Vec
import os

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

sentences = MySentences('/ezroot/download/books2') 
train_model = Word2Vec(sentences, window=5, min_count=1, workers=4)
train_model.save('./MyModel')

train_model.wv.save_word2vec_format('./mymodel.txt', binary=False)

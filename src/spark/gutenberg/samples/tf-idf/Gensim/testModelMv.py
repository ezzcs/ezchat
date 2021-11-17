#coding:utf-8
import gensim
from gensim.models import KeyedVectors

word2vec_model_path = './mymodel.txt' ##词向量文件的位置
word2vec_model = KeyedVectors.load_word2vec_format(word2vec_model_path, binary=False,unicode_errors='ignore')
word2vec_dict = {}
ezkeys = word2vec_model.key_to_index
ezkeyList = ezkeys.keys()
for key in ezkeyList:
    print(key)


print('lord similarity with father')
ezsimi = word2vec_model.similarity('lord','father')
print(ezsimi)


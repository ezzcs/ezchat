#coding:utf-8
import gensim
from gensim.models import KeyedVectors

word2vec_model_path = './mymodel.txt' ##词向量文件的位置
word2vec_model = KeyedVectors.load_word2vec_format(word2vec_model_path, binary=False,unicode_errors='ignore')
word2vec_dict = {}
for vector in word2vec_model.get_normed_vectors():
    print(vector)


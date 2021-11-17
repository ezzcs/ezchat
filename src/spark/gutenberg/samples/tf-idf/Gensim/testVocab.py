from gensim.models import Word2Vec
model = Word2Vec.load('./MyModel')
# 对于训练好的模型，我们可以通过下面这前三行代码来查看词表中的词，频度，以及索引位置， 
# 最关键的是可以通过第四行代码判断模型中是否存在这个词
for key in model.wv.key_to_index:
    print(key)

v1 = model.wv.get_vector(u"Lord")
print(v1)


print("Similar[Lord]")
v2 = model.wv.most_similar(u"Lord")
print(v2)


print("Similar[Sin]")
v3 = model.wv.most_similar(u"Sin")
print(v3)

print("Similar[Light]")
v4 = model.wv.most_similar(u"Light")
print(v4)

print("Similar[Israel]")
v5 = model.wv.most_similar(u"Israel")
print(v5)

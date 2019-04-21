from snownlp import SnowNLP

s = SnowNLP(u'垃圾玩意')

s.words # [u'这个', u'东西', u'真心',
# u'很', u'赞']

s.tags # [(u'这个', u'r'), (u'东西', u'n'),
# (u'真心', u'd'), (u'很', u'd'),
# (u'赞', u'Vg')]

print(s.sentiments)

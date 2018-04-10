# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import MySQLdb

db=MySQLdb.connect("localhost","root","root","porn",charset='utf8')
select_sql="SELECT title FROM pornlist"
cursor=db.cursor()
cursor.execute(select_sql)
l=[date[0] for date in cursor.fetchall()]
cursor.close()
db.close()
text= "  ".join(l)
wordlist_after_jieba=jieba.cut(text,cut_all=False)
wl_space_split="  ".join(wordlist_after_jieba)
#backgroup-Image=plt.imread('bg.png')
wc=WordCloud(background_color='black',
             width=1000,
             height=800,
             max_words=100,
             max_font_size=400,
             random_state=30,
             )
wc.generate(wl_space_split)
plt.imshow(wc)
plt.axis("off")
plt.show()


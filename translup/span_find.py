
import json

from nltk import word_tokenize
from fuzzywuzzy import fuzz

count = 0

# par = open('parae','a')
# qu = open('quese','a')
# an = open('anse','a')
# sp = open('span_upd','a')
fh = open('sample1','a')

al_count = 0

with open('real_span_tel.txt') as pre,open('real_ans_tel.txt') as pa,open('real_con_tel.txt') as pr:
	pl = pre.readlines()
	an = pa.readlines()
	cn = pr.readlines()


	for c in range(len(cn)):
		# if an[c].lower().strip() not in cn[c].lower():
		# 	print(an[c],c)
		# 	count+=1

		sp,ep = pl[c].strip().split('\t')
		cn_tokens = ' '.join(word_tokenize(cn[c])[int(sp):int(ep)+1])
		if cn_tokens == (an[c].strip()):
			count+=1
		elif fuzz.ratio(cn_tokens,an[c].lower().strip()) >0.98: ##comment ths condition too..
			al_count+=1
		else:
			for i,word in enumerate(word_tokenize(cn[c])):
				fh.write(str(i)+str(word)+'\t') 
			fh.write(str(cn_tokens)+'//'+str(an[c].strip())+'//'+str(sp)+'/'+str(ep)+str(c)+'\n')
			# print(p)
			# pass
print(count,al_count,count+al_count)
	
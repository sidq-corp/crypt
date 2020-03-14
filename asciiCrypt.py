import hashlib
from random import randint
def to_ord(string):
	char = list(string)
	ord_a = []
	for i in range(len(char)):
		ord_a.append(ord(char[i]))
	return ord_a

def to_chr(num):
	chr_a = ''
	for i in range(len(num)):
		chr_a = chr_a + chr(int(num[i]))
	return chr_a

def crypt(string, key):
	key = str(hashlib.md5(str(key).encode()).hexdigest())
	string = to_ord(string)
	key = to_ord(key)
	key_l = len(key)
	string_l = len(string)
	q = 0
	sum_s = []
	for i in range(string_l):
		s = string[i] + key[q]
		
		sum_s.append(chr(int(s/2)))
		sum_s.append(str(s%2))
		q += 1
		if q >= key_l:
			q = 0
	return ''.join(sum_s)

def de_crypt(string, key):
	key = str(hashlib.md5(str(key).encode()).hexdigest())
	key_l = len(key)
	string_l = len(string)
	n = []
	q = 0
	for i in range(0,string_l,2):
		des = ord(string[i])*2 + int(string[i+1]) - ord(key[q]) 
		n.append(randint(34,120) if des < 32 else randint(33,120) if des > 126 else des)
		q += 1
		if q >= key_l:
				q = 0
	st = to_chr(n)
	return st



if __name__ == '__main__':
	print('********DEBUG********')
	key = input('key = ')
	key2 = input('key = ')
	string = input('string = ')
	print('********OUTPUT*******')
	a = crypt(string, key)
	print('crypy string =',a)
	print('decrypt string =',de_crypt(a,key2))
	print('*********************')


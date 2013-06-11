#-*-coding:utf-8-*-

from tanimoto import tanimoto

def test_tanimoto():
	a= ['shirt','shoes','pants','socks']
	b = ['shirt','skirt','shoes']
	print tanimoto(a, b)

if __name__ == '__main__':  
	test_tanimoto()

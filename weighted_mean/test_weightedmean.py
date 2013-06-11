#-*-coding:utf-8-*-
#-*-coding:utf-8-*-
from weightedmean import weightedmean


def test_weightedmean():
	x = [2, 1]
	w = [1.0, 1.0]  #小数，不然会保留整数
	print weightedmean(x,w)


if __name__ == '__main__':  
	test_weightedmean()


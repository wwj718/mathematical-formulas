#-*-coding:utf-8-*-

def euclidean(p,q):
	'''
	   欧几里得距离
	   多维空间中两点的距离(直线距离)
	   可用于判断事项两两间的相似程度
	   对于(p1,p2),(q1,q2)   距离为((p1-q1)**2+(p2-q2)**2)**0.5
	'''
	sumSq = 0.0 
	
	#将差值的平方累加起来
	for i in range(len(p)):
		sumSq = sumSq + (p[i]-q[i])**2
		
	#求平方根
	return (sumSq**0.5)
	
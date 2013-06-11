#-*-coding:utf-8-*-

def weightedmean(x, w):
    '''
    加权平均
    观测变量（x1.x2）,权重(w1,w2)
    则：((x1*w1)+(x2+w2))/(w1+w2)
    '''
    num = sum([x[i]*w[i] for i in range(len(w))])
    den = sum(w[i] for i in range(len(w)))
    return num/den
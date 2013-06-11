#-*-coding:utf-8-*-

def tanimoto(a,b):
    '''
    用于度量两个集合之间的相似程度
    交集部分c  
    Na(a中元素个数)  Nb(b中元素个数) 
    则 T = Nc/(Na+Nb-Nc)
    '''
    c = [v for v in a if v in b]
    #参与除法的两个数中有以一个数为浮点数,否则答案为0
    return float( float(len(c))/(len(a)+len(b)-len(c) ))  
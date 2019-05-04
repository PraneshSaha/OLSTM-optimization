import numpy as np
def F1(x):
    X=np.asarray(x)
    f=np.sum(np.multiply(X,X))
    return f
# dimension 30 [-100,100] 0
def F2(x):
    X=np.asarray(x)
    f1=np.sum(np.abs(X))
    f2=1
    for i in range(len(x)):
        f2=f2*abs(x[i])
    f=f1+f2
    return f
#dimn 30 [-10,10] 0
def F3(x):
    X=np.asarray(x)
    s=0
    for i in range(len(x)):
        s=s+np.sum(X[:i+1])**2
    return s
#dimn 30 [-100,100] 0
def F4(x):
    X=np.asarray(x)
    f=np.max(np.abs(X))
    return f
#dim 30 [-100,100] 0
def F5(x):
    X=np.asarray(x)
    s=0
    for i in range(len(x)-1):
        s=s+100*(X[i+1]-X[i]**2)**2+(X[i]-1)**2
    return s
#dim 30 [-30,30] 0
def F6(x):
    X=np.asarray(x)
    X=np.abs(X+.5)
    M=np.multiply(X,X)
    f=np.sum(M)
    return f
#dim 30 [-100,100] 0
def F7(x):
    X=np.asarray(x)
    i=np.asarray(range(1,len(x)+1))
    M1=np.multiply(X,X)
    M2=np.multiply(M1,M1)
    M3=np.multiply(M2,i)
    f=np.sum(M3)+np.random.uniform(0,1)
    return f
#dim 30 [-1.28,1.28] 0    
def F8(x):
    X=np.asarray(x)
    i=np.asarray(range(1,len(x)+1))
    M1=np.multiply(X,X)
    f=np.sum(np.multiply(i,M1))
    return f
#dim 30 [10,10] 0
def F9(x):
    f=(1.5-x[0]+x[0]*x[1])**2+(2.25-x[0]+x[0]*x[1]**2)**2+(2.625-x[0]+x[0]*x[1]**3)**2
    return f
#dim 2 [-4.5,4.5] 0
def F10(x):
    f=-np.cos(x[0])*np.cos(x[1])*np.exp(-(x[0]-3.14)**2-(x[1]-3.14)**2)
    return f
#dim 2 [-100,100] -1
def F11(x):
    f=0.26*(x[0]*x[0]+x[1]*x[1])-.48*x[0]*x[1]
    return f
#dim 2 [-10,10] 0
def F12(x):
    f=100*(x[0]*x[0]-x[1])**2+(x[0]-1)**2+(x[2]-1)**2+90*(x[2]*x[2]-x[3])**2+10.1*((x[1]-1)**2+(x[3]-1)**2)+19.8*(x[1]-1)*(x[3]-1)
    return f
#dim 4 [-10,10] 0
def F13(x):
    X=np.asarray(x)
    M1=(X-1)**2
    X2=X[:len(x)-1]
    X3=X[1:]
    M2=np.multiply(X2,X3)
    f=np.sum(M1)-np.sum(M2)
    return f
#dim 10 [-100,100] -210
def F14(x):
    X=np.asarray(x)
    M1=np.sum(X**2)
    i=np.asarray(range(1,len(x)+1))
    M2=np.sum(np.multiply(i,X)*.5)
    f=M1+M2**2+M2**4
    return f
#dim 10 [-5,10] 0
def F15(x):
    X=np.asarray(x)
    X1=X[1:]**2
    X2=X[:len(x)-1]
    i=np.asarray(range(2,len(x)+1))
    f=(X[0]-1)**2+np.sum(np.multiply(i,(2*X1-X2)**2))
    return f
#dim 30 [-10,10] 0
a1=[-32,-16,0,16,32]*5
a2=[-32,-32,-32,-32,-32,-16,-16,-16,-16,-16,0,0,0,0,0,16,16,16,16,16,32,32,32,32,32]
a=np.array([a1,a2])
def F16(x):
    i=np.asarray(range(1,26))
    s=0
    for j in range(25):
        s1=i[j]+(x[0]-a[0,j])**6+(x[1]-a[1,j])**6
        s=s+(1/s1)
    f=1/((1/500)+s)
    return f
#dim 2 [-65.536,65.536] .998

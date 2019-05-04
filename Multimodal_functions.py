def F17(x):
    X=np.asarray(x)
    S=-np.multiply(X,np.sin(np.sqrt(np.abs(X))))
    f=np.sum(S)
    return f
#dimn 30 [-500,500] -419.9829*30
def F18(x):
    X=np.asarray(x)
    M1=np.multiply(X,X)
    M2=-10*np.cos(2*3.14*X)+10
    f=np.sum(M1+M2)
    return f
#dimn 30,200 [-5.12,5.12] 0
def F19(x):
    X=np.asarray(x)
    M1=np.sum(np.multiply(X,X))/len(x)
    M2=np.sum(np.cos(2*3.14*X))/len(x)
    f=-20*np.exp(-.2*np.sqrt(M1))-np.exp(M2)+20+np.exp(1)
    return f
#dimn 30,200 [-32,32] 0
def F20(x):
    X=np.asarray(x)
    M1=np.sum(np.multiply(X,X))/4000
    M2=1
    for i in range(len(x)):
        M2=M2*np.cos(X[i]/np.sqrt(i+1))
    f=M1-M2+1
    return f
#dimn 30,200 [-600,600] 0
def u(x,a,k,m):
    s=0
    for i in x:
        if i>a:
            s=s+k*((i-a)**m)
        elif -a<i and i<a:
            s=s+0
        elif i<-a:
            s=s+k*((-i-a)**m)
    return s
def F21(x):
    X=np.asarray(x)
    y=1+((X+1)/4)
    us=u(x,10,100,4)
    M1=0
    for i in range(len(x)-1):
        M1=M1+((y[i]-1)**2)*(1+10*(np.sin(3.14*y[i+1])**2))
    f=(3.14*(10*np.sin(3.14*y[0])**2+M1+(y[len(x)-1]-1)**2)/len(x))+us
    return f
#dimn 30,200 [-50,50] 0
def F22(x):
    X=np.asarray(x)
    us=u(x,5,100,4)
    M1=np.multiply(X-1,X-1)
    M2=np.sin(3*3.14*X+1)
    M3=1+np.multiply(M2,M2)
    s1=np.sum(np.multiply(M1,M3))
    f=.1*(np.sin(3*3.14*X[0])**2+s1+((X[len(x)-1]-1)**2)*(1+np.sin(2*3.14*X[len(x)-1])**2))+us
    return f
#dimn 30,200 [-50,50] 0

def F23(x):
    f=(x[1]-(5.1/(4*3.14*3.14))*x[0]*x[0]+(5/3.14)*x[0]-6)**2+10*(1-(1/(8*3.14)))*np.cos(x[0])+10
    return f
#dim 2 [-5,10] [0,15] .398
def F24(x):
    f=x[0]**2+2*x[1]**2-0.3*np.cos(3*3.14*x[0])-0.4*np.cos(4*3.14*x[1])+0.7
    return f
#dim 2 [-100,100] 0
def F25(x):
    f=(x[0]-2*x[1]-7)**2+(2*x[0]+x[1]-5)**2
    return f
#dim 2 [-10,10] 0
def F26(x):
    i=np.asarray(range(1,len(x)+1))
    X=np.asarray(x)
    f=-np.sum(np.sin(X[0])*np.sin(np.multiply(i,X**2)/3.14)**20)
    return f
#dim D [0,3.14] 5 -4.687 2 -1.8013
def F27(x):
    f=x[0]**2+2*x[1]**2-0.3*np.cos(3*3.14*x[0])*np.cos(4*3.14*x[1])+0.3
    return f
#dim 2 [-100,100] 0
def F28(x):
    f=x[0]**2+2*x[1]**2-0.3*np.cos(3*3.14*x[0]+4*3.14*x[1])+.3
    return f
#dim 2 [-100,100] 0
def F29(x):
    f=(1+((x[0]+x[1]+1)**2)*(19-14*x[0]+3*x[0]**2-14*x[1]+6*x[0]*x[1]+3*x[1]*x[1]))*(30+((2*x[0]-3*x[1])**2)*(18-32*x[0]+12*x[0]*x[0]+48*x[1]-36*x[0]*x[1]+27*x[1]*x[1]))
    return f
#dim 2 [-2,2] 3
def F30(x):
    s=0
    X=np.asarray(x)
    d=len(x)
    for i in range(1,d+1):
        p=0
        for j in range(1,d+1):
            p=p+(j**i+0.5)*((X[j-1]/j)**i-1)
        s=s+p**2
    return s
#dim d [-d,d] 0

    

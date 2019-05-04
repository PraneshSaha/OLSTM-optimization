def Sphere(x):
    X=np.asarray(x)
    f=np.sum(np.multiply(X,X))
    return f
def Ackeley(x):
    d=len(x)
    c=2*3.14
    b=.2
    a=20
    X=np.asarray(x)
    X2=b*np.sqrt(np.sum(np.multiply(X,X))/d)
    cscx=np.sum(np.cos(c*X))/d
    f=-a*np.exp(-X2)-np.exp(cscx)+a+np.exp(1)
    #print(f)
    return f
def Rastrigin(x):
    d=len(x)
    X=np.asarray(x)
    X2=np.sum(np.multiply(X,X)-10*np.cos(2*np.pi*X))
    f=X2+10*d
    return f
def Griewank(x):
    X=np.asarray(x)
    M1=np.sum(np.multiply(X,X))/4000
    M2=1
    for i in range(len(x)):
        M2=M2*np.cos(X[i]/np.sqrt(i+1))
    f=M1-M2+1
    return f
def Weierstrass(x):
    X=np.asarray(x)
    a=.5
    b=3
    Kmax=20
    d=len(x)
    ak=np.ones((Kmax+1,1))*a
    bk=np.ones((Kmax+1,1))*b
    for i in range(Kmax+1):
        ak[i]=ak[i]**i
        bk[i]=bk[i]**i
    s1=0
    for i in range(d):
        M1=np.sum(np.multiply(ak,np.cos(2*3.14*bk*(X[i]+0.5))))
        s1=s1+M1
    f=s1-d*np.sum(np.multiply(ak,np.cos(2*3.14*bk*0.5)))
    return f


def F31(x):
    opt=np.ones((10,len(x)))
    opt[0,0]=0
    opt[1,1]=0
    opt[2,2]=0
    opt[3,3]=0
    opt[4,4]=0
    opt[5,5]=0
    opt[6,6]=0
    opt[7,7]=0
    opt[8,8]=0
    opt[9,:]=0
    bias=np.array([0,100,200,300,400,500,600,700,800,900])
    X=np.asarray(x)
    lam=[5/100]*10
    sig=[1]*10
    d=len(x)
    f=0
    w_all=np.ones((1,10))
    fe=np.ones((1,10))
    for i in range(10):
        Xo=X-opt[i,:]
        w=np.exp(-np.sum(np.multiply(Xo,Xo))/(2*d*sig[i]**2))
        Xl=Xo/lam[i]
        fe[:,i]=2000*Sphere(Xl)/300000
        #print(fe[:,i])
        w_all[:,i]=w
    w_mx=np.max(w_all)
    for i in range(10):
        if w_all[:,i]!=w_mx:
            w_all[:,i]=w_all[:,i]*(1-(w_mx**10))
    
    w_all=w_all/np.sum(w_all) 
    f=np.sum(np.multiply(w_all,(fe+bias)))
    #print(w_all,fe.shape,bias.shape,(fe+bias).shape)
    return f
#30 [-5,5] 0
def F32(x):
    opt=np.ones((10,len(x)))
    opt[0,0]=0
    opt[1,1]=0
    opt[2,2]=0
    opt[3,3]=0
    opt[4,4]=0
    opt[5,5]=0
    opt[6,6]=0
    opt[7,7]=0
    opt[8,8]=0
    opt[9,:]=0
    bias=np.array([0,100,200,300,400,500,600,700,800,900])
    X=np.asarray(x)
    lam=[5/100]*10
    sig=[1]*10
    d=len(x)
    f=0
    w_all=np.ones((1,10))
    fe=np.ones((1,10))
    for i in range(10):
        Xo=X-opt[i,:]
        w=np.exp(-np.sum(np.multiply(Xo,Xo))/(2*d*sig[i]**2))
        Xl=Xo/lam[i]
        fe[:,i]=Griewank(Xl)
        w_all[:,i]=w
    w_mx=np.max(w_all)
    for i in range(10):
        if w_all[:,i]!=w_mx:
            w_all[:,i]=w_all[:,i]*(1-(w_mx**10))
    
    w_all=w_all/np.sum(w_all) 
    f=np.sum(np.multiply(w_all,(fe+bias)))
    return f
#30 [-5,5] 0
def F33(x):
    opt=np.ones((10,len(x)))
    opt[0,0]=0
    opt[1,1]=0
    opt[2,2]=0
    opt[3,3]=0
    opt[4,4]=0
    opt[5,5]=0
    opt[6,6]=0
    opt[7,7]=0
    opt[8,8]=0
    opt[9,:]=0
    bias=np.array([0,100,200,300,400,500,600,700,800,900])
    X=np.asarray(x)
    lam=[1]*10
    sig=[1]*10
    d=len(x)
    f=0
    w_all=np.ones((1,10))
    fe=np.ones((1,10))
    for i in range(10):
        Xo=X-opt[i,:]
        w=np.exp(-np.sum(np.multiply(Xo,Xo))/(2*d*sig[i]**2))
        Xl=Xo/lam[i]
        fe[:,i]=Griewank(Xl)
        w_all[:,i]=w
    w_mx=np.max(w_all)
    for i in range(10):
        if w_all[:,i]!=w_mx:
            w_all[:,i]=w_all[:,i]*(1-(w_mx**10))
    
    w_all=w_all/np.sum(w_all) 
    f=np.sum(np.multiply(w_all,(fe+bias)))
    return f
def F34(x):
    opt=np.ones((10,len(x)))
    opt[0,0]=0
    opt[1,1]=0
    opt[2,2]=0
    opt[3,3]=0
    opt[4,4]=0
    opt[5,5]=0
    opt[6,6]=0
    opt[7,7]=0
    opt[8,8]=0
    opt[9,9]=0
    bias=np.array([0,100,200,300,400,500,600,700,800,900])
    X=np.asarray(x)
    
    lam=[5/32,5/32,1,1,5/0.5,5/.5,5/100,5/100,5/100,5/100]
    sig=[1]*10
    f_mx=[19.980841134,250.0,39.194601061455685,25.99867632,100000.0]

    d=len(x)
    f=0

    w_all=np.ones((1,10))
    fe=np.ones((1,10))
    for i in range(10):
        Xo=X-opt[i,:]
        w=np.exp(-np.sum(np.multiply(Xo,Xo))/(2*d*sig[i]**2))
        Xl=Xo/lam[i]
        
        if i==0 or i==1:
            fe[:,i]=2000*Ackeley(Xl)/f_mx[0]
        elif i==3 or i==2:  
            fe[:,i]=2000*Rastrigin(Xl)/f_mx[1]
        elif i==4 or i==5:
            fe[:,i]=2000*Weierstrass(Xl)/f_mx[2]
        elif i==6 or i==7:
            fe[:,i]=2000*Griewank(Xl)/f_mx[3]
        elif i==8 or i==9:
            fe[:,i]=2000*Sphere(Xl)/f_mx[4]
        w_all[:,i]=w
    w_mx=np.max(w_all)
    for i in range(10):
        if w_all[:,i]!=w_mx:
            w_all[:,i]=w_all[:,i]*(1-(w_mx**10))
    
    w_all=w_all/np.sum(w_all) 
    f=np.sum(np.multiply(w_all,(fe+bias)))
    return f
def F35(x):
    opt=np.ones((10,len(x)))
    opt[0,0]=0
    opt[1,1]=0
    opt[2,2]=0
    opt[3,3]=0
    opt[4,4]=0
    opt[5,5]=0
    opt[6,6]=0
    opt[7,7]=0
    opt[8,8]=0
    opt[9,:]=0
    bias=np.array([0,100,200,300,400,500,600,700,800,900])
    X=np.asarray(x)
    
    lam=[1/5,1/5,5/.5,5/.5,5/100,5/100,5/32,5/32,5/100,5/100]
    sig=[1]*10
    f_mx=[19.980841134,6250.0,39.194601061455685,25.99867632,100000.0]

    d=len(x)
    f=0

    w_all=np.ones((1,10))
    fe=np.ones((1,10))
    for i in range(10):
        Xo=X-opt[i,:]
        w=np.exp(-np.sum(np.multiply(Xo,Xo))/(2*d*sig[i]**2))
        Xl=Xo/lam[i]
        
        if i==6 or i==7:
            fe[:,i]=2000*Ackeley(Xl)/f_mx[0]
        elif i==0 or i==1:  
            fe[:,i]=2000*Rastrigin(Xl)/f_mx[1]
        elif i==2 or i==3:
            fe[:,i]=2000*Weierstrass(Xl)/f_mx[2]
        elif i==4 or i==5:
            fe[:,i]=2000*Griewank(Xl)/f_mx[3]
        elif i==8 or i==9:
            fe[:,i]=2000*Sphere(Xl)/f_mx[4]
        w_all[:,i]=w
    w_mx=np.max(w_all)
    for i in range(10):
        if w_all[:,i]!=w_mx:
            w_all[:,i]=w_all[:,i]*(1-(w_mx**10))
    
    w_all=w_all/np.sum(w_all) 
    f=np.sum(np.multiply(w_all,(fe+bias)))
    return f

def F36(x):
    opt=np.ones((10,len(x)))
    opt[0,0]=0
    opt[1,1]=0
    opt[2,2]=0
    opt[3,3]=0
    opt[4,4]=0
    opt[5,5]=0
    opt[6,6]=0
    opt[7,7]=0
    opt[8,8]=0
    opt[9,:]=0
    bias=np.array([0,100,200,300,400,500,600,700,800,900])
    X=np.asarray(x)
    
    lam=[.1*1/5,.2*1/5,.3*5/.5,.4*5/.5,.5*5/100,.6*5/100,.7*5/32,.8*5/32,.9*5/100,5/100]
    sig=[.1,.2,.3,.4,.5,.6,.7,.8,.9,1]
    f_mx=[625000.0,156250.0,15.516042233254296,19.91442441634296,100.99952124,70.44456496,22.019600795068175,20.015235996099676,123456.79012345678,100000.0]

    d=len(x)
    f=0

    w_all=np.ones((1,10))
    fe=np.ones((1,10))
    for i in range(10):
        Xo=X-opt[i,:]
        w=np.exp(-np.sum(np.multiply(Xo,Xo))/(2*d*sig[i]**2))
        Xl=Xo/lam[i]
        
        if i==6 or i==7:
            fe[:,i]=2000*Ackeley(Xl)/f_mx[i]
        elif i==0 or i==1:  
            fe[:,i]=2000*Rastrigin(Xl)/f_mx[i]
        elif i==2 or i==3:
            fe[:,i]=2000*Weierstrass(Xl)/f_mx[i]
        elif i==4 or i==5:
            fe[:,i]=2000*Griewank(Xl)/f_mx[i]
        elif i==8 or i==9:
            fe[:,i]=2000*Sphere(Xl)/f_mx[i]
        w_all[:,i]=w
    w_mx=np.max(w_all)
    for i in range(10):
        if w_all[:,i]!=w_mx:
            w_all[:,i]=w_all[:,i]*(1-(w_mx**10))
    
    w_all=w_all/np.sum(w_all) 
    f=np.sum(np.multiply(w_all,(fe+bias)))
    return f
#30 [-5,5] 0

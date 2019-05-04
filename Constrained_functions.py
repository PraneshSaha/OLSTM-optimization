def multi(X):
    x=np.asarray(X)
    f= 5*np.sum(x[:4])-5*np.sum(np.multiply(x[:4],x[:4]))-np.sum(x[4:])
    return f
    
def satisfyConstraints(pos):
    t1=2*pos[0]+2*pos[1]+pos[9]+pos[10]-10
    t2=2*pos[0]+2*pos[2]+pos[9]+pos[10]-10
    t3=2*pos[1]+2*pos[2]+pos[10]+pos[11]-10
    t4=-8*pos[0]+pos[9]
    t5=-8*pos[1]+pos[10]
    t6=-8*pos[2]+pos[11]
    t7=-2*pos[3]-pos[4]+pos[9]
    t8=-2*pos[5]-pos[6]+pos[10]
    t9=-2*pos[7]-pos[8]+pos[11]
        
    constraint=False
    if t1<=0 and t2<=0 and t3<=0 and t4<=0 and t5<=0 and t6<=0 and t7<=0 and t8<=0 and t9<=0:
        constraint=True
    
    return constraint 
#dim 13 l [0] U [1,1,1,1,1,1,1,1,1,100,100,100,1] -15
def multi2(X):
    x=np.asarray(X)
    CS1=np.sum(np.cos(x)**4)
    CS2=np.prod(np.cos(x)**2)
    i=np.asarray(range(1,len(X)+1))
    x2=np.sqrt(np.sum(np.multiply(i,x**2)))
    f=(CS1-2*CS2)/x2
    return f
def satisfyConstraints2(pos):
    x=np.asarray(pos)
    t1=-np.prod(x)+.75
    t2=np.sum(x)-7.5*len(pos)
    constraint=False
    if t1<=0 and t2<=0:
        constraint=True
    return constraint
#dim 20 l [0] U [10] -.803619
def multi3(X): #maximisation
    x=np.asarray(X)
    d=len(X)
    f=np.sqrt(d)**d*np.prod(x)
    return -f
def satisfyConstraints3(pos):
    x=np.asarray(pos)
    t1=np.sum(x**2-1)
    constraint=False
    if t1==0:
        constraint=True
    return constraint
#dim 20 l [0] U [1] -1
def multi4(X):
    f=5.3578547*x[2]**2+0.8356891*x[0]*x[4]+37.293239*x[0]-40792.141
    return f
def satisfyConstraints4(pos):
    x=np.asarray(pos)
    u=85.334407+0.0056858*x[1]*x[4]+0.0006262*x[0]*x[4]+.0022053*x[2]*x[4]
    v=80.51249+0.0071317*x[1]*x[4]+0.0029955*x[0]*x[1]+0.002181*x[2]**2
    w=9.300961+0.0047026*x[2]*x[4]+0.0012547*x[0]*x[2]+0.0019085*x[2]*x[3]
    t1=u-92
    t2=u
    t3=v-110
    t4=-v+90
    t5=w-25
    t6=-w+20
    constraint=False
    if t1<=0 and t2<=0 and t3<=0 and t4<=0 and t5<=0 and t6<=0:
        constraint=True
    return constraint
#dim 5 L [78,33,27,27,27] U [102,45,45,45,45] -30665.539 
def multi5(x):
    f=3*x[0]+0.000001*x[0]**3+2*x[1]+(2/3)*0.000001*x[1]**3
    return f
def satisfyConstraints5(pos):
    h1=1000*(np.sin(-x[2]-0.25)+np.sin(-x[3]-0.25))+894.8-x[0]
    h2=1000*(np.sin(x[2]-0.25)+np.sin(x[2]-x[3]-0.25))+894.8-x[1]
    h3=1000*(np.sin(x[3]-0.25)+np.sin(x[3]-x[2]-0.25))+1294.8
    t1=x[2]-x[3]-0.55
    t2=x[3]-x[2]-0.55
    constraint=False
    if t1<=0 and t2<=0 and h1==0 and h2==0 and h3==0:
        constraint=True
    return constraint
#dim 4 l [0,0,-0.55,-.55] U [1200,1200,0.55,0.55] 5126.4981
def multi6(x):
    f=(x[0]-10)**2+(x[1]-20)**3
    return f
def satisfyConstraints6(pos):
    t1=-(pos[0]-5)**2-(pos[1]-5)**2+100
    t2=(pos[0]-6)**2+(x[1]-5)**2-82.81
    constraint=False
    if t1<=0 and t2<=0:
        constraint=True
    return constraint
#dim 2 l[ 13,0] U [100,100] -6961.81387558015
def multi7(x):
    f=x[0]**2+x[1]**2+x[0]*x[1]-14*x[0]-16*x[1]+(x[2]-10)**2+4*(x[3]-5)**2+(x[4]-3)**2+2*(x[5]-1)**2+5*x[6]**2+7*(x[7]-11)**2+2*(x[8]-10)**2+(x[9]-7)**2+45
    return f
def satisfyConstraints7(x):
    t1=-105+4*x[0]+5*x[1]-3*x[6]+9*x[7]
    t2=10*x[0]-8*x[1]-17*x[6]+2*x[7]
    t3=-8*x[0]+2*x[1]+5*x[8]-2*x[9]-12
    t4=3*(x[0]-2)**2+4*(x[1]-3)**2+2*x[2]**2-7*x[3]-120
    t5=5*x[0]**2+8*x[1]+(x[2]-6)**2-2*x[4]-40
    t6=x[0]**2+2*(x[1]-4)**2-2*x[0]*x[1]+14*x[4]-6*x[5]
    t7=0.5*(x[0]-8)**2+2*(x[1]-4)**2+3*x[4]**2-x[5]-30
    t8=-3*x[0]+6*x[1]+12*(x[8]-8)**2-7*x[9]
    constraint=False
    if t1<=0 and t2<=0 and t3<=0 and t4<=0 and t5<=0 and t6<=0 and t7<=0 and t8<=0:
        constraint=True
    return constraint
#dim 10 l[-10] U [10] 24.30620906818
def multi8(x):
    f=-np.sin(2*3.14*x[0])*np.sin(2*3.14*x[1])/(x[0]**3*(x[0]+x[1]))
    return f
def satisfyCostraints8(x):
    t1=x[0]**2-x[1]+1
    t2=1-x[0]+(x[1]-4)**2
    constraint=False
    if t1<=0 and t2<=0:
        constraint=True
    return constraint
#dim 2 l[0] U[10] -0.09582504
def multi9(x):
    f=(x[0]-10)**2+5*(x[1]-12)**2+x[2]**4+3*(x[3]-11)**2+10*x[4]**6+7*x[5]**2+x[6]**4-4*x[5]*x[6]-10*x[5]-8*x[6]
    return     
def satisfyConsraints9(x):
    t1=-127+2*x[0]**2+3*x[1]**4+x[2]+4*x[3]**2+5*x[4]
    t2=-282+7*x[0]+3*x[1]+10*x[2]**2+x[3]-x[4]
    t3=-196+23*x[0]+x[1]**2+6*x[5]**2-8*x[6]
    t4=4*x[0]**2+x[1]**2-3*x[0]*x[1]+2*x[2]**2+5*x[5]-11*x[6]
    constraint=False
    if t1<=0 and t2<=0 and t3<=0 and t4<=0:
        constraint=True
    return constraint
#dim 7 l[-10] U[10] 680.630057374402
def multi10(x):
    f=x[0]+x[1]+x[2]
    return f
def satisfyConstraints10(x):
    t1=-1+0.0025*(x[3]+x[5])
    t2=-1+0.0025*(x[4]+x[6]-x[3])
    t3=-1+0.01*(x[7]-x[4])
    t4=-x[0]*x[5]+833.33252*x[3]+100*x[0]-83333.333
    t5=-x[1]*x[6]+1250*x[4]+x[1]*x[3]-1250*x[3]
    t6=-x[2]*x[7]+1250000+x[2]*x[4]-2500*x[4]
    constraint=False
    if t1<=0 and t2<=0 and t3<=0 and t4<=0 and t5<=0 and t6<=0:
        constraint=True
    return constraint
#dim 8 l [100,1000,1000,1000,10,..10] U [10000,10000,10000,10000,1000,...] 7049.24802052867
def multi11(x):
    f=x[0]**2+(x[1]-1)**2
    return f
def satisfyConstraints11(x):
    t1=x[1]-x[0]**2
    constraint=False
    if t1==0:
        constraint=True
    return constraint
#dim 2 l[-1] U[1] 0.7499
def multi12(x):
    f=-(100-(x[0]-5)**2-(x[1]-5)**2-(x[2]-5)**2)/100
    return f
def satisfyConstraints12(x):
    X=np.asarray(x)
    t1=np.sum((X-1)**2)-0.0625
    t2=np.sum((X-2)**2)-0.0625
    t3=np.sum((X-3)**2)-0.0625
    t4=np.sum((X-4)**2)-0.0625
    t5=np.sum((X-5)**2)-0.0625
    t6=np.sum((X-6)**2)-0.0625
    t7=np.sum((X-7)**2)-0.0625
    t8=np.sum((X-8)**2)-0.0625
    t9=np.sum((X-9)**2)-0.0625
    constraint=False
    if t1<=0 and t2<=0 and t3<=0 and t4<=0 and t5<=0 and t6<=0 and t7<=0 and t8<=0 and t9<=0:
        constraint=True
    return constraint
#dim 3 l[0] u[10] -1
def multi13(x):
    X=np.asarray(x)
    p=np.prod(X)
    f=np.exp(p)
    return f
def satisfyConstraints13(x):
    X=np.asarray(x)
    t1=np.sum(X**2)-10
    t2=X[1]*X[0]-5*X[3]*X[4]
    t3=X[0]**3+X[1]**3+1
    constraint=False
    if t1==0 and t2==0 and t3==0:
        constraint=True
    return constraint
#dim 5 l [-2.3,-2.3,-3.2,-3.2,-3.2] U [2.3,2.3,3.2,3.2,3.2] 0.05394154041898
def multi14(x):
    c=np.asarray([-6.089,-17.164,-34.054,-5.914,-24.721,-14.986,-24.1,-10.708,-26.662,-22.179])
    X=np.asarray(x)
    s=np.sum(X)
    X1=X/s
    lg=np.log(X1)
    lgc=c+lg
    X2=np.sum(np.multiply(X,lgc))
    return X2
def satisfyConstraints14(x):
    t1=x[0]+2*x[1]+2*x[2]+x[5]+x[9]-2
    t2=x[3]+2*x[4]+x[5]+x[6]-1
    t3=x[2]+x[6]+x[7]+2*x[8]+x[9]-1
    constraint=False
    if t1==0 and t2==0 and t3==0:
        constraint=True
    return constraint
#dim 10 l[0] U[10] -47.7648884594915
def multi15(x):
    f=1000-x[0]**2-2*x[1]**2-x[2]**2-x[0]*x[1]-x[0]*x[2]
    return f
def satisfyConstraints15(x):
    t1=x[0]**2+x[1]**2+x[2]**2-25
    t2=8*x[0]+14*x[1]+7*x[2]-56
    constraint=False
    if t1==0 and  t2==0:
        constraint=True
    return constraint
#dim 3 l[0] U[10] 961.715022289961

        

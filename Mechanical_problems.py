def multi16(x): # x: d D N
    f=(x[2]+2)*x[1]*x[0]*x[0]
    return f
def satisfyConstraints16(x):
    t1=1-((x[1]**3*x[2])/(717854*x[0]**4))
    t2=((4*x[1]**2-x[0]*x[1])/(12566*(x[1]*x[0]**3-x[0]**4)))+(1/(5108*x[0]**2))
    t3=1-((140.45*x[0])/(x[1]*x[1]*x[2]))
    t4=((x[0]+x[1])/1.5)-1
    constraint=False
    if t1<=0 and t2<=0 and t3<=0 and t4<=0:
        constraint=True
    return constraint
#dimn 3 [0.05,2.00] [0.25,1.30] [2.00,15] x1 0.05276 x2 0.804380 x3 2 f 0.011958
def multi17(x): #x: h,l,t,b
    f=1.10471*x[0]*x[0]*x[1]+0.04811*x[2]*x[3]*(14+x[1])
    return f
def satisfyConstraints17(x):
    P=6000 #lb 
    L=14 #inch
    delta_mx=0.25 #inch
    E=30*10**6
    G=12*10**6
    T_max=13600
    sig_max=30000
    Pc=4.013*E*np.sqrt(x[2]**2*x[3]**6/36)*(1-(x[2]*0.5/L)*np.sqrt(E*0.25/G))/(L*L)
    delta=4*P*L**3/(E*x[2]**2*x[3])
    sigma=6*P*L/(x[3]*x[2]**2)
    J=2*(np.sqrt(2)*x[0]*x[1]*((x[1]*x[1]/12)+(x[0]+x[2])**2/4))
    R=np.sqrt(x[1]*x[1]*0.25+(x[0]+x[2])**2*0.25)
    M=P*(L+0.5*x[1])
    T2=M*R/J
    T1=P/(np.sqrt(2)*x[0]*x[1])
    T=np.sqrt(T1*T1+2*T1*T2*x[1]*(0.5/R)+T2*T2)
    t1=T-T_max
    t2=sigma-sig_max
    t3=delta-delta_mx
    t4=x[0]-x[3]
    t5=P-Pc
    t6=0.125-x[0]
    t7=0.10471*x[0]*x[0]+0.04811*x[2]*x[3]*(14+x[1])-5
    constraint=False
    if t1<=0 and t2<=0 and t3<=0 and t4<=0 and t5<=0 and t6<=0 and t7<=0 and x[0]>0.1 and x[1]>0.1 and x[2]>0.1 and x[3]>0.1:
        constraint=True
    return constraint 
#dim 4 L[0.1] U[2,10,10,2] x1 0.343891 x2 1.883570 x3 9.03133 x4 0.212121 f 1.72545
def multi18(x):
    f=0.6224*x[0]*x[2]*x[3]+1.7781*x[1]*x[2]**2+3.1661*x[0]*x[0]*x[3]+19.84*x[0]*x[0]*x[2]
    return f
def satisfyConstraints18(x):
    t1=-x[0]+0.0193*x[2]
    t2=-x[1]+0.00954*x[2]
    t3=-3.14*x[2]*x[2]*x[3]-4*3.14*(x[2]**3/3)+1296000
    t4=x[3]-240
    constraint=False
    if t1<=0 and t2<=0 and t3<=0 and t4<=0:
        constraint=True
    return constraint
#dim 4 [0,0,10,10] [100,100,200,200] x1 1.187150 x2 0.6 x3 69.7075 x4 7.798440 f 5034.1800
        
def multi19(x): # d,D,Nc
    f=3.14*3.14*(x[2]+2)*x[1]*x[0]*x[0]/4
    return f
def satisfyConstraints19(x):
    C=x[1]/x[0]
    C_f=((4*C-1)/(4*C-4))+(0.615/C)
    S=13288.02
    Fmax=453.6
    
    t1=S-8*C_f*Fmax*x[1]/(3.14*x[0]**3)
    
    G=808543.6
    K=G*x[0]**4/(8*x[2]*x[1]**3)
    delta_l=Fmax/K
    l_f=delta_l+1.05*(x[2]+2)*x[0]
    
    t2=35.56-l_f
    t3=x[0]-0.508
    t4=7.62-(x[0]+x[1])
    t5=C-3
    
    delta_p=136.08/K
    
    t6=15.24-delta_p
    t7=((Fmax-136.08)/K)-1.05*(x[2]+2)*x[0]
    t8=((Fmax-136.08)/K)-3.175
    
    constraint=False
    if t8<=0 and t7>=0 and t6>=0 and t5>=0 and t4>=0 and t3>=0 and t2>=0 and t1>=0:
        constraint=True
    return constraint
#dim 3 d [0.508,1.016] D [1.27,7.620] Nc [15,25] d 0.599394 D 1.92367 f 42.0990
def multi20(x):
    X=np.asarray(x)
    f=0.6224*(np.sum(X))
    return f
def satisfyConstraints20(x):
    t1=(61/x[0]**3)+(37/x[1]**3)+(19/x[2]**3)+(7/x[3]**3)+(1/x[4]**3)
    constraint=False
    if t1<=1 and x[0]>0.01 and x[1]>0.01 and x[2]>0.01 and x[3]>0.01 and x[4]>0.01:
        constraint=True
    return constraint
# dimn 5 [0.01] [100]
def multi21(x):
    l=100
    f=(2*np.sqrt(2)*x[0]+x[1])*l
    return f
def satisfyConstraints21(x):
    P=2
    Sig=2
    t1=((np.sqrt(2)*x[0]+x[1])*P/(np.sqrt(2)*x[0]*x[0]+2*x[0]*x[1]))-Sig
    t2=(x[1]/(np.sqrt(2)*x[0]*x[0]+2*x[0]*x[1]))*P-Sig
    t3=(P/(np.sqrt(2)*x[1]+x[0]))-Sig
    constraint=False
    if t1<=0 and t2<=0 and t3<=0 and x[0]<=1 and x[0]>0 and x[1]>0 and x[1]<=1:
        constraint=True
    return constraint
#dim 2 [0] [1]


        
    

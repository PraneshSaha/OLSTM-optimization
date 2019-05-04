import numpy as np
import math
import copy

# This class contains the code of the Particles in the swarm
class short_term_particle():
   
 
    def __init__(self,dimension,low,high):
        self.pos=[]
        self.velocity=[]
        self.pBest=np.zeros((7,dimension))
        self.vel_clamp=[.1,250,50]
        self.low=low
        self.high=high
        self.dimension=dimension
        self.func_val=[]
        #self.is_constraint=is_constraint
        
        
        
        for i in range(dimension):
            self.pos.append(np.random.uniform(self.low[i],self.high[i]))
            self.velocity.append(np.random.uniform(0,self.vel_clamp[i]))
            self.pBest[0,i]=np.random.uniform(self.low[i],self.high[i])
        
        
        self.func_val.append(milling(self.pBest[0,:]))      #FUNCTION EVAL
       
        self.w = 0.729844 # Inertia weight to prevent velocities becoming too large
        self.c1 = 1.496180 # Scaling co-efficient on the social component
        self.c2 = 1.496180 # Scaling co-efficient on the cognitive component

        
    def pbest_get(self,iteration):
        
        l=self.pBest.shape[1]
    
        if iteration==0:
            ind=7
        else:
            ind=iteration
        #self.func_val.append(Ackeley(self.pBest[ind-1]))
        m1=np.random.randint(1,ind+1)    #m1 : amount of lookback
        pbest=np.zeros((self.dimension,1))
        pr=np.random.uniform(0,1)
        if pr>0.5:
            pbest=self.pBest[np.argmin(self.func_val[:m1]),:]*np.random.uniform(.91,1.1)
        else:
            pbest=self.pBest[np.argmin(self.func_val[:m1]),:]
        return pbest
    
    def forget_me(self):
        pbest=np.zeros((1,self.dimension))
        #print(self.pBest.shape)
        pbest[0,:]=self.pBest[np.argmin(self.func_val),:]
        self.pBest[0,:]=pbest[0,:]
        self.pBest[1:,:]=0
        self.func_val=[min(self.func_val)]
        return
    
    def updatePositions(self,gBest,iter_no):
        
        
       
        self.updateVelocities(gBest,iter_no)
       
        for i in range(self.dimension):
            self.pos[i] = self.pos[i] + self.velocity[i]  
            #print("shr Particle"+str(iter_no)+"in loop",gBest,self.pos[i])
            if self.pos[i]>=self.high[i]:
                delta=self.pos[i]-self.high[i]
                self.pos[i]=self.pos[i]-np.random.uniform(delta+.02,delta+.04)
                #print("more",gBest)
                
            elif self.pos[i]<=self.low[i]:
                delta=self.low[i]-self.pos[i]
                self.pos[i]=self.pos[i]+np.random.uniform(delta+0.01,delta+.03)
                #print(self.pos[i])
                #print("less",gBest)
            if iter_no!=0:
                self.pBest[iter_no,i]=self.pos[i]
            #print("shr Particle"+str(iter_no)+"in loop",gBest,self.pos[i])
       
        
        f1=milling(self.pos) #FUNCTION EVAL
        
        
        if iter_no==0:
            if f1<self.func_val[0]:
                self.func_val=[f1]
                self.pBest[0,:]=self.pos
            else:
                self.pos=self.pBest[0,:]
                f1=self.func_val[0]
        else:
            self.func_val.append(f1)
        #print("sh",gBest,Gbst)
        return self.pos,f1
 
    def updateVelocities(self, gBest,iter_no):
        
        for i in range(self.dimension):
            pbest=0
            theta1=np.random.randint(5,75)*3.14/180
            theta2=np.random.randint(5,75)*3.14/180
            theta3=np.random.randint(5,75)*3.14/180
            if iter_no>1:
                pbest=self.pbest_get(iter_no)
            elif iter_no==0:
                pbest=self.pbest_get(iter_no)
                self.forget_me()
                #print("forgetting",gBest)
            elif iter_no==1:
                pbest=self.pBest[0,:]
            if len(gBest)==0:
                self.velocity[i]=np.random.uniform(0,self.vel_clamp[i])
            else:
                social = self.c1 * (gBest[i] - self.pos[i])
            #print("lng particle"+str(iter_no)+"in vel loop",gBest,self.velocity[i])
                cognitive = self.c2 * (pbest[i] - self.pos[i])
                self.velocity[i] = np.cos(theta3)* (self.w * self.velocity[i]) + np.cos(theta2)*social + np.cos(theta1)*cognitive
            if abs(self.velocity[i])>self.vel_clamp[i]:
                self.velocity[i]=self.velocity[i]*np.cos(3.14/2.5)
                #print("more",self.velocity[i])
        #print("shv",gBest)
        return 
 
    
    
    
    
class long_term_particle():
    def __init__(self,dimension,low,high):
        self.pos=[]
        self.velocity=[]
        self.pBest=np.zeros((30,dimension))
        self.for_del=[]
        self.vel_clamp=[0.1,250,50]
        self.low=low
        self.high=high
        self.dimension=dimension
        self.func_val=np.zeros((30,1))
        
        
        
        #print("long")
        
        for i in range(dimension):
            self.pos.append(np.random.uniform(self.low[i],self.high[i]))
            self.velocity.append(np.random.uniform(0,self.vel_clamp[i]))
            
        for i in range(30):
            for j in range(self.dimension):
                self.pBest[i,:]=np.random.uniform(self.low[j],self.high[j],self.dimension)
            
            self.func_val[i,:]=milling(self.pBest[i,:])              #FUNCTION EVAL
            
        self.w = 0.729844 # Inertia weight to prevent velocities becoming too large
        self.c1 = 1.496180 # Scaling co-efficient on the social component
        self.c2 = 1.496180 # Scaling co-efficient on the cognitive component

        
    def pbest_get(self,iter_no):
        l=self.pBest.shape[1]

        #self.func_val[ind-1]=Ackeley(self.pBest[ind-1])
        m1=np.random.randint(1,30)    #m1 : amount of lookback
        pbest=np.zeros((self.dimension,1))
        
        pbest=self.pBest[np.argmin(self.func_val[:m1]),:]
        
        return pbest
    
    def forget_me(self,pbest):
        
        to_delete=np.random.randint(0,30,6)
        for i in to_delete:
            for j in range(self.dimension):
                self.pBest[i,j]=np.random.normal((self.high[j]+self.low[j])*.5,(self.high[j]-self.low[j])/4)
            
            self.func_val[i]=milling(self.pBest[i,:])          #FUNCTION EVAL
            self.pBest[i,:]=self.pBest[i,:]#*np.random.uniform(0.91,1.1)    
        return
    
    def updatePositions(self,gBest,iter_no):
        #print('lng1',gBest)
        self.updateVelocities(gBest,iter_no)
        
        for i in range(self.dimension):
            
            self.pos[i] = self.pos[i] + self.velocity[i]  
            #print("lng Particle"+str(iter_no)+"in loop",gBest,self.pos[i])
            if self.pos[i]>=self.high[i]:
                delta=self.pos[i]-self.high[i]
                self.pos[i]=self.pos[i]-np.random.uniform(delta+.02,delta+.04)
                #print("more",gBest)
               
            elif self.pos[i]<=self.low[i]:
                #print("in")
                delta=self.low[i]-self.pos[i]
                self.pos[i]=self.pos[i]+np.random.uniform(delta+0.01,delta+.03)
                #print("less",gBest)
            self.pBest[iter_no,i]=self.pos[i]
            #print("lng Particle"+str(iter_no)+"in loop",gBest,self.pos[i])
        
        self.func_val[iter_no,0]=milling(self.pos) #FUNCTION EVAL
        
        return self.pos,self.func_val[iter_no,0]
 
    def updateVelocities(self, gBest,iter_no):
        
        for i in range(self.dimension):
            pbest=0
            theta1=np.random.randint(10,75)*3.14/180
            theta2=np.random.randint(10,75)*3.14/180
            theta3=np.random.randint(10,75)*3.14/180
            if iter_no!=0:
                pbest=self.pbest_get(iter_no)
            else:
                pbest=self.pbest_get(iter_no)
                self.forget_me(pbest)  
            if len(gBest)==0:
                self.velocity[i]=np.random.uniform(-self.vel_clamp[i],self.vel_clamp[i])
            else:
                social = self.c1 * (gBest[i] - self.pos[i])
            #print("lng particle"+str(iter_no)+"in vel loop",gBest,self.velocity[i])
                cognitive = self.c2 * (pbest[i] - self.pos[i])
                self.velocity[i] = np.cos(theta3)* (self.w * self.velocity[i]) + np.cos(theta2)*social + np.cos(theta1)*cognitive
            if abs(self.velocity[i])>self.vel_clamp[i]:
                self.velocity[i]=self.velocity[i]*np.cos(3.14/2.5)
                #print("over particle"+str(iter_no),self.velocity[i])
       # print("lngv",gBest)
        return
 
   
            
    
    
class optimistic():
    def __init__(self,gbest_pos,low,high,i):
        self.pos=[]
       
        self.d=len(gbest_pos)
        self.gBest=gbest_pos
        
        self.low1=low
        self.high1=high
        self.t=1/np.power(i,(1/2))
        self.b=max(abs(max(low)),abs(min(high)))
        #print(self.low.shape)
        for i in range(len(gbest_pos)):
            self.pos.append(np.random.normal(self.gBest[i],1))
            
        
    def update_pos(self):
        
        for i in range(self.d):
            self.pos[i]=self.gBest[i]+np.random.uniform(-self.t*self.gBest[i],self.t*self.gBest[i])
            
            if self.pos[i]<=self.low1[i] :
                delta=self.low1[i]-self.pos[i]
                self.pos[i]=self.pos[i]+np.random.uniform(delta+.001,delta+.002)
            elif self.pos[i]>=self.high1[i]:
                delta=self.pos[i]-self.high1[i]
                self.pos[i]=self.pos[i]-np.random.uniform(delta+.001,delta+.002)
        return self.pos
    
    

    
    
class ParticleSwarmOptimizer():
    
    def __init__(self,swarm_size,dimension,low,high,iterations):
        #self.opt=0 #chnge with function
        #self.epsilon=0.0
        self.swarm_shrt=[]
        self.swarm_lng=[]
        #self.gbest=[]
        
        self.solution=[]
        
        self.low=low
        self.high=high
        self.iterations=iterations
        self.dimension=dimension
        sht_p=int(.45*swarm_size)
        lng_p=int(.45*swarm_size)
        self.opt_p=int(.1*swarm_size)
        for i in range(sht_p):
            particle1 = short_term_particle(dimension,low,high)
            self.swarm_shrt.append(particle1)
            particle2 = long_term_particle(dimension,low,high)
            self.swarm_lng.append(particle2)
        
        
    def optimize(self):
        Gbest=[]
        for i in range(dimension):
            Gbest.append(np.random.uniform(low[i],high[i]))
        
        gmin=milling(Gbest)       #FUNCTION EVAL
        itr=0
        solution=0
        pos=[]
        opt=[]
        minm=1000
        min_pos=[]
        minm2=1000
        min_pos2=[]
        min_opt=np.inf
        pos_opt=[]
       
        for i in range(1,self.iterations+1):
            if i%200==0:
                print ("iteration ", i)
            #print('0',gmin,Gbest)
            gBB=copy.deepcopy(Gbest)
            
            for j in range(len(self.swarm_shrt)):
                
                pos,val=self.swarm_shrt[j].updatePositions(Gbest,i%7)
                
                if minm>val:
                    minm=val
                    min_pos=pos
                    
                elif i==1:
                    minm=val
                    min_pos=pos
                
                pos2,val2=self.swarm_lng[j].updatePositions(Gbest,i%30)   
                                
                if minm2>val2:
                    minm2=val2
                    min_pos2=pos2
                elif i==1:
                    minm2=val2
                    min_pos2=pos2
                    
                
                if len(Gbest)!=0:
                    if Gbest[0]!=gBB[0]:
                        Gbest=copy.deepcopy(gBB)
              
            if i%2==0:
                opt=[]
                for j in range(self.opt_p):
                    part=optimistic(Gbest,self.low,self.high,i)
                    #print(j)
                    opt.append(part)
            
           
            if i>=2:
                for j in range(self.opt_p):
                    pos=opt[j].update_pos()
                    val=0
                    
                    val=milling(pos) #FUNCTION EVAL
                    if min_opt>=val:
                        min_opt=val
                        pos_opt=pos
                    elif i==2:
                        min_opt=val
                        pos_opt=pos
            #print('3',gmin,Gbest) 
            
            sltn=min(minm,minm2,min_opt)
            a=np.asarray([minm,minm2,min_opt])
            ps=np.argmin(a)
            
            pos=[min_pos,min_pos2,pos_opt]
            
            gb=pos[ps]
            
            if sltn<gmin:
                #print(Gbest)
                gmin=sltn
                Gbest=gb
            if i%200==0:
                print(gmin,Gbest)
                #print(Gbest)
            self.solution.append((sltn))
            #if abs(gmin-self.opt)<=self.epsilon:
                #solution=gmin
                #itr=i
                #pos=Gbest
                #break
        solution=gmin
        itr=i
        pos=Gbest
        return solution,itr,pos,self.solution
    
    
   

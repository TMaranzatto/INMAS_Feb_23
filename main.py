# adding a comment to push
"""
Created on Fri Jan  3 20:04:19 2020
@author: gaurav
"""

import scipy as sci
import numpy as np
import matplotlib.pyplot as plt

#Create function to assign seat number to each passenger
def AssignSeats(rq,cq,assign_type,ac):
    n_rows=ac.n_rows
    n_pass=ac.n_pass
    n_cols=ac.n_cols
    if(assign_type=="SINP"):        
        #Initialize initial and final positions
        i=0
        f=ac.n_rows
        
        #Define column seating positions 
        c=[0,5,1,4,2,3]
        
        #Define iteratiion counter
        count=0
        
        #Assign queue
        while(f<=n_pass):
            rq[i:f]=list(reversed(range(0,n_rows)))
            cq[i:f]=[c[count]]*n_rows
            i+=n_rows
            f+=n_rows
            count+=1
    
    if(assign_type=="Random"):
        av_rows=np.arange(0,n_rows,1)
        av_rows=np.tile(av_rows,(n_cols,1))
        av_rows=av_rows.T.flatten()
        av_cols=np.arange(0,n_cols,1)
        av_cols=np.tile(av_cols,(n_rows,1)).flatten()
        av_seats=np.zeros((n_pass,2))
        for i in range(n_pass):
            av_seats[i]=[av_rows[i],av_cols[i]]
        np.random.shuffle(av_seats)
        rq=av_seats[:,0]
        cq=av_seats[:,1]
        
    if(assign_type=="BTF"):
        av_rows=np.arange(0,n_rows,1)
        av_rows=np.tile(av_rows,(n_cols,1))
        av_rows=av_rows.T.flatten()
        av_cols=np.arange(0,n_cols,1)
        av_cols=np.tile(av_cols,(n_rows,1)).flatten()
        av_seats=np.zeros((n_pass,2))
        for i in range(n_pass):
            av_seats[i]=[av_rows[i],av_cols[i]]
        group1=av_seats[:48]
        np.random.shuffle(group1)
        group2=av_seats[48:96]
        np.random.shuffle(group2)
        group3=av_seats[96:]
        np.random.shuffle(group3)
        av_seats_final=np.concatenate((group3,group2,group1))
        rq=av_seats_final[:,0]
        cq=av_seats_final[:,1]
        
    if(assign_type=="FTB"):
        av_rows=np.arange(0,n_rows,1)
        av_rows=np.tile(av_rows,(n_cols,1))
        av_rows=av_rows.T.flatten()
        av_cols=np.arange(0,n_cols,1)
        av_cols=np.tile(av_cols,(n_rows,1)).flatten()
        av_seats=np.zeros((n_pass,2))
        for i in range(n_pass):
            av_seats[i]=[av_rows[i],av_cols[i]]
        group1=av_seats[:48]
        np.random.shuffle(group1)
        group2=av_seats[48:96]
        np.random.shuffle(group2)
        group3=av_seats[96:]
        np.random.shuffle(group3)
        av_seats_final=np.concatenate((group1,group2,group3))
        rq=av_seats_final[:,0]
        cq=av_seats_final[:,1]

    if(assign_type=="WMA"):
        window_1=np.array([0]*n_rows)
        rows_1=np.arange(0,n_rows,1)
        window_2=np.array([5]*n_rows)
        rows_2=np.arange(0,n_rows,1)
        window=np.concatenate((window_1,window_2))
        rows=np.concatenate((rows_1,rows_2))
        av_seats_w=np.column_stack((rows,window))
        np.random.shuffle(av_seats_w)
        
        middle_1=np.array([1]*n_rows)
        middle_2=np.array([4]*n_rows)
        middle=np.concatenate((middle_1,middle_2))
        av_seats_m=np.column_stack((rows,middle))
        np.random.shuffle(av_seats_m)
        
        aisle_1=np.array([2]*n_rows)
        aisle_2=np.array([3]*n_rows)
        aisle=np.concatenate((aisle_1,aisle_2))
        av_seats_a=np.column_stack((rows,aisle))
        np.random.shuffle(av_seats_a)
        
        av_seats=np.concatenate((av_seats_w,av_seats_m,av_seats_a))
        rq=av_seats[:,0]
        cq=av_seats[:,1]
        
    if(assign_type=="Southwest"):
        #Make an array [0,5,0,5,...]
        window=np.array([0,5]*n_rows)
        
        #Make an array [0,0,1,1,2,2,...]
        rows_1=np.arange(0,n_rows,1)
        rows_2=np.arange(0,n_rows,1)
        rows=sci.ravel(np.column_stack((rows_1,rows_2)))
        
        w_seats=np.column_stack((rows,window))
        w_group1=w_seats[:32,:]
        w_group2=w_seats[32:,:]
        
        aisle=np.array([2,3]*n_rows)
        a_seats=np.column_stack((rows,aisle))
        a_group1=a_seats[:32,:]
        a_group2=a_seats[32:,:]
        
        mega_group1=np.concatenate((w_group1,a_group1))
        np.random.shuffle(mega_group1)
        mega_group2=np.concatenate((w_group2,a_group2))
        np.random.shuffle(mega_group2)
        
        w_and_a=np.concatenate((mega_group1,mega_group2))
        
        middle=np.array([1,4]*n_rows)
        m_seats=np.column_stack((rows,middle))
        m_group1=m_seats[:32,:]
        np.random.shuffle(m_group1)
        m_group2=m_seats[32:,:]
        np.random.shuffle(m_group2)
        
        av_seats=np.concatenate((w_and_a,m_group1,m_group2))
        rq=av_seats[:,0]
        cq=av_seats[:,1]
        
    return rq,cq


class Aircraft():
    def __init__(self):
        pass

    def Initialize737(self):
        #Initialize zero arrays
        #Define number of rows and columns
        self.n_rows=23
        self.n_cols=6
    
        #Calculate number of passengers
        self.n_pass=self.n_rows*self.n_cols
    
        #Create seat matrix
        self.seats=np.zeros((self.n_rows,self.n_cols))
        self.seats[:,:]=-1
    
        #Create aisle array
        self.aisle_q=np.zeros(self.n_rows)
        self.aisle_q[:]=-1
        
        #Create initial passenger number queue
        self.pass_q=[int(i) for i in range(self.n_pass)]
        self.pass_q=np.array(self.pass_q)
        
        #Create array for seat nos
        self.row_q_init=np.zeros(self.n_pass)
        self.col_q_init=np.zeros(self.n_pass)
        
        #Define multipliers
        self.empty_mult=1+2
        self.aisle_mult=4+2
        self.middle_mult=5+2
        self.aisle_middle_mult=7+2
        
        #Let's create moveto arrays
        moveto_loc=np.zeros(self.n_pass)
        moveto_time=np.zeros(self.n_pass)
    
        self.moveto_loc_dict={i:j for i in self.pass_q for j in moveto_loc}
        self.moveto_time_dict={i:j for i in self.pass_q for j in moveto_time}
        
    def IssueSeatingOrder(self,assign_type):
        #Assign seating order
        self.row_q,self.col_q=AssignSeats(self.row_q_init,self.col_q_init,assign_type,self)
        
        #Create seat and speed dictionary
        self.pass_dict={}
        self.time_dict={}
        
        #Create array for speeds
        mean_time=1.
        stddev_time=0.2
        self.time_q=np.random.normal(loc=mean_time,scale=stddev_time,size=self.n_pass)
    
        seat_nos=np.column_stack((self.row_q,self.col_q))
        for i in range(self.n_pass):
            self.pass_dict[i]=seat_nos[i]
    
        for i in range(self.n_pass):
            self.time_dict[i]=self.time_q[i]
            
        #Create sum time array
        self.sum_time=np.zeros(self.n_pass)
        for i in range(self.n_pass):
            self.sum_time[i]=sum(self.time_q[:i+1])
        

#Create function to move passengers into aircraft
def MoveToAisle(t,aisle_q,pass_q,sum_time):
    if(t>sum_time[0]):
        if(aisle_q[0]==-1):
            aisle_q[0]=pass_q[0].copy()
            pass_q=np.delete(pass_q,0)
            sum_time=np.delete(sum_time,0)
    return aisle_q,pass_q,sum_time
#Let's define the boarding process in a while loop
#Define initial conditions
def BoardFlight(ac):
    ac.time=0
    n_iter=0
    time_step=0.1
    exit_sum=np.sum(ac.pass_q)
    pass_sum=np.sum(ac.seats)
    
    #Imaging definitions
    ac.img_list=[]
    iters_per_snap=50
    
    
    while(pass_sum!=exit_sum):
        #Try to move passenger inside the plane if passengers are left
        if(ac.pass_q.size!=0):
            ac.aisle_q,ac.pass_q,sum_time=MoveToAisle(ac.time,ac.aisle_q,ac.pass_q,ac.sum_time)
        #Scan the aisle first for non-negative units (passengers)
        for passg in ac.aisle_q:
            if(passg!=-1):
                #Store the row of passenger in aisle
                row=int(np.where(ac.aisle_q==passg)[0][0])
                #See if move has been assigned to passenger
                if(ac.moveto_time_dict[passg]!=0):
                    #If move has been assigned check if it is time to move
                    if(ac.time>ac.moveto_time_dict[passg]):
                        #If it is time to move follow the procedure below
                        #Check if move is forward in aisle or to seat
                        if(ac.moveto_loc_dict[passg]=="a"):
                            #If move is in the aisle, check if position ahead is empty
                            if(ac.aisle_q[row+1]==-1):
                                #If position is empty move passenger ahead and free the position behind
                                ac.aisle_q[row+1]=passg
                                ac.aisle_q[row]=-1
                                #Set moves to 0 again
                                ac.moveto_loc_dict[passg]=0
                                ac.moveto_time_dict[passg]=0
                        elif(ac.moveto_loc_dict[passg]=="s"):
                            #If move is to the seat,
                            #Find seat row and column of passenger
                            passg_row=int(ac.pass_dict[passg][0])
                            passg_col=int(ac.pass_dict[passg][1])
                            #Set seat matrix position to the passenger number
                            ac.seats[passg_row,passg_col]=passg
                            #Free the aisle
                            ac.aisle_q[row]=-1
                elif(ac.moveto_time_dict[passg]==0):
                    #If move hasn't been assgined to passenger
                    #Check passenger seat location
                    passg_row=int(ac.pass_dict[passg][0])
                    passg_col=int(ac.pass_dict[passg][1])
                    if(passg_row==row):
                        #If passenger at the row where his/her seat is,
                        #Designate move type as seat
                        ac.moveto_loc_dict[passg]="s"
                        #Check what type of seat: aisle, middle or window
                        #Depending upon seat type, designate when it is time to move
                        if(passg_col==0):
                            if(ac.seats[passg_row,1]!=-1 and ac.seats[passg_row,2]!=-1):
                                ac.moveto_time_dict[passg]=ac.time+ac.aisle_middle_mult*ac.time_dict[passg]
                            elif(ac.seats[passg_row,1]!=-1):
                                ac.moveto_time_dict[passg]=ac.time+ac.middle_mult*ac.time_dict[passg]                                   
                            elif(ac.seats[passg_row,2]!=-1):
                                ac.moveto_time_dict[passg]=ac.time+ac.aisle_mult*ac.time_dict[passg]
                            else:
                                ac.moveto_time_dict[passg]=ac.time+ac.empty_mult*ac.time_dict[passg]
                        elif(passg_col==5):
                            if(ac.seats[passg_row,4]!=-1 and ac.seats[passg_row,3]!=-1):
                                ac.moveto_time_dict[passg]=ac.time+ac.aisle_middle_mult*ac.time_dict[passg]
                            elif(ac.seats[passg_row,4]!=-1):
                                ac.moveto_time_dict[passg]=ac.time+ac.middle_mult*ac.time_dict[passg]                                   
                            elif(ac.seats[passg_row,3]!=-1):
                                ac.moveto_time_dict[passg]=ac.time+ac.aisle_mult*ac.time_dict[passg]
                            else:
                                ac.moveto_time_dict[passg]=ac.time+ac.empty_mult*ac.time_dict[passg]
                        elif(passg_col==1):
                            if(ac.seats[passg_row,2]!=-1):
                                ac.moveto_time_dict[passg]=ac.time+ac.aisle_mult*ac.time_dict[passg] 
                            else:
                                ac.moveto_time_dict[passg]=ac.time+ac.empty_mult*ac.time_dict[passg]
                        elif(passg_col==4):
                            if(ac.seats[passg_row,3]!=-1):
                                ac.moveto_time_dict[passg]=ac.time+ac.aisle_mult*ac.time_dict[passg]
                            else:
                                ac.moveto_time_dict[passg]=ac.time+ac.empty_mult*ac.time_dict[passg]
                        elif(passg_col==2 or passg_col==3):
                            ac.moveto_time_dict[passg]=ac.time+ac.empty_mult*ac.time_dict[passg]
                    elif(passg_row!=row):
                        #If passenger is not at the row where his/her seat is,
                        #Designate movement type as aisle
                        ac.moveto_loc_dict[passg]="a"
                        #Designate time to move
                        ac.moveto_time_dict[passg]=ac.time+ac.time_dict[passg]

        #Imaging
        if(n_iter%iters_per_snap==0 and ac.repeat==1):
            snap=ac.seats.copy()
            snap=np.insert(snap,3,ac.aisle_q,axis=1)
            ac.img_list.append(snap)
        


        #Iteration timekeeping
        ac.time+=time_step
        n_iter+=1
        pass_sum=np.sum(ac.seats)
    
    #Image final seat matrix
    if(ac.repeat==1):
        snap=ac.seats.copy()
        snap=np.insert(snap,3,ac.aisle_q,axis=1)
        ac.img_list.append(snap)

########################## USER INPUT BEGINS HERE ############################
#Define aircraft object    
ac=Aircraft()

#Define array to store times
time_arr=[]

#Define method of boarding (see AssignSeats function for options)
method="BTF"

#The number of times the simulation has to be repeated
ac.repeat=1
#Run the simulation
for i in range(ac.repeat):
    ac.Initialize737()
    ac.IssueSeatingOrder(method)
    BoardFlight(ac)
    time_arr.append(ac.time)

#Print the result
print("The time for method {0} is {1:.2f} +/ {2:.2f}".format(method,np.mean(time_arr),np.std(time_arr)))

#Animation
import matplotlib.animation as anim
from matplotlib import colors

#Only do the animation if the simulation is being run once
if(ac.repeat==1):
    #Define discrete color map  (blue for empty, gold for passenger)
    cmap = colors.ListedColormap(["darkslateblue", 'gold'])
    bounds=[-1,0,300]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    
    #Copy image list to a local variable
    img_list=ac.img_list
    #Repeate the final seat matrix 2 more times so that it is visible in animation for some time
    for i in range(2):
        img_list.append(img_list[-1])
    im=[]
    
    #Create figure and add subplot
    fig=plt.figure(figsize=(8,13))
    ax=fig.add_subplot(111)
    ax.set_xlabel("Rear",fontsize=20)
    ax.set_title("Passenger entry here",fontsize=20)
    
    #Use imshow on the images and create a nice looking plot
    for i in range(len(img_list)):
        image=ax.imshow(img_list[i],animated=True,cmap=cmap,norm=norm)
        ax.set_xticks(np.arange(-0.5,7.5,1))
        ax.set_yticks(np.arange(-0.5,23.5,1))
        ax.grid(color="k",linestyle="-",linewidth=2.5)  
        ax.xaxis.set_ticklabels([])
        ax.yaxis.set_ticklabels([])
        im.append([image])
    
    #Play and store the animation
    mov=anim.ArtistAnimation(fig,im,interval=180)
    plt.show()
    mov.save("Airplane_Boarding.png".format(method))

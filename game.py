import random
choice=["O", "X"]
while True:
    a=input(f"What will be your choice: O or X ? Enter O or X: ")
    if a.lower()=="0" or a.lower()=="o":
            print("You have chosen O")
            userin="O"
            computerin="X"
            break

    elif a.lower()=='x' or a.lower()=="*" :
         print("You have chosen X")
         userin="X"
         computerin="O"
         break  
    else:
        print("Wrong Input, please choose only any of O or X") 
        continue 
l=[" "," "," "," "," "," "," "," "," "]
corrl=[11,12,13,21,22,23,31,32,33]
occl=[]

def box():    
    print(f" {l[0]} | {l[1]} | {l[2]} ")
    print(f"---+---+---")
    print(f" {l[3]} | {l[4]} | {l[5]} ")
    print(f"---+---+---")
    print(f" {l[6]} | {l[7]} | {l[8]} ")

winvalue=0
def win():
     global winvalue
     for i in {0,3,6} :  
        if l[0+i]==userin and l[1+i]==userin and l[2+i]==userin:
            print(f"Congratulation! You have won the game")
            winvalue=1
            break
        if l[0+i]==computerin and l[1+i]==computerin and l[2+i]==computerin:
            print(f"Oh! You have lost the game")
            winvalue=1
            break

     for i in {0,1,2} :  
        if l[0+i]==userin and l[3+i]==userin and l[6+i]==userin:
            print(f"Congratulation! You have won the game")
            winvalue=1
            break

        if l[0+i]==computerin and l[3+i]==computerin and l[6+i]==computerin:
            print(f"Oh! You have lost the game")
            winvalue=1
            break


     if l[0]==userin and l[4]==userin and l[8]==userin:
            print(f"Congratulation! You have won the game")
            winvalue=1
     if l[2]==userin and l[4]==userin and l[6]==userin:
            print(f"Congratulation! You have won the game")
            winvalue=1
     if l[0]==computerin and l[4]==computerin and l[8]==computerin:
            print(f"Oh! You have lost the game")  
            winvalue=1     
     if l[2]==computerin and l[4]==computerin and l[6]==computerin:
            print(f"Oh! You have lost the game")  
            winvalue=1 



while len(corrl)>0:
    try:  
      x=int(input(f"Enter Vertical position from [1,3] where you want to place {userin}:"))
    except ValueError:
        print("Please enter a numaric value")
        continue
    if(x>3 or x<1):
        print("Out of range, Please enter within range")
        continue 

    try:   
       y=int(input(f"Enter Horizontal position from [1,3] where you want to place {userin}:"))
    except ValueError:
        print("Please enter a numaric value only")
        continue
    if(y>3 or y<1):
        print("Out of range, please enter within range")
        continue    
    
    for a in range(1,4):
       for b in range(1,4):
            if (x,y)==(a,b):
               t=int(str(x)+str(y))
               if occl.count(t)!=0:
                   print("Position already occupied")
                   continue
               else:
                   l[corrl.index(t)]=userin
                   occl.append(t)
                   print("Updated box, after you entered the value, is below:-")
                   box()
                   win()
                   if winvalue==1:
                       break

                   print("Now Computer is choosing.....")
                   print("Updated box, after computer entered the value, is below:-")
                   comp=random.choice(list(set(corrl).difference(set(occl))))
                   l[corrl.index(comp)]=computerin
                   occl.append(comp)
                   box()
                   win()
                   if winvalue==1:
                       break
       if winvalue==1:
              break  
    if winvalue==1:
              break            

else:
    print("Match Draw")

        



    
        
    
    



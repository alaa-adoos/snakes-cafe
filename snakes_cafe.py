

cafe_menu=[
{
"type":"appetizers",
"items":["wings","cookies","spring rolls"]
},
{
"type":"entrees",
"items":["salmon","steak","meat trando","A literal garden"]
},
{
"type":"desserts",
"items":["ice cream","cake","pie"]
},
{
"type":"drinks",
"items":["coffe","tea","unicorn tears"]
},

]



def show_menu():
    index=0

    print("**********************************")
    print("**    welcom to snakes cafe       ** ")
    print("**    please see our menu         ** ")
    print("**\t\t")
    print("**  to quit any time, type \"quit\" ** ")
    print("************************************ " )
    while index<(len(cafe_menu)):
          menu=cafe_menu[index]
          type=menu["type"]
          items=menu["items"]
          print(type)
          for i in  range(len(type)):
             print("_" ,end="")
          print("\n")   
          for i in items:
                 print(i)
          index+=1  
          print("\n")       

    order_now()

    
  
    

    
          
def order_now():
    print("****************************************")
    print("**    what whould you like to order?\t** ")
    print("**    to open your card,type \"card\"\t** ")
    print("****************************************")
 
    menu1=[]
    order=[]
    i=0

   
    while i<len(cafe_menu):
             menu=cafe_menu[i]
             items=menu["items"]
             for f in items:
               var=menu1.append(f)
 
             i+=1

  
  

    total=len(order)
    while True:
          massge=input("> ")
          
          if massge=="quit":

                 break
          elif massge=="cart":
            if total==0:
                print("************************")
                print("** your cart is empty !**")
                print("** go and pick a order  **" )
            
                
            print("************************")
            print("**\tCart list\t**")
            print("************************")
            print("**  Quantity  Product\t**")
            count={}
            for i in order:
                if not i in count:
                    count[i]=1
                else:
                    count[i]+=1
            for res in count:
                result=count[res]
                print(f"**\t{result}     {res}\t**")

           

        

                

            print("************************")





        
          else:
            result=list(filter(lambda x:x==massge,menu1))
            if len(result):
                      item=result[0]
                      order.append(item)
                      total=order.count(item)
                      if total==1:
                             print(f"** {total} order  of {item} have beeen added to your meal **")
                      else:
                          print(f"** {total} orders  of {item} have beeen added to your meal **")     
            else:
                 print("wrong choice ! ")

 



if __name__=="__main__":
  
        
    show_menu()
        




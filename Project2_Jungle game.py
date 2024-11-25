print("Jungle Game")
def final_call():
    x=int(input('''Do you want to play again \n Yes-1 No-2\n 1::'''))
    if(x==2):
        print("Thanks for playing")
    else:
        options()

def options():
        a=int(input("Press 1====>Left \n Press 2====>Right \n"))
        if(a==2):
            print("Again two otions")
            y=int(input("Press 1====>Left \n Press 2====>Right \n"))
            if(y==2):
                print("killed by soldier====>Game over")
                final_call()
            elif(y==1):
                print("Want to take strangers help???")
                z=int(input("Press 1====>Yes \n Press 2====>No \n"))
                if(z==1):
                   print("Stranger saves you=====>Congratuations U won")

                   final_call()
                else:
                   print("You trapped ====>Game over")
                   final_call()

        elif(a==1):
            b=int(input("Press 1====>turn Left \n Press 2====>turn Right \n"))
            if(b==1):
             print("You have fallen in a pit=====>Game over")
             final_call()
            else:
             print("You have been killed by an animal====>Game over")
             final_call()
    


options()


    

    




    

    




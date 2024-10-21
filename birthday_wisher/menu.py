import os

"""
This fuction is made to visualise the selection of a particular item in a list.
press "ENTER" to proceed pointing to the next item in the lis 
if you want to select the option that is indicated by the arrow press 'p' (pick) and then 'ENTER'
then the fuction will return the index of that item in a list
"""
def option_sys(options,title_msg):
    os.system("clear")
    index = 0
    ch = "---"
    while ch != "p": # looping the option for choosing if use has not pressed 'p' for pick
        print("\033[1m",title_msg,"\033[0;37m: \n")
        for i, opt in enumerate(options):
            
            if i != index: 
                print("  ",opt) #print two empty spaces before option chosen 
            else:
                print("\033[1;34m> \033[0;37m",opt) #print arrow before option chosen 
            
        ch = input("") #collect input to proceed choosing
        print(ch)

        if ch == "": #in enter is pressed point to next option 
            index += 1
            if index == len(options):
                index = 0

        os.system("clear")

    
    return index


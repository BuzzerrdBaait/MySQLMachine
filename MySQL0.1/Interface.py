import Datastream
from Datastream import subreddit_list,manage_submission, create_tables1,create_tables2
#import urlopener
import tkinter
from tkinter import *
import time
import winsound

root = tkinter.Tk()
root.geometry("700x300")
root.configure(bg = "indian red")
dispxhome=300
dispyhome=200

Python_subreddits = ['Python', 'LearnPython', 'Programming', 'PythonProgramming', 'DataScience', 'DataAnalysis', 'Matplotlib', 'Flask', 'Django']        #This is where you create columns of stuff you want to search
hacking_subreddits = ['netsec', 'hacking', 'howtohack', 'reverseengineering', 'pwned', 'sysadmin', 'ethicalhacking', 'crypto', 'networking']             #that way you can go make a sandwhich while it searches.
educationlist = ["YouShouldKnow", "everymanshouldknow", "changemyview", "howto", "Foodforthought", "lectures", "college", "GetStudying", "watchandlearn", "bulletjournal", "applyingtocollege", "todayIlearned"]
Most_Popular_Subreddits = ['AskReddit', 'funny', 'gaming', 'aww', 'todayilearned', 'science', 'worldnews', 'movies', 'Music']
business_subreddits = ['startup', 'entrepreneur', 'smallbusiness', 'marketing', 'sales', 'management', 'businessideas', 'finance']

spinbox_values = [Python_subreddits, hacking_subreddits,educationlist, Most_Popular_Subreddits, hacking_subreddits, business_subreddits]

entry_list=[]
tablename=[]


def ding(bpm):
     beat_len=60/bpm
     winsound.Beep(2000, int(beat_len * 500))              #This is a fun way to customize 
     winsound.Beep(1000, int(beat_len * 500))              #The dings. It makes it easier         
     winsound.Beep(1500, int(beat_len * 500))              #to change.
     winsound.Beep(2000, int(beat_len * 500))
                              
def whenEnterIsPressed(event,entry):                #Used for when I need to press enter
     entry_value = entry.get()                      #to insert variables.
     entry_list.append(entry_value)
     display_label.config(text=("List to mine ", entry_list))
     entryleng=len(entry_list)
     entry.delete(0,'end')

     ding(120)
     

     return()
     
def send_request():                     
     templist=[]
     depth=scale.get()
     #print(depth)


     for item in entry_list:                  #Searches and creates a tables of what
          templist.clear()                    #was searched.
          print("Searching ",item)
          templist.append(item)
          manage_submission(templist,depth)
          create_tables1()
          create_tables2()
          
          time.sleep(3)
     
     speed=100
     for dings in range(0,3):
          speed+=25
          
          ding(speed)

     return(entry_list.clear(),display_label.config(text=("List to mine ", entry_list)))

def add_subreddits():                            
     spinboxinputs=spinbox.get()
     
     spinboxadd = spinboxinputs.split()
     for item in spinboxadd:
          entry_list.append(item)
     display_label.config(text=("List to mine: ", entry_list))
     

def remove_subreddits():
     entrylen=len(entry_list)
     entry_list.pop(entrylen-1)
     display_label.config(text=("List to mine:{} ").format(entry_list))

          
input_label = tkinter.Label(root, text = "I want to search ",width=15,font="18", bg = "ivory")
display_label = tkinter.Label(root, text = "List to mine:",font=("Arial", 18, "bold"),wraplength=550, bg = "indianred")
help_label = tkinter.Label(root, text = "Type a subreddit to search\n and press <Enter> ", bg = "ivory")
help_label2 = tkinter.Label(root, text = "Build a list and \n send it to be searched.. ",width=25, bg = "ivory")
help_label3 = tkinter.Label(root, text = "Adjust the number of posts \n to be searched---> ",width=25, bg = "ivory")
button = tkinter.Button(text="fetch info",font="16",bg="ivory",width=10, command=send_request)
button2 = tkinter.Button(text="Include spinbox in search.",font="16",width=21, bg="ivory", command=add_subreddits)
delete_button=tkinter.Button(text="Remove item",font="16",width=10, bg="ivory",command=remove_subreddits)

entry = tkinter.Entry(root, width=20, bd=3,bg="ivory", relief="sunken", font="16")
entry.bind("<Return>", lambda event, entry=entry: whenEnterIsPressed(event, entry))

frame = Frame(root)

frame2=Frame(root)


spinbox = Spinbox(frame2, values=spinbox_values,width=35, font="18", bg="ivory")

scale = Scale(frame, orient=VERTICAL,bg="ivory")
scale.set(10)


help_label.grid(column=0,row=0,pady=5,padx=2)
help_label2.grid(column=1,row=0,pady=5,padx=2)
help_label3.grid(columnspan=2,column=2,row=0,pady=5,padx=2)
input_label.grid(column=0,row=1, padx=2)

entry.grid(column=1,row=1,padx=2)
frame2.grid(columnspan=2,row=2,column=0,padx=2)
spinbox.grid(columnspan=2,row=2,column=0,padx=2,pady=3)
display_label.grid(column=0,row=3,rowspan=2,columnspan=5)
delete_button.grid(column=2,row=1,sticky="w")
button.grid(column=3, row=1,sticky="w")
button2.grid(columnspan=2,column=2,row=2,sticky="w")

frame.grid(column=4,rowspan=3,row=0,sticky="s")
scale.grid(column=4,rowspan=3,row=0,sticky="s")



root.mainloop()
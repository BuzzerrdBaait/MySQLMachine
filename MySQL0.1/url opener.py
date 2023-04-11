from MySQLMachine import db
import tkinter
from tkinter import ttk,OptionMenu,StringVar,Frame
import webbrowser

root = tkinter.Tk()
tablesearch=[]
root.geometry("400x400")
root.configure(bg = "indian red")


tableselection=[]
options = []
options2=["Open Urls","Show Table","cmd3"]
templist=[]
tablesinfo=[]

def callquery():
    query=sqlentry.get()
    print(query)
    sqlentry.delete(0,'end')

def clear_all():
    print("trying to clear boss")
    Textwidget.delete(1.0, 'end')
    sqlentry.delete(0,'end')
    
def open_urls(tblname,limit):
    query=("SELECT url_5 FROM {} ORDER BY score_3 DESC LIMIT {};").format(tblname,limit)# UNION SELECT url_5 FROM reddit_4 WHERE score_3 > (select avg(score_3) from reddit) Union SELECT url_5 FROM reddit_2 WHERE score_3 > (select avg(score_3) from reddit_2);")
    response=(db.query(query))
    print(query)
    print(response)
    for item in response:
        for url in item:
            url=str(url)
        
            print(url)
            webbrowser.open_new_tab(url)

def pop_tables():
    query=("SHOW TABLES;")
    response=db.query(query)

    for item in response:
        for tablesname in response:
            for tablename in tablesname:
                options.append(tablename)


pop_tables()                                      #Populates the tables selector


def show_columns(tablesname):
    Textwidget.delete(1.0,'end')
    query=("DESCRIBE {}").format(tablesname)
    response=db.query(query)
    templist=[]
    
    for item in response:
        templist.append(item[0])
    
    Textwidget.insert(1.0,templist)
    return(tablesname,templist)

def show_table(table,limit):
    tablesinfo.clear()
    Textwidget.delete(1.0,'end')
    query=("SELECT * FROM {} ORDER BY score_3 DESC LIMIT {};").format(table, limit)
    response=db.query(query)
    for item in response:
        for i in range(0,(len(item))):
            tablesinfo.append(item[i])
            Textwidget.insert(1.0,item[i])
            Textwidget.insert(1.0,"   ")
        print("NEW ROW \n")
        #tablesinfo.append(item[0])

        #(item[0])
        #print(item[1])
        #print(item[2])
        #print(item[3])
        #print(item[4])
        #print(item[5])
        #url=(item[6])
        #print(url)
        #print(item[7])
        #print(url)
    return()

        #Textwidget.insert(1.0,item[5])

selectedtablelist=[]

def optionMenuSelected(value):
    selectedtablelist.clear()
    selectedtable=(value)
    show_columns(selectedtable)
    optionMenu2.update()
    selectedtablelist.append(selectedtable)
    #print(selectedtable,templist)

def cmd3():
    print("command 3")


def optionmenu2selected(value):
    selectedtable=selectedtablelist[0]
    #print(value)
    #print(options2[0])        

    if value == options2[0]:
        open_urls(selectedtable,limit=20)                   #ADD Functions here
    elif value == options2[1]:
        show_table(selectedtable,limit=5)
    elif value == options2[2]:
        cmd3()

    
Welcome = tkinter.Label(root, text = "Custom SQL queries",width=25, bg = "ivory")
sqlentry= tkinter.Entry(root,width=30, bg="ivory")
Textwidget=tkinter.Text(root, bg="ivory", fg="black", height=10, width=100, font="10")
clear_button=tkinter.Button(root,text="Clear", command=clear_all)
#test_button=tkinter.Button(root,text="Perform action", command=update_text_widg)

#sqlentry.bind("<Return>", lambda event, entry=sqlentry: callquery())


frame=Frame(root)

option = StringVar(frame)
option.set("Table Menu")

optionMenu = OptionMenu(frame, option, *options, command=optionMenuSelected)


optionMenu.pack()
#frame=Frame(root)

option2 = StringVar(frame)
option2.set("CMD Selection")



optionMenu2 = OptionMenu(frame, option2, *options2, command=optionmenu2selected)

frame.pack()
optionMenu2.pack()






#optionMenu = OptionMenu(frame,option, "Option 1", "Option 2", "Option 3")
#frame.pack()
#optionMenu.pack()

#Welcome.pack()
#sqlentry.pack()
Textwidget.pack()
clear_button.pack()
#test_button.pack()





#show_db()


root.mainloop()

  "MySQLMachine"
  
  is a reddit bot that mines data and stores it in a database. Something special about this bot, is that it checks the datatypes of the information to be stored, and the number of different items to be stored. Next, it will create a unique table with the columns named appropriately, and store the information into the newly created table. I had to do it this way because of the frequency of large amounts of data being stored. I have been able to mine subreddits in entirety with this bot.

Also, there is the url opener GUI that allows you to search your database and open the top x amount of urls.                                    

I would reccomend downloading MySQL workbench (GUI for database). Here is the link for MySQL Workbench ---> https://dev.mysql.com/downloads/workbench/                 

_.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__
Getting Started:.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.

  To get started, you need to have a MySQL Database, Python installed, and some basic understanding of SQL.                                                

The API used to connect to Reddit is called praw. You will have to register with OAuth to gain access to Reddit's API. Below are some useful links to documentation and the link to Oauth incase you dont want to read the guide.

(Docs to praw) ---> https://praw.readthedocs.io/en/stable/ ,
(guide)        --->  https://github.com/reddit-archive/reddit/wiki/OAuth2  ,
(register here)---> https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2Fprefs%2Fapps ,
(MySQL Workbench download) *Optional but highly recommended*->  https://dev.mysql.com/downloads/workbench/


_.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-._

What next?

  After you have created a database, and registered with Oauth. You will have to fill out your Oauth credentials. The code will look like this..
  See lines 23-28 in Datastream.py
  
  import praw

reddit = praw.Reddit(
    client_id="my client id",
    client_secret="my client secret",
    password="my password",
    user_agent="my user agent",
    username="my username",
)

You will need to create a connection in MySQL. I use MySQL workbench and it is on the home dashboard of MySQL notated by a (+) symbol. "To add a connection".
Next navigate to lines 53-56 of MySQLMachine0.1. This is where you will fill in your databases authentication info such as username, password, and ip_address. It will look like this...


dbname='newdatabase'                #   Enter your database's name/"schema"
host='localhost'                    #   'localhost or ip address the db is hosted @
user='USERNAME'                     #   Database 'User name' 
password='PASSWORD123!@#$q'         #   'Password'
                                    #   I would store these in another file but they are here to demonstrate that this is where your db info goes.

_.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-._

After filling in your information. Open Interface.py and confirm you are connecting to your database. The IDE's cmd line will print 'connected to database successfully' or an error. If you are having errors you may want to check to make sure your database is running. Within your workbench you can go to server, server status. If it is not connected, use the Database tab to show the option Database/Connect Database/Manage connections. That will probably be a good place to look if you are having issues.

If you want to make new users, go to the Administration tab on middle-far-left side of the workbench. There are plenty of useful options there to help you on your way! 
Have Fun!

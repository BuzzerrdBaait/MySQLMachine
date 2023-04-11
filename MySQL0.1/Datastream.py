from MySQLMachine import create_table_if_not_exists,insert_into_table_w_a_list,SQLDatabase,dbname

import datetime
import praw
import re

#currentcolnames=[]
#tableslist=[]
#currenttable=[]
#searchlist=[]
data_to_be_stored=[]
data_to_be_stored2=[]
currenttable=[]

currentcolnames=[]
tableslist=[]


searchlist=[]
commentinfo=[]


subreddit_list=[]
reddit = praw.Reddit(
        client_id="CLIENT ID",                 #Reddit info would go here
        client_secret="CLEINT SECRET",          #API KEY
        password="PASSWORD",
        user_agent="LMGTFY (by u/REDDIT USERNAME GOES HERE)",
        username="REDDIT USERNAME",)
               
def cut_off_string(string):
        if len(string) > 250:
            return string[:250]
        else:
            return string
        
def remove_emojis(string):
        emoji_pattern = re.compile("["                   #These represent the unicode sets we
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"  
                               u"\U000024C2-\U0001F251"
                               u"\u2700-\U0001F9FF"

                               "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', string)


  
    
def manage_submission(subreddit_list,depth):
        
        for subreddit in subreddit_list:
            
            
            posts=reddit.subreddit(subreddit).top(limit=depth)
            for post in posts:
                
                
                
                submission = reddit.submission(id=post.id)
                
                url=str(submission.url)
                url=(cut_off_string(url))
                
                author=str(submission.author)
                
                title=str(submission.title)
                title=cut_off_string(title)
                title= title.replace("'", "")
                title=remove_emojis(title)
                
                score=int(submission.score)##############<_______Turn to an int after I get this working
                
                id=(submission.id)   #
                
                submission.created_utc
                readable_date_time_for_post = datetime.datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')
                str(readable_date_time_for_post)
                
                data_to_be_stored.append(subreddit)
                data_to_be_stored.append(title)
                data_to_be_stored.append(score)
                data_to_be_stored.append(author) 
                data_to_be_stored.append(url)
                data_to_be_stored.append(readable_date_time_for_post)
                data_to_be_stored.append(id)
                submission.comments.replace_more(limit=None)

                for comment in submission.comments.list():

                    
                    comment_author=str(comment.author)
              
                    comment_body=str(comment.body)
                    comment_body=remove_emojis(comment_body)
                    comment_body= comment_body.replace("'", "")
                    comment_body=cut_off_string(comment_body)
                   
                    #comment.controversiality,
                    #comment.created_utc,
                    #comment.distinguished,
                    #comment.edited,
                    comment_id=(comment.id)
                    #comment.is_submitter,
                    #comment.link_id,
                    #comment.parent_id,
                    #comment.permalink,
                    comment_score=(comment.score)
                    comment_score=int(comment_score)
                    readable_date_time = datetime.datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S')
                    

                    data_to_be_stored2.append(subreddit)
                    data_to_be_stored2.append(title)
                    data_to_be_stored2.append(comment_score)
                    data_to_be_stored2.append(comment_author)
                    data_to_be_stored2.append(comment_body)
                    data_to_be_stored2.append(url)
                    data_to_be_stored2.append(readable_date_time)
                    data_to_be_stored2.append(comment_id)
                    

      
            return()
        return()

            
          
               
#manage_submission(subreddit_list)
#create_tables1()
parentname=["subreddit","Post_name","score","author","url", "date", "postid"]      #Here is where you can insert your column names. Once set you dont have to keep renaming columns.
parentname2=["subreddit", "Post_name","comment_score","author","Comment","url","date","comment_id"]  #Create table reads these strings to determine what the columns name will be.
                                                                                                     #The column is the type of information you will be extracting. It does not have    
def create_tables1():                                                                                #have to be reddit.
      
      
      create_table_if_not_exists(data_to_be_stored,currenttable,currentcolnames,parentname,rowlength=7)   #<---This is how you can make a call. and I put it within 
      insert_into_table_w_a_list(dbname, currenttable, currentcolnames,data_to_be_stored)                 #another function so we dont have to import variables when
      data_to_be_stored.clear()                                                                            #calling froma nother file.
      currenttable.clear()
      currentcolnames.clear()
      

def create_tables2():
      current_table=[]
      currentcolnames=[]
      create_table_if_not_exists(data_to_be_stored2,currenttable,currentcolnames,parentname2,rowlength=8)
      insert_into_table_w_a_list(dbname, currenttable, currentcolnames,data_to_be_stored2)
      data_to_be_stored2.clear()
      currenttable.clear()
      currentcolnames.clear()






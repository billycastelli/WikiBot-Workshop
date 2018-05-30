
import praw
import wikipedia as w

reddit = praw.Reddit(client_id = 'x',
                     client_secret = 'x',
                     username = 'TheZotBot',
                     password = 'x',
                     user_agent = 'web:WikiBot:1.0 (by /u/TheZotBot)')




subreddit = reddit.subreddit("all")

posts = subreddit.new(limit = 5)

reply = ""
    


for comment in subreddit.stream.comments():
    if 'wikipedia.org' in comment.body:
        whole_comment = comment.body.split()
        for word in whole_comment:
            if 'wikipedia.org' in word:
                link = word
                print("URL: ", link)
                link = link.split('/')
                keyword = link[-1].strip(',;:]-')
                print("KEYWORD: ", keyword)
                try:
                    reply = "\n" + w.summary(keyword, 3)
                    comment.reply("**Here is a summary of this Wikipedia Article:**\n" + reply)
                except w.exceptions.DisambiguationError as e:
                    reply = "\n", w.summary(e.options[0])
                    comment.reply("**Here is a summary of this Wikipedia Article:**\n" + reply)
                except:
                    pass
                
    if "uciWikiBot:" in comment.body:
        keyword = comment.body.split()[-1]
        reply = w.summary(keyword, 3)
        comment.reply("**Here is a summary of this Wikipedia Article:**\n" + reply)

                
                        





 




'''
Functions of the bot...

to start...   goes through comments of 5 recent posts
after... streams comments



-Give wikipedia summaries upon request
    wikipedia.summary(name, sentences = 4)
    
try:
	w.summary('tit')
except w.exceptions.DisambiguationError as e:
	w.summary(e.options[0])
	#what about other errors? just ignore



    
-Give summaries of wikipedia links
"https://en.m.wikipedia.org/wiki/Bang_Khun_Thian_District?wprov=sfla1"
get bang_khun_thian_district from this





'''

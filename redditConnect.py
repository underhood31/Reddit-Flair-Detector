import praw
from pymongo import MongoClient
import datetime as dt

def GetSpecificData(category_object, category_name, ):
    try:
        Category=category_name
        Flair = str(category_object.link_flair_text.strip())
        Score = category_object.score
        Title = category_object.title
        Body = category_object.selftext
        Link = category_object.url
        NoOfComments = category_object.num_comments
        num=0
        Comments=[]
        for c in category_object.comments:
            if num>9:
                break

            try:
                
                Comments.append(c.body)
                num+=1
            except:
                Comments.append("")
                num+=1
        TimeStamp = dt.datetime.fromtimestamp(category_object.created) + dt.timedelta(hours=5,minutes=30)
        Username = str(category_object.author)
        
        allDetails = {
            "Category":Category,
            "Flair":Flair,
            "Score":Score,
            "Title":Title,
            "Body":Body,
            "Link":Link,
            "NoOfComments":NoOfComments,
            "Comments": Comments,
            "TimeStamp":TimeStamp,
            "Username":Username
        }
        return allDetails
        
    except:
        return None

# DB configurations
client = MongoClient('localhost', 27017)
db = client['reddit_data']
Test = db['test']
Train = db['train']

#PRAW configurations
cred= praw.Reddit(client_id='', client_secret='', user_agent='Flair_Detector')
page = cred.subreddit('india')
top = page.top(limit=1000)
new = page.new(limit=1000)
controversial = page.controversial(limit=1000)
rising = page.rising(limit=1000)
hot = page.hot(limit=1000)

threshhold = 80 #Number of entries in train database /1000

print("\n----------Top----------\n")
count=0
for post in top:
    
    Data = GetSpecificData(post, "Top")
    if Data==None:
        print("Error; skipped")
        count+=1
        continue
    print("good",count)
    count+=1;
    if count>threshhold: #For test dataset
        Test.insert_one(Data)
    else:       #For train dataset
        Train.insert_one(Data)


print(count)


print("\n----------New----------\n")
count=0
for post in new:
    Data = GetSpecificData(post, "New")
    if Data==None:
        print("Error; skipped")
        count+=1
        continue
    print("good",count)
    count+=1;
    if count>threshhold: #For test dataset
        Test.insert_one(Data)
    else:       #For train dataset
        Train.insert_one(Data)

print(count)

print("\n----------Controversial----------\n")
count=0
for post in controversial:
    Data = GetSpecificData(post, "Controversial")
    if Data==None:
        print("Error; skipped")
        count+=1
        continue
    print("good",count)
    count+=1;
    if count>threshhold: #For test dataset
        Test.insert_one(Data)
    else:       #For train dataset
        Train.insert_one(Data)
print(count)

print("\n----------Rising----------\n")
count=0
for post in rising:
    Data = GetSpecificData(post, "Rising")
    if Data==None:
        print("Error; skipped")
        count+=1
        continue
    print("good",count)
    count+=1;
    if count>threshhold: #For test dataset
        Test.insert_one(Data)
    else:       #For train dataset
        Train.insert_one(Data)
print(count)

print("\n----------Hot----------\n")
count=0
for post in hot:
    Data = GetSpecificData(post, "Hot")
    if Data==None:
        print("Error; skipped")
        count+=1
        continue
    print("good",count)
    count+=1;
    if count>threshhold: #For test dataset
        Test.insert_one(Data)
    else:       #For train dataset
        Train.insert_one(Data)
print(count)

print("\n---------------DONE :)-------------------")

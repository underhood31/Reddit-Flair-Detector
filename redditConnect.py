import praw
import json

import datetime as dt

cred= praw.Reddit(client_id='HkBGGe_k4LXW9w', client_secret='yZQZeViIt5FDuLZSC3nxnkJFVto', user_agent='Flair_Detector')

            
page = cred.subreddit('india')

allDetails_train = {
    "Category":[],
    "Flair":[],
    "Score":[],
    "Title":[],
    "Body":[],
    "Link":[],
    "NoOfComments":[],
    "Comment1":[],
    "Comment2":[],
    "Comment3":[],
    "Comment4":[],
    "Comment5":[],
    "Comment6":[],
    "Comment7":[],
    "Comment8":[],
    "Comment9":[],
    "Comment10":[],
    "TimeStamp":[],
    "Username":[]

}
allDetails_test = {
    "Category":[],
    "Flair":[],
    "Score":[],
    "Title":[],
    "Body":[],
    "Link":[],
    "NoOfComments":[],
    "Comment1":[],
    "Comment2":[],
    "Comment3":[],
    "Comment4":[],
    "Comment5":[],
    "Comment6":[],
    "Comment7":[],
    "Comment8":[],
    "Comment9":[],
    "Comment10":[],
    "TimeStamp":[],
    "Username":[]

}

top = page.top(limit=5)
# new = page.new(limit=1000)
# controversial = page.controversial(limit=1000)
# rising = page.rising(limit=1000)
# hot = page.hot(limit=1000)

print("\n----------Top----------\n")
count=0
for post in top:
    if count<2:
        try:
            flair = str(post.link_flair_text.strip())
            allDetails_train["Category"].append("Top")
            allDetails_train["Flair"].append(flair)
            allDetails_train["Score"].append(post.score)
            allDetails_train["Title"].append(post.title)
            allDetails_train["Body"].append(post.selftext)
            allDetails_train["Link"].append(post.url)
            allDetails_train["NoOfComments"].append(post.num_comments)
            num=1
            for c in post.comments:
                if num>10:
                    break

                try:
                    commName = "Comment" + str(num)
                    allDetails_train[commName].append(c.body)
                    num+=1
                except:
                    commName = "Comment" + str(num)
                    allDetails_train[commName].append("")
                    num+=1
            allDetails_train["TimeStamp"].append(str(dt.datetime.fromtimestamp(post.created)))
            allDetails_train["Username"].append(str(post.author))
            count+=1
            print("good")
        except:
            count+=1
            print("error; skipped")
    else:
        try:
            flair = str(post.link_flair_text.strip())
            allDetails_test["Category"].append("Top")
            allDetails_test["Flair"].append(flair)
            allDetails_test["Score"].append(post.score)
            allDetails_test["Title"].append(post.title)
            allDetails_test["Body"].append(post.selftext)
            allDetails_test["Link"].append(post.url)
            allDetails_test["NoOfComments"].append(post.num_comments)
            num=1
            for c in post.comments:
                if num>10:
                    break

                try:
                    commName = "Comment" + str(num)
                    allDetails_test[commName].append(c.body)
                    num+=1
                except:
                    commName = "Comment" + str(num)
                    allDetails_test[commName].append("")
                    num+=1
            allDetails_test["TimeStamp"].append(str(dt.datetime.fromtimestamp(post.created)))
            allDetails_test["Username"].append(str(post.author))
            print("good")
            count+=1
        except:
            print("error; skipped")
            count+=1

print(count)
with open('test.json', 'w') as fp:
    json.dump(allDetails_test, fp)
with open('train.json', 'w') as fp:
    json.dump(allDetails_train, fp)
# print("\n----------New----------\n")
# for post in new:
#     try:
#         print(post.title, " by ", post.link_flair_text.strip())
#     except:
#         print("error")

# print("\n----------Controversial----------\n")
# for post in controversial:
#     try:
#         print(post.title, " by ", post.link_flair_text.strip())
#     except:
#         print("error")

# print("\n----------Rising----------\n")
# for post in rising:
#     try:
#         print(post.title, " by ", post.link_flair_text.strip())
#     except:
#         print("error")

# print("\n----------Hot----------\n")
# for post in hot:
#     try:
#         print(post.title, " by ", post.link_flair_text.strip())
#     except:
#         print("error")

# top = page.top(limit=1)
# for i in top:
#     print("---------------")
#     # print(i.title,"\n",i.score,"\n",i.num_comments,"\n",i.url,"\n",dt.datetime.fromtimestamp(i.created),"\n",i.selftext)
#     print(i.author);
# for i in top:
#     l=0
#     for j in i.comments:
#         if l>100 :
#             break
#         # if isinstance(j, MoreComments):
#         #     continue

#         print(j.body)
#         l+=1
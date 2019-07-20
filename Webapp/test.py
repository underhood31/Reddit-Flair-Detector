import pandas as pd
from collections import Counter
import string
# flairToInt = {
#         "Other": -1,
#         "AMA":0,
#         "AMA Concluded":0,
#         "Casual AMA":0,
#         "AskIndia":1,
#         "Business/Finance":2,
#         "Demonetization":3,
#         "Entertainment":4,
#         "Food":5,
#         "Lifehacks":6,
#         "Misleading":7,
#         "Non-Political":8,
#         "Photography":9,
#         "Policy":10,
#         "Policy & Economy":10,
#         "Policy/Economy":10,
#         "Politics":11,
#         "Politics -- Source in comments": 11,
#         "Politics [OLD]":11,
#         "Scheduled":12,
#         "Science & Technology":13,
#         "Science/Technology":13,
#         "Sports":14,
#         "[R]eddiquette":15,
#         "r/all":16,
#         "/r/all":16
#     }
def initWith(num,times):
    toRet=[]
    for i in range(times):
        toRet.append(num)
    return toRet

def CategoryVsTime():
    others=initWith(0,24)
    others.insert(0,"Others")
    ama=initWith(0,24)
    ama.insert(0,"AMA")
    askIndia=initWith(0,24)
    askIndia.insert(0,"AskIndia")
    business=initWith(0,24)
    business.insert(0,"Business/Finance")
    demonetization=initWith(0,24)
    demonetization.insert(0,"Demonetization")
    entertainment=initWith(0,24)
    entertainment.insert(0,"Entertainment")
    food=initWith(0,24)
    food.insert(0,"Food")
    lifehacks=initWith(0,24)
    lifehacks.insert(0,"LifeHacks")
    misleading=initWith(0,24)
    misleading.insert(0,"Misleading")
    nonp=initWith(0,24)
    nonp.insert(0,"Non-Political")
    photo=initWith(0,24)
    photo.insert(0,"Photography")
    policy=initWith(0,24)
    policy.insert(0,"Policy & economy")
    politics=initWith(0,24)
    politics.insert(0,"Politics")
    scheduled=initWith(0,24)
    scheduled.insert(0,"Scheduled")
    scTech=initWith(0,24)
    scTech.insert(0,"Science & Technology")
    sports=initWith(0,24)
    sports.insert(0,"Sports")
    red=initWith(0,24)
    red.insert(0,"[R]eddiquette")
    rAll=initWith(0,24)
    rAll.insert(0,"r/all")
    
    allDataFrame = pd.read_csv("Data/all.csv", delimiter="\t")
    hour = list(allDataFrame['Hour'])
    category = list(allDataFrame['Flair'])
    for i in range(len(hour)):
        if category[i]==-1:
            others[int(hour[i])+1]+=1
        elif category[i]==0:
            ama[int(hour[i])+1]+=1
        elif category[i]==1:
            askIndia[int(hour[i])+1]+=1
        elif category[i]==2:
            business[int(hour[i])+1]+=1
        elif category[i]==3:
            demonetization[int(hour[i])+1]+=1
        elif category[i]==4:
            entertainment[int(hour[i])+1]+=1
        elif category[i]==5:
            food[int(hour[i])+1]+=1
        elif category[i]==6:
            lifehacks[int(hour[i])+1]+=1
        elif category[i]==7:
            misleading[int(hour[i])+1]+=1
        elif category[i]==8:
            nonp[int(hour[i])+1]+=1
        elif category[i]==9:
            photo[int(hour[i])+1]+=1
        elif category[i]==10:
            policy[int(hour[i])+1]+=1
        elif category[i]==11:
            politics[int(hour[i])+1]+=1
        elif category[i]==12:
            scheduled[int(hour[i])+1]+=1
        elif category[i]==13:
            scTech[int(hour[i])+1]+=1
        elif category[i]==14:
            sports[int(hour[i])+1]+=1
        elif category[i]==15:
            red[int(hour[i])+1]+=1
        elif category[i]==16:
            rAll[int(hour[i])+1]+=1
        
    return others,ama,askIndia,business,demonetization,entertainment,food,lifehacks,misleading,nonp,photo,policy,politics,scheduled,scTech,sports,red,rAll
def getDataByHeader(header):
    allDataFrame = pd.read_csv("Data/all.csv", delimiter="\t")
    col = list(allDataFrame[header])
    category = list(allDataFrame['Flair'])
    toret=initWith(0,18)
    for i in range(len(col)):
        if(category[i]!=-1):
            toret[category[i]]+=col[i]
    return toret
def getMost(flair):
    allDataFrame = pd.read_csv("Data/all.csv", delimiter="\t")
    category = list(allDataFrame['Flair'])
    col = list(allDataFrame['Text'])
    s=''
    for i in range(len(col)):
        if(category[i]==flair):
            s += (" " + col[i])
    
    toRem=["with", "that", "there", "their"]
    for c in toRem:
        s= s.replace(c," ")
    
    # s=re.sub(r'\b\w{,3}\b', '', s)
    s = ''.join([w+" " for w in s.split() if len(w)>3])
    # print(s)
    s=s.split()
    counter = Counter(s)
    return counter.most_common(4) 
others,ama,askIndia,business,demonetization,entertainment,food,lifehacks,misleading,nonp,photo,policy,politics,scheduled,scTech,sports,red,rAll = CategoryVsTime()
likes = getDataByHeader("NumComments")
for i in range(-1,17):
    s = getMost(i)
    print(s)
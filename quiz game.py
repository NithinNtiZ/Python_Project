#from question import question 
#from question1 import question 


#list of questions 
ques= [
    "what is your name ?\na)nithin\nb)nithin1\nc)babu\nd)nithin babu\n",
    "what is your age ?\na)10\nb)29\nc)50\nd)100\n",
    "where are you from ?\na)trivandrum\nb)kollam\nc)earth\nd)milkyway\n"
]

#class declaration
class question:
    def __init__(self, quest, ans):
        self.quest=quest
        self.ans=ans

#object declaration
x = [

    question(ques[0], "d"),
    question(ques[1], "b"),
    question(ques[2], "a"),
    
]


score=0
for que in x:
    answer= input (que.quest)
    if answer==que.ans:
        score+=1

print ("your score "+ str(score) +"/" + str(len(x)) )

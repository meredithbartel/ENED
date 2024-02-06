# Activity Python 1: Task 2
# File: ACT_Python_HeaderTemplate_Team204_Bartelmj.py
# Date: 1/1/24
# By: Meredith Bartel
# Section: 10.1
# Team: 2165
#
# ELECTRONIC SIGNATURE
# Meredith Bartel
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# gives you random question for the amount of questions you want to put in
import random


with open('TeamQuestion.txt','r') as mydata:
    data = mydata.readlines()


questionstoask = []


numquestions = int(input('How many questions do you want to extract? '))

while len(questionstoask) < numquestions and len(questionstoask) < len(data):
  
    lineselect = random.randint(0, len(data) - 1)
    question = data[lineselect].strip()
    
  
    print(question)
    keep = input("Keep this question? Enter (y or n): ").lower()
        
    if keep == 'y':
        questionstoask.append(question)
      
        del data[lineselect]


with open('QuestionsToAsk.txt', 'w') as rfile:
    for question in questionstoask:
        rfile.write(question + '\n')

print(f"{len(questionstoask)} Questions stored to 'QuestionsToAsk.txt'")


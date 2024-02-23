
"""
Created on Thu Jan 30 11:54:35 2020

@author: 남준녕
"""
import random

file = open("D:\lecture\\movie review\\new_data_review\\mixing\\baseline_new/review_history_trusted_comment_sympathy_noempty.txt",  "r",encoding='utf-8')
file1 = open("D:\lecture\\movie review\\new_data_review\\mixing\\baseline_new/review_history_untrusted_comment_sympathy_noempty.txt",  "r",encoding='utf-8')
file3 = open("D:\lecture\\movie review\\new_data_review\\mixing\\baseline_new/review_history_trusted_comment_sympathy_noempty.txt",  "r",encoding='utf-8')
file4 = open("D:\lecture\\movie review\\new_data_review\\mixing\\baseline_new/review_history_untrusted_comment_sympathy_noempty.txt",  "r",encoding='utf-8')
f = open("D:\lecture\\movie review\\new_data_review\\mixing\\baseline_new/test_comment_trust.txt",  "w",encoding='utf-8')
f1 = open("D:\lecture\\movie review\\new_data_review\\mixing\\baseline_new/test_comment_untrust.txt",  "w",encoding='utf-8')
f2 = open("D:\lecture\\movie review\\new_data_review\\mixing\\baseline_new/scaling_comment_trust.txt",  "w",encoding='utf-8')
f3 = open("D:\lecture\\movie review\\new_data_review\\mixing\\baseline_new/scaling_comment_untrust.txt",  "w",encoding='utf-8')
random_num = []
random_num1 = []
random_num2 = []
random_num3=[]

trust_num =39489
untrust_num =22815
scaling =4000
test = 1000

num = random.randrange(0,trust_num)

for i in range(scaling):
    while (num in random_num)  :
        num = random.randrange(0,trust_num)
    random_num.append(num)

random_num.sort()    
    

count=1
while (count<=trust_num):
    line = file.readline()
    if count-1 in random_num:
        f2.write(line)
    count+=1
f2.close()

num1 = random.randrange(0,untrust_num)

for i in range(scaling):
    while (num1 in random_num1)  :
        num1 = random.randrange(0,untrust_num)
    random_num1.append(num1)

random_num1.sort()    
    

count=1
while (count<=untrust_num):
    line = file1.readline()
    if count-1 in random_num1:
        f3.write(line)
    count+=1
f3.close()

num2 = random.randrange(0,trust_num)

for i in range(test):
    while (num2 in random_num2)  :
        num2 = random.randrange(0,trust_num)
    random_num2.append(num2)

random_num2.sort()    
    

count=1
while (count<=trust_num):
    line = file3.readline()
    if count-1 in random_num2:
        f.write(line)
    count+=1
f.close()

num3 = random.randrange(0,untrust_num)

for i in range(test):
    while (num3 in random_num3)  :
        num3 = random.randrange(0,untrust_num)
    random_num3.append(num3)

random_num3.sort()    
    

count=1
while (count<=untrust_num):
    line = file4.readline()
    if count-1 in random_num3:
        f1.write(line)
    count+=1
f1.close()          
    
     
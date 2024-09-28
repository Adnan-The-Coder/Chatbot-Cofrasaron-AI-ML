a = [1,2]
b = [3,4]
per_day_study_compulsory = ['MATHEMATICS','PHYSICS'] # MATH and PHYSICS complete time and CS 1 hr and english 1 hr and next day chemistry 2 hr 
per_study_left = ["CHEMISTRY","ENGLISH","COMPUTER SCIENCE"]
        

count = 1
for i in range(3):  
    for (c,d) in zip(per_day_study_compulsory,per_study_left):
        print('Day',count,c,'and',d)
        count += 1
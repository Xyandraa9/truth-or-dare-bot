from random import randint

def file_rand_return():
    count = 0
    with open('question_file.txt','r+') as question:
        for i in question:
            count+=1
        question.seek(0)
        rand = randint(0,count)
        check = 0
        for i in question:
            check +=1
            q = i.split('Q.')
            x = q[1].split("\n")
            if(check == rand):
                return x[0]
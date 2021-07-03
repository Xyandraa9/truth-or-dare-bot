from random import randint

# question = ["What's a weird food combination that you like?"
# ,"What song u like the melody but dislike the lyrics",
# "What's the weirdest butterfly effect that's happened in your life?",
# "If you were to kill your anime kin from any anime who would it be?",
# "Which anime/movie/book character would you like to live as for 24 hours?",
# "If you were to live any antagonists life for a day, who would it be and why?",
# "If you could change anything in the world, what would it be?",
# "Which movie character do you relate to the most?",
# "Who is your favorite comfort character, and why?",
# "Who's your favorite fictional character and why?",
# "If you had to choose to spectate your enemy's life or best friend's life, who would you choose?(the enemy and/or best friend role could or could not be mutual to them)",
# " What music is so last year but you still like to listen to?",
# "What show/movie is so badly written, but you would watch over and over again anyway?",
# "",
# ""]

# def question_return():
#     return question

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
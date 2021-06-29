import random

count = 0
with open('question_file.txt','r+') as question:
    for i in question:
        count+=1
    question.seek(0)
    rand = random.randint(0,count)
    check = 0
    for i in question:
        check +=1
        q = i.split('Q.')
        x = q[1].split("\n")
        if(check == rand):
            print(x[0])


# print('1',ctx.args)
        # print('2',ctx.author)
        # print('3',ctx.bot)
        # print('4',ctx.channel)
        # print('5',ctx.cog)
        # print('6',ctx.command)
        # print('7',ctx.command_failed)
        # print('8',ctx.guild)
        # print('9',ctx.invoked_subcommand)
        # print('10',ctx.invoked_with)
        # print('11',ctx.kwargs)
        # print('12',ctx.me)
        # print(ctx.message.guild.id)
        # print('14',ctx.prefix)
        # print('15',ctx.subcommand_passed)
        # print('16',ctx.valid)
        # print('17',ctx.voice_client)
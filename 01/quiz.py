questions = ['Who is an foundator of Python?', 'How is represnted boolean data type in Python?', 'How much is 36+34?']
answers = ['Guido van Rossum', 'bool', '70']
q = zip(questions, answers)

quizz = [] 
for item in q:
    quizz.append({'question': item[0], 'answer': item[1]})


def quiz_game(qa):
    score = 0
    for q in qa:
        print(q['question'])
        answer = input('What\'s your answer? \n')
        print()
        if answer == q['answer']:
            score +=1
            print('Well done!')
            print()
        else:
            print('No. Your answer is wrong, sorry! ')
            print()
    if score == len(questions):
        print(f'Congrats! You\'ve win. Your score is {score}')
        print()
    else:
        print(f'Your score is {score}')
    print('Thanx for taking part!')
    print()
quiz_game(quizz)

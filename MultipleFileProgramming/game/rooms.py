import random
rooms = ["Sport", "History", "Geography"] # add ---> Animals , Science

index = random.randint(0, 2)
room = rooms[index]

file_path = 'data/' + room + '.txt'

with open(file_path, 'r') as raeder:
    fileContent = raeder.readlines()

def displayQuestionsAndGetAnswers():
    print(f"====================== {room} ======================")
    answers = []
    for line in range(0, len(fileContent), 2):
        question = fileContent[line][:-1]
        ans = input(question)
        answers.append(ans)
    return answers

def checkAnswers(answers):
    score = 0
    for line in range(1, len(fileContent), 2):
        ansArrayIndex = line // 2
        answer = fileContent[line][:-1]
        if (answer == answers[ansArrayIndex]):
            score += 1
    return score

def getUserScore():
    return checkAnswers(displayQuestionsAndGetAnswers())

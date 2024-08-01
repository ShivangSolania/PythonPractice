from ques import Question
quest = [ 
    "What colours are apple?\na) red\nb) black\nc)magenta\n\n",
    "What colours are orange?\na) red\nb) black\nc)orange\n\n",
    "What colours are banana?\na) red\nb) yellow\nc)magenta\n\n",   
]

questions = [
    Question(quest[0], "a"),
    Question(quest[1], "c"),
    Question(quest[2], "b"),
]

def test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("Score is:" , score , "/3")
    
test(questions)
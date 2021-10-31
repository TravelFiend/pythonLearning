from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

theQuestions = []
for question in question_data:
  theQuestions.append(Question(question['text'], question['answer']))

quiz = QuizBrain(theQuestions)

while quiz.still_has_questions():
  quiz.next_question()

print('You\'ve completed the quiz')
print(f'Your final score was: {quiz.score}/{quiz.question_number}')

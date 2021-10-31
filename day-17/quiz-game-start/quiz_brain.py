class QuizBrain:
  def __init__(self, questions_list):
    self.questions_list = questions_list
    self.question_number = 0
    self.score = 0

  def still_has_questions(self):
    return self.question_number < len(self.questions_list)

  def next_question(self):
    currentQuestion = self.questions_list[self.question_number]
    if self.question_number < len(self.questions_list):
      self.question_number += 1
    user_answer = input(f'Q.{self.question_number}: {currentQuestion.text} (True/False): ')
    self.checkAnswer(currentQuestion.answer, user_answer)

  def checkAnswer(self, correctAnswer, userAnswer):
    if correctAnswer.lower() == userAnswer.lower():
      self.score += 1
      print('You got it right big dog!')
    else:
      print('Sorry, that\'s wrong')
    print(f'The correct answer was: {correctAnswer}')
    print(f'Your current score is {self.score}/{self.question_number}\n')

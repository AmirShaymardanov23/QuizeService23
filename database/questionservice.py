from database.models import Question,db
import random

# Get questions
def get_questions_db(level):

    # if !=level
    if level == 'all':
        questions = []
        all_questions = Question.query.all

        for i in range(20):
            questions.append(random.choice(all_questions))

        return questions
    # if level is not default
    questions_from_level = Question.query.filter(level=level).all()
    questions = [random.choice(questions_from_level) for i in range(20)]

    return questions


# checking answer
def check_user_answer(question_id,user_answer):

    current_question = Question.query.get(question_id)

    # checking users answer with answer from db
    if current_question.correct_answer == True:
        return True
    return False


#adding question to db

def add_questions(level,question,answer1,answer2,answer3,answer4,correctness):
    add_questions = Question.query.filter(level=level,question=question,answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4,correctness=correctness).all()

    return add_questions
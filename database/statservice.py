from database.models import Result,db,Rating


#  get user's rating
def get_rating_db(level):

    # if all
    if level == 'all':
        rating = Result.query.all()

        rating_user = []



def add_user_answer_db(user_id,user_answer,correctness):

    adding_answer = Result.query.filter(user_id=user_id,user_answer=user_answer,correctness=correctness)


def add_user_rating_db(user_id,correct_answer):

    #checking if user in Rating
    pass


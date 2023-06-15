from main import db
from datetime import datetime

# users' table
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String,nullable = False)
    phone_number = db.Column(db.String,unique = True)
    reg_data = db.Column(db.Datetime, default = datetime.now())


# questions' table
class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.String, default = 'Easy')
    main_question = db.Column(db.String, nullable=False, unique=True)
    answer1 = db.Column(db.String)
    answer2 = db.Column(db.String)
    answer3 = db.Column(db.String, nullable=True)
    answer4 = db.Column(db.String, nullable=True)
    correct_answer = db.Column(db.Integer,nullable=False )
    timer = db.Column(db.Integer)

# result's table
class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question_id'))
    user_answer = db.Column(db.String, nullable = False)
    correctness = db.Column(db.Boolean, nullable = True)
    level = db.Column(db.String)
    user_fk = db.relationship(User)
    question_fk = db.relationship(Question)


# rating
class Rating(db.Model):
    __tablename__ = 'ratings'
    user_id = db.Column(db.Integer,db.ForeignKey('user_id'))
    user_correct_answers = db.Column(db.Integer,default=0)

    user_fk = db.relationship(User)
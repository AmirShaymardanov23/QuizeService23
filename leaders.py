from flask import Blueprint
from typing import Dict,List

leaders_bp = Blueprint('leaders',__name__)

# запрос на получении топов
@leaders_bp.route('/leaders/<string:level>',methods = ['GET'])
def get_top_5_leaders(level:str = 'all')-> Dict[str,List[Dict[str,int]]]:
    pass


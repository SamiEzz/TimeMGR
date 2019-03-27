import time
from activity import activity

# 16/03 a 13h10


def main_program():
    user_in=""
    end_work=0
    task1=activity()
    task1.start_act()
    task1.project="TIME_MGR"
    task1.comments="First task ever !"
    while end_work!="1":
        print("Press '0' to stop counter")
        user_in = input()
        if user_in=="0" :
            end_work="1"
            task1.end_act()
    task1.export2json()


main_program()

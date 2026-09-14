from models import User
def match_learners(user,learners):
 a=set((user.skills or '').lower().split(',')); return sorted(((len(a & set((x.skills or '').lower().split(','))),x) for x in learners if x.id!=user.id),key=lambda p:p[0],reverse=True)

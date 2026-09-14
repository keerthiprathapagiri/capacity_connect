import sys, json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import app,db
from models import User,Course,Lecture,Competency,Assessment,Notification

def user(name,email,role,status='approved'):
 u=User.query.filter_by(email=email).first()
 if not u: u=User(email=email); db.session.add(u)
 u.name=name; u.role=role; u.approval_status=status; u.skills='python,sql,flask,analytics'; u.set_password('demo123'); return u

def run():
 with app.app_context():
  admin=user('Admin','admin@capacity.local','admin'); trainer=user('Trainer','trainer@capacity.local','trainer'); learner=user('Learner','learner@capacity.local','learner'); pending=user('Pending Trainer','pending@capacity.local','trainer','pending'); db.session.flush()
  c=Course.query.filter_by(title='Practical Python Foundations').first()
  if not c: c=Course(title='Practical Python Foundations',description='A signal-rich course for technical teams.',trainer_id=trainer.id); db.session.add(c); db.session.flush()
  first=Lecture.query.filter_by(course_id=c.id,title='Functions and mental models').first()
  if not first:
   data=[{'start':0,'end':18,'text':'Functions accept inputs and return outputs.'},{'start':18,'end':42,'text':'Small pure functions are easier to test and reason about.'},{'start':42,'end':70,'text':'Use meaningful names and explicit contracts.'}]
   p=Path(app.config['UPLOAD_TRANSCRIPT_FOLDER'])/'python-functions.json'; p.write_text(json.dumps(data),encoding='utf8')
   db.session.add(Lecture(course_id=c.id,title='Functions and mental models',topic='Python',description='Build robust abstractions.',video_path=None,transcript_path='uploads/transcripts/python-functions.json',duration=70))
  else:
   p=Path(app.config['UPLOAD_TRANSCRIPT_FOLDER'])/'python-functions.json'; p.write_text(json.dumps([{'start':0,'end':18,'text':'Functions accept inputs and return outputs.'},{'start':18,'end':42,'text':'Small pure functions are easier to test and reason about.'},{'start':42,'end':70,'text':'Use meaningful names and explicit contracts.'}]),encoding='utf8'); first.transcript_path='uploads/transcripts/python-functions.json'; first.duration=70
  if not Lecture.query.filter_by(course_id=c.id,title='Data and debugging').first(): db.session.add(Lecture(course_id=c.id,title='Data and debugging',topic='Python',difficulty='Advanced',description='Debug with evidence.'))
  db.session.flush()
  if not Assessment.query.filter_by(course_id=c.id).first(): db.session.add(Assessment(course_id=c.id,title='Python understanding check',questions=[{'text':'What does a function return?','answer':'a value'},{'text':'What makes code easier to test?','answer':'pure functions'}]))
  if not Competency.query.filter_by(user_id=learner.id,skill='Python').first(): db.session.add(Competency(user_id=learner.id,skill='Python',score=62))
  if not Notification.query.filter_by(user_id=learner.id,title='Welcome to Capacity Connect').first(): db.session.add(Notification(user_id=learner.id,title='Welcome to Capacity Connect',message='Your learning signals will shape your competency profile.'))
  db.session.commit(); print('Idempotent demo data ready')
if __name__=='__main__': run()

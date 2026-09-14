from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from app import db
class User(UserMixin,db.Model):
 id=db.Column(db.Integer,primary_key=True); name=db.Column(db.String(120),nullable=False); email=db.Column(db.String(160),unique=True,nullable=False); password_hash=db.Column(db.String(255),nullable=False); role=db.Column(db.String(20),default='learner'); approval_status=db.Column(db.String(20),default='approved'); bio=db.Column(db.Text); skills=db.Column(db.String(500)); interests=db.Column(db.String(500)); created_at=db.Column(db.DateTime,default=datetime.utcnow)
 def set_password(self,p): self.password_hash=generate_password_hash(p)
 def check_password(self,p): return check_password_hash(self.password_hash,p)
class Course(db.Model):
 id=db.Column(db.Integer,primary_key=True); title=db.Column(db.String(180),nullable=False); description=db.Column(db.Text); trainer_id=db.Column(db.Integer,db.ForeignKey('user.id')); created_at=db.Column(db.DateTime,default=datetime.utcnow); lectures=db.relationship('Lecture',backref='course',cascade='all, delete-orphan')
class Lecture(db.Model):
 id=db.Column(db.Integer,primary_key=True); course_id=db.Column(db.Integer,db.ForeignKey('course.id'),nullable=False); title=db.Column(db.String(180)); description=db.Column(db.Text); topic=db.Column(db.String(120)); difficulty=db.Column(db.String(40),default='Intermediate'); video_path=db.Column(db.String(300)); transcript_path=db.Column(db.String(300)); duration=db.Column(db.Integer,default=0); created_at=db.Column(db.DateTime,default=datetime.utcnow)
class VideoEvent(db.Model):
 id=db.Column(db.Integer,primary_key=True); user_id=db.Column(db.Integer,db.ForeignKey('user.id')); lecture_id=db.Column(db.Integer,db.ForeignKey('lecture.id')); event_type=db.Column(db.String(40)); timestamp=db.Column(db.Float); created_at=db.Column(db.DateTime,default=datetime.utcnow)
class Doubt(db.Model):
 id=db.Column(db.Integer,primary_key=True); user_id=db.Column(db.Integer,db.ForeignKey('user.id')); lecture_id=db.Column(db.Integer,db.ForeignKey('lecture.id')); topic=db.Column(db.String(120)); question=db.Column(db.Text); anonymous=db.Column(db.Boolean,default=False); answer=db.Column(db.Text); resolved=db.Column(db.Boolean,default=False); created_at=db.Column(db.DateTime,default=datetime.utcnow)
class Assessment(db.Model):
 id=db.Column(db.Integer,primary_key=True); course_id=db.Column(db.Integer,db.ForeignKey('course.id')); title=db.Column(db.String(180)); questions=db.Column(db.JSON,default=list)
class AssessmentResult(db.Model):
 id=db.Column(db.Integer,primary_key=True); assessment_id=db.Column(db.Integer); user_id=db.Column(db.Integer); score=db.Column(db.Float); created_at=db.Column(db.DateTime,default=datetime.utcnow)
class TeachBack(db.Model):
 id=db.Column(db.Integer,primary_key=True); user_id=db.Column(db.Integer); lecture_id=db.Column(db.Integer); response=db.Column(db.Text); score=db.Column(db.Float); created_at=db.Column(db.DateTime,default=datetime.utcnow)
class Competency(db.Model):
 id=db.Column(db.Integer,primary_key=True); user_id=db.Column(db.Integer); skill=db.Column(db.String(120)); score=db.Column(db.Float,default=0); updated_at=db.Column(db.DateTime,default=datetime.utcnow)
class Notification(db.Model):
 id=db.Column(db.Integer,primary_key=True); user_id=db.Column(db.Integer); title=db.Column(db.String(180)); message=db.Column(db.Text); read=db.Column(db.Boolean,default=False); created_at=db.Column(db.DateTime,default=datetime.utcnow)
class PeerConnection(db.Model):
 id=db.Column(db.Integer,primary_key=True); requester_id=db.Column(db.Integer); helper_id=db.Column(db.Integer); status=db.Column(db.String(20),default='pending'); created_at=db.Column(db.DateTime,default=datetime.utcnow)
class Message(db.Model):
 id=db.Column(db.Integer,primary_key=True); sender_id=db.Column(db.Integer); room=db.Column(db.String(120)); body=db.Column(db.Text); anonymous=db.Column(db.Boolean,default=False); created_at=db.Column(db.DateTime,default=datetime.utcnow)
class CurriculumAlert(db.Model):
 id=db.Column(db.Integer,primary_key=True); course_id=db.Column(db.Integer); lecture_id=db.Column(db.Integer); message=db.Column(db.Text); severity=db.Column(db.String(20),default='medium'); created_at=db.Column(db.DateTime,default=datetime.utcnow)

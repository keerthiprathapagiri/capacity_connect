from flask import Blueprint,render_template,redirect,url_for
from flask_login import login_required,current_user
from app import db
from models import User,Course,Doubt,VideoEvent
from utils.decorators import role_required
trainer_bp=Blueprint('trainer',__name__,url_prefix='/trainer')
@trainer_bp.route('/dashboard')
@login_required
@role_required('trainer','admin')
def dashboard(): return render_template('trainer/dashboard.html',courses=Course.query.filter_by(trainer_id=current_user.id).all(),doubts=Doubt.query.all(),learners=User.query.filter_by(role='learner').all())
@trainer_bp.route('/learners')
@login_required
@role_required('trainer','admin')
def learners(): return render_template('trainer/learners.html',learners=User.query.filter_by(role='learner').all())
@trainer_bp.route('/confusion')
@login_required
@role_required('trainer','admin')
def confusion(): return render_template('trainer/confusion.html',events=VideoEvent.query.all())
@trainer_bp.route('/doubts')
@login_required
@role_required('trainer','admin')
def doubts(): return render_template('trainer/doubts.html',doubts=Doubt.query.all())

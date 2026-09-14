from flask import Blueprint,render_template,request,redirect,url_for,flash
from flask_login import login_required,current_user
from models import Course,Competency,Doubt,Assessment,AssessmentResult,TeachBack
from app import db
learner_bp=Blueprint('learner',__name__,url_prefix='/learner')
@learner_bp.route('/dashboard')
@login_required
def dashboard(): return render_template('dashboard.html',courses=Course.query.all(),competencies=Competency.query.filter_by(user_id=current_user.id).all(),doubts=Doubt.query.filter_by(user_id=current_user.id).all())
@learner_bp.route('/competency')
@login_required
def competency(): return render_template('competency.html',competencies=Competency.query.filter_by(user_id=current_user.id).all())
@learner_bp.route('/readiness')
@login_required
def readiness(): return render_template('readiness.html',competencies=Competency.query.filter_by(user_id=current_user.id).all())
@learner_bp.route('/assessment/<int:assessment_id>',methods=['GET','POST'])
@login_required
def assessment(assessment_id):
 a=Assessment.query.get_or_404(assessment_id)
 if request.method=='POST':
  qs=a.questions or []; correct=sum(str(request.form.get('q'+str(i),'')).strip().lower()==str(q.get('answer','')).strip().lower() for i,q in enumerate(qs))
  score=round(correct*100/len(qs),1) if qs else 0
  db.session.add(AssessmentResult(assessment_id=a.id,user_id=current_user.id,score=score)); db.session.commit(); flash(f'Assessment submitted: {score}%','success'); return redirect(url_for('learner.dashboard'))
 return render_template('assessment.html',assessment=a)
@learner_bp.route('/teach-back/<int:lecture_id>',methods=['POST'])
@login_required
def teach_back(lecture_id):
 response=request.form.get('response','').strip()
 if len(response)<10: flash('Please explain the concept in a little more detail.','warning')
 else:
  db.session.add(TeachBack(user_id=current_user.id,lecture_id=lecture_id,response=response,score=min(100,len(response)/2))); db.session.commit(); flash('Teach-back submitted for review.','success')
 return redirect(url_for('courses.lecture',lecture_id=lecture_id))

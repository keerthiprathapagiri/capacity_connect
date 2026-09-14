import json, os
from flask import Blueprint,render_template,request,redirect,url_for,flash,jsonify,current_app
from flask_login import login_required,current_user
from app import db
from models import Course,Lecture
from utils.decorators import role_required
from werkzeug.utils import secure_filename
courses_bp=Blueprint('courses',__name__,url_prefix='/courses')
@courses_bp.route('/')
def list_courses(): return render_template('courses.html',courses=Course.query.order_by(Course.created_at.desc()).all())
@courses_bp.route('/<int:course_id>')
def detail(course_id): return render_template('course.html',course=Course.query.get_or_404(course_id))
@courses_bp.route('/create',methods=['GET','POST'])
@login_required
@role_required('trainer','admin')
def create():
 if request.method=='POST': db.session.add(Course(title=request.form['title'],description=request.form.get('description'),trainer_id=current_user.id)); db.session.commit(); return redirect(url_for('courses.list_courses'))
 return render_template('create_course.html')
@courses_bp.route('/<int:course_id>/lecture',methods=['POST'])
@login_required
@role_required('trainer','admin')
def add_lecture(course_id):
 c=Course.query.get_or_404(course_id); f=request.files.get('video'); path=None
 if current_user.role == 'trainer' and (current_user.approval_status != 'approved' or c.trainer_id != current_user.id):
  return ('Trainer approval or course ownership required',403)
 if f and f.filename:
  name=secure_filename(f.filename)
  if not name or '.' not in name or name.rsplit('.',1)[1].lower() not in current_app.config['ALLOWED_VIDEO_EXTENSIONS']:
   flash('Unsupported video type. Use MP4, WebM, MOV, M4V or OGG.','danger'); return redirect(url_for('courses.detail',course_id=c.id))
  f.save(os.path.join(current_app.config['UPLOAD_VIDEO_FOLDER'],name)); path=os.path.join('uploads/videos',name).replace('\\','/')
 l=Lecture(course_id=c.id,title=request.form['title'],description=request.form.get('description'),topic=request.form.get('topic'),video_path=path,transcript_path=request.form.get('transcript')); db.session.add(l); db.session.commit(); return redirect(url_for('courses.detail',course_id=c.id))
@courses_bp.route('/lecture/<int:lecture_id>')
def lecture(lecture_id): return render_template('lecture.html',lecture=Lecture.query.get_or_404(lecture_id))

@courses_bp.route('/lecture/<int:lecture_id>/transcript')
def transcript(lecture_id):
 l=Lecture.query.get_or_404(lecture_id)
 if not l.transcript_path: return jsonify([])
 full=os.path.join(current_app.static_folder,l.transcript_path)
 try:
  with open(full,encoding='utf-8') as f: data=json.load(f)
  return jsonify(data if isinstance(data,list) else data.get('segments',[]))
 except (OSError,ValueError): return jsonify([])

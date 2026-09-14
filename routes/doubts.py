from flask import Blueprint,render_template,request,redirect,url_for,flash
from flask_login import login_required,current_user
from app import db
from models import Doubt
bp=Blueprint('doubts',__name__,url_prefix='/doubts')
@bp.route('/')
@login_required
def index(): return render_template('doubts.html',doubts=Doubt.query.order_by(Doubt.created_at.desc()).all())
@bp.route('/ask',methods=['POST'])
@login_required
def ask(): db.session.add(Doubt(user_id=current_user.id,lecture_id=request.form.get('lecture_id') or None,topic=request.form.get('topic'),question=request.form['question'],anonymous=bool(request.form.get('anonymous')))); db.session.commit(); flash('Doubt posted','success'); return redirect(url_for('doubts.index'))
doubts_bp=bp

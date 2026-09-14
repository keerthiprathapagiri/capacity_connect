from flask import Blueprint,render_template,redirect,url_for
from flask_login import current_user
main_bp=Blueprint('main',__name__)
@main_bp.route('/')
def index(): return render_template('landing.html')
@main_bp.route('/dashboard')
def dashboard():
 if not current_user.is_authenticated:return redirect(url_for('auth.login'))
 return redirect(url_for(current_user.role+'.dashboard'))
@main_bp.route('/profile',methods=['GET','POST'])
def profile():
 from app import db
 if not current_user.is_authenticated:return redirect(url_for('auth.login'))
 if __import__('flask').request.method=='POST':
  from flask import request
  current_user.bio=request.form.get('bio'); current_user.skills=request.form.get('skills'); current_user.interests=request.form.get('interests'); db.session.commit()
 return render_template('profile.html')

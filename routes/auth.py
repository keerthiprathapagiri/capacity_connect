from flask import Blueprint,render_template,request,redirect,url_for,flash
from flask_login import login_user,logout_user,current_user
from app import db
from models import User
from werkzeug.security import generate_password_hash
auth_bp=Blueprint('auth',__name__,url_prefix='/auth')
@auth_bp.route('/login',methods=['GET','POST'])
def login():
 if request.method=='POST':
  u=User.query.filter_by(email=request.form['email'].lower()).first()
  if u and u.check_password(request.form['password']) and (u.approval_status=='approved' or u.role!='trainer'):
   login_user(u); return redirect(url_for('main.dashboard'))
  flash('Invalid credentials or trainer awaiting approval','danger')
 return render_template('login.html')
@auth_bp.route('/register',methods=['GET','POST'])
def register():
 if request.method=='POST':
  if User.query.filter_by(email=request.form['email'].lower()).first(): flash('Email already registered','warning')
  else:
   role=request.form.get('role','learner'); u=User(name=request.form['name'],email=request.form['email'].lower(),role=role,approval_status='pending' if role=='trainer' else 'approved'); u.set_password(request.form['password']); db.session.add(u); db.session.commit(); flash('Account created. Trainers require admin approval.','success'); return redirect(url_for('auth.login'))
 return render_template('register.html')
@auth_bp.route('/logout')
def logout(): logout_user(); return redirect(url_for('main.index'))

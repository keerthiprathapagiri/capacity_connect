from flask import Blueprint,render_template,redirect,url_for
from flask_login import login_required
from app import db
from models import User,Course
from utils.decorators import role_required
admin_bp=Blueprint('admin',__name__,url_prefix='/admin')
@admin_bp.route('/dashboard')
@login_required
@role_required('admin')
def dashboard(): return render_template('admin/dashboard.html',users=User.query.all(),courses=Course.query.all())
@admin_bp.route('/trainers/<int:user_id>/approve')
@login_required
@role_required('admin')
def approve(user_id):
 u=User.query.get_or_404(user_id); u.approval_status='approved'; db.session.commit(); return redirect(url_for('admin.dashboard'))
@admin_bp.route('/trainers/<int:user_id>/reject')
@login_required
@role_required('admin')
def reject(user_id):
 u=User.query.get_or_404(user_id); u.approval_status='rejected'; db.session.commit(); return redirect(url_for('admin.dashboard'))
@admin_bp.route('/users')
@login_required
@role_required('admin')
def users(): return render_template('admin/users.html',users=User.query.all())

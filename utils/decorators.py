from functools import wraps
from flask import abort
from flask_login import current_user

def role_required(*roles):
 def deco(f):
  @wraps(f)
  def wrapped(*a,**kw):
   if not current_user.is_authenticated or current_user.role not in roles: abort(403)
   if current_user.role == 'trainer' and current_user.approval_status != 'approved': abort(403)
   return f(*a,**kw)
  return wrapped
 return deco

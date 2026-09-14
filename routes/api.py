from flask import Blueprint,request,jsonify
from flask_login import login_required,current_user
from app import db
from models import VideoEvent
api_bp=Blueprint('api',__name__,url_prefix='/api')
@api_bp.route('/events',methods=['POST'])
@login_required
def event():
 d=request.get_json() or {}; db.session.add(VideoEvent(user_id=current_user.id,lecture_id=d.get('lecture_id'),event_type=d.get('event_type','pause'),timestamp=d.get('timestamp',0))); db.session.commit(); return jsonify(ok=True)
@api_bp.route('/heatmap/<int:lecture_id>')
def heatmap(lecture_id):
 rows=db.session.query(VideoEvent.timestamp,db.func.count(VideoEvent.id)).filter_by(lecture_id=lecture_id).group_by(VideoEvent.timestamp).all(); return jsonify(labels=[r[0] for r in rows],values=[r[1] for r in rows])

from flask import Blueprint,render_template
from flask_login import login_required,current_user
from app import db
from models import Message
chat_bp=Blueprint('chat',__name__,url_prefix='/chat')
@chat_bp.route('/')
@login_required
def chat(): return render_template('chat.html',messages=Message.query.order_by(Message.created_at).limit(100).all())
def register_chat(socketio):
 @socketio.on('join')
 def join(data):
  from flask_socketio import join_room
  join_room(data.get('room','general'))
 @socketio.on('message')
 def message(data):
  from flask_socketio import emit
  m=Message(sender_id=current_user.id if current_user.is_authenticated else None,room=data.get('room','general'),body=data.get('body',''),anonymous=data.get('anonymous',False)); db.session.add(m); db.session.commit(); emit('message',{'body':m.body,'anonymous':m.anonymous},to=m.room)

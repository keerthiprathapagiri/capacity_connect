import os
from pathlib import Path
basedir=Path(__file__).resolve().parent
class Config:
    SECRET_KEY=os.getenv('SECRET_KEY','capacity-connect-demo-secret')
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL',f"sqlite:///{basedir/'instance'/'capacity_connect.db'}")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    UPLOAD_VIDEO_FOLDER=str(basedir/'static'/'uploads'/'videos')
    UPLOAD_TRANSCRIPT_FOLDER=str(basedir/'static'/'uploads'/'transcripts')
    MAX_CONTENT_LENGTH=500*1024*1024
    ALLOWED_VIDEO_EXTENSIONS={'mp4','webm','mov','m4v','ogg'}
    ALLOWED_TRANSCRIPT_EXTENSIONS={'json','txt','vtt'}

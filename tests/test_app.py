from app import create_app

def test_home():
 app=create_app(); c=app.test_client(); assert c.get('/').status_code==200

def test_register():
 app=create_app(); c=app.test_client(); r=c.post('/auth/register',data={'name':'Test','email':'x@test.local','password':'x','role':'learner'},follow_redirects=True); assert r.status_code==200

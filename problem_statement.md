============================================================
CAPACITY CONNECT
COMPLETE END-TO-END PROJECT DEVELOPMENT PROMPT
============================================================

You are an expert full-stack developer, software architect,
UI/UX designer, database designer, and testing engineer.

Build a COMPLETE, FUNCTIONAL, POLISHED web application from
SCRATCH.

Do not assume that I already have a project.

Create the entire project, including:

- folder structure
- backend
- frontend
- database
- authentication
- role management
- dashboards
- course system
- video system
- transcript system
- confusion tracking
- confusion heatmap
- doubts
- anonymous doubts
- real-time chat
- anonymous chat
- skill matching
- peer rescue
- assessments
- competency scoring
- role readiness
- curriculum feedback
- notifications
- analytics
- seed/demo data
- testing
- documentation
- deployment configuration

The project name is:

                    CAPACITY CONNECT

The application must be a professional hackathon prototype,
not a basic college CRUD application.

============================================================
1. PROJECT PURPOSE
============================================================

Capacity Connect is a learning and competency platform for
technical organizations.

The central philosophy is:

        UNDERSTANDING > COMPLETION

Traditional LMS platforms mostly tell trainers:

- who logged in
- who watched a video
- who completed a course
- who scored marks

Capacity Connect should go further.

It should identify whether learners actually understood
what they were taught.

The system observes learning signals such as:

- video pauses
- rewinds
- replays
- repeated viewing
- doubts
- assessment performance
- teach-back responses
- peer interactions
- competency
- skill gaps

and turns those signals into actionable insights.

The central product loop is:

LEARN
   ↓
STRUGGLE / CONFUSION
   ↓
ASK DOUBT
   ↓
GET HELP
   ↓
ASSESS UNDERSTANDING
   ↓
MEASURE COMPETENCY
   ↓
CHECK ROLE READINESS
   ↓
IDENTIFY CONTENT PROBLEMS
   ↓
IMPROVE CURRICULUM

Important:

Do NOT make the application exclusively about meteorology
or Earth Sciences.

It should be a GENERAL technical learning and competency
platform.

It can be positioned as suitable for:

SIH26075
Ministry of Earth Sciences
Smart Education

but the actual product should work for:

- technical organizations
- colleges
- training institutions
- corporate training
- developer learning
- government technical training


============================================================
2. MAIN PRODUCT STATEMENT
============================================================

The landing page should communicate this idea:

"Existing LMS platforms tell trainers what learners completed.
Capacity Connect tells them what learners failed to understand."

Alternative supporting statement:

"Built to understand how people learn,
not just what they complete."

The UI and feature architecture must reinforce this concept.


============================================================
3. TECHNOLOGY STACK
============================================================

Use the following stack.

BACKEND
--------

Python 3.x

Flask

Flask-SQLAlchemy

Flask-SocketIO

Werkzeug

Flask-Login OR secure Flask session authentication

Use Flask Blueprints for modular routes.


FRONTEND
--------

HTML5

CSS3

Vanilla JavaScript

Jinja2

Bootstrap 5 may be used selectively.

Do NOT use React.

Do NOT use Node.js as the backend.

The frontend should still look extremely polished.


DATABASE
--------

SQLite

Use SQLAlchemy ORM.

SQLite is sufficient for this prototype.

The database should be created automatically through Python code.

Do NOT require manually creating tables using DB Browser.

Use:

db.create_all()

or a proper initialization mechanism.


REAL-TIME CHAT
--------------

Flask-SocketIO

Use:

async_mode="threading"

unless there is a strong technical reason to use another mode.


CHARTS
------

Chart.js


VIDEO
-----

HTML5 <video>


TRANSCRIPTION
-------------

Preferred:

faster-whisper

Use local transcription.

Do NOT make an external AI API mandatory.


OPTIONAL NLP
------------

scikit-learn may be used for:

- TF-IDF
- cosine similarity
- transcript search
- similar doubt detection

Do not use external AI APIs for core functionality.


FILE STORAGE
------------

Videos:

static/uploads/videos/

Transcripts:

static/uploads/transcripts/

Images:

static/images/

Do NOT store video binaries inside SQLite.


============================================================
4. NO API KEY DEPENDENCY
============================================================

The COMPLETE CORE APPLICATION must work without:

- OpenAI API key
- Gemini API key
- Groq API key
- Claude API key
- Firebase
- MongoDB
- external vector database
- paid APIs

Do not design the application so that it becomes unusable
when an API key is missing.

Local processing and rule-based algorithms should handle
the core prototype.

Optional AI enhancements can be mentioned in future scope.


============================================================
5. COMPLETE PROJECT STRUCTURE
============================================================

Create a clean architecture similar to:

capacity-connect/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── Procfile
│
├── instance/
│   └── capacity_connect.db
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── course.py
│   ├── lecture.py
│   ├── doubt.py
│   ├── video_event.py
│   ├── assessment.py
│   ├── question.py
│   ├── assessment_result.py
│   ├── teach_back.py
│   ├── competency.py
│   ├── role.py
│   ├── role_requirement.py
│   ├── peer_connection.py
│   ├── message.py
│   ├── curriculum_alert.py
│   └── notification.py
│
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   ├── main.py
│   ├── learner.py
│   ├── trainer.py
│   ├── admin.py
│   ├── courses.py
│   ├── doubts.py
│   ├── skill_match.py
│   ├── chat.py
│   └── analytics.py
│
├── services/
│   ├── confusion_service.py
│   ├── matching_service.py
│   ├── competency_service.py
│   ├── readiness_service.py
│   ├── curriculum_service.py
│   ├── transcript_service.py
│   └── notification_service.py
│
├── utils/
│   ├── decorators.py
│   ├── helpers.py
│   └── seed.py
│
├── templates/
│   ├── base.html
│   ├── landing.html
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   │
│   ├── learner/
│   │   ├── dashboard.html
│   │   ├── courses.html
│   │   ├── lecture.html
│   │   ├── skill_match.html
│   │   ├── doubts.html
│   │   ├── chat.html
│   │   ├── competency.html
│   │   └── readiness.html
│   │
│   ├── trainer/
│   │   ├── dashboard.html
│   │   ├── courses.html
│   │   ├── create_course.html
│   │   ├── upload.html
│   │   ├── learners.html
│   │   ├── confusion.html
│   │   ├── doubts.html
│   │   └── curriculum_alerts.html
│   │
│   └── admin/
│       ├── dashboard.html
│       ├── users.html
│       ├── trainers.html
│       ├── courses.html
│       └── analytics.html
│
├── static/
│   ├── css/
│   │   ├── style.css
│   │   ├── landing.css
│   │   ├── dashboard.css
│   │   ├── chat.css
│   │   └── animations.css
│   │
│   ├── js/
│   │   ├── main.js
│   │   ├── background.js
│   │   ├── video.js
│   │   ├── heatmap.js
│   │   ├── skill-match.js
│   │   ├── doubts.js
│   │   ├── chat.js
│   │   └── dashboard.js
│   │
│   ├── images/
│   │   └── hero.png
│   │
│   └── uploads/
│       ├── videos/
│       └── transcripts/
│
├── scripts/
│   └── seed.py
│
└── tests/
    ├── test_auth.py
    ├── test_matching.py
    ├── test_confusion.py
    ├── test_competency.py
    └── test_readiness.py


============================================================
6. DEVELOPMENT ORDER
============================================================

Build the project in the following exact phases.

PHASE 1
Project initialization

PHASE 2
Database

PHASE 3
Authentication

PHASE 4
Role-based authorization

PHASE 5
Global UI design system

PHASE 6
Landing page

PHASE 7
Learner dashboard

PHASE 8
Trainer dashboard

PHASE 9
Admin dashboard

PHASE 10
Profile

PHASE 11
Courses

PHASE 12
Video upload

PHASE 13
Transcript generation

PHASE 14
Lecture player

PHASE 15
Video event tracking

PHASE 16
Confusion algorithm

PHASE 17
Heatmap

PHASE 18
Doubts

PHASE 19
Anonymous doubts

PHASE 20
Lecture transcript search

PHASE 21
Skill Match

PHASE 22
Peer Rescue

PHASE 23
Socket.IO chat

PHASE 24
Normal and anonymous chat

PHASE 25
Assessments

PHASE 26
Teach-back

PHASE 27
Competency engine

PHASE 28
Role readiness

PHASE 29
Curriculum feedback

PHASE 30
Notifications

PHASE 31
Analytics

PHASE 32
Demo data

PHASE 33
Testing

PHASE 34
UI polishing

PHASE 35
Deployment

PHASE 36
Documentation

Do not jump randomly between phases.


============================================================
7. PHASE 1 — PROJECT INITIALIZATION
============================================================

Create the Flask application from scratch.

Configure:

- Flask
- SQLAlchemy
- Socket.IO
- secret key
- upload folders
- maximum upload size
- session configuration

Create:

app.py

config.py

requirements.txt

.env.example

README.md

Create required directories automatically if they don't exist.


============================================================
8. PHASE 2 — DATABASE
============================================================

Create SQLite database:

instance/capacity_connect.db

Create models for:

USER
----

id
name
email
password_hash
role
approval_status
bio
skills
interests
profile_image
created_at


COURSE
------

id
title
description
trainer_id
created_at


LECTURE
-------

id
course_id
title
description
topic
difficulty
video_path
transcript_path
duration
created_at


VIDEO EVENT
-----------

id
user_id
lecture_id
event_type
timestamp
created_at


DOUBT
-----

id
user_id
lecture_id
topic
question
timestamp
anonymous
status
answer
created_at


ASSESSMENT
----------

id
lecture_id
title


QUESTION
--------

id
assessment_id
question
option_a
option_b
option_c
option_d
correct_answer


ASSESSMENT RESULT
-----------------

id
user_id
assessment_id
score
created_at


TEACH BACK
----------

id
user_id
lecture_id
response
score
trainer_feedback
created_at


COMPETENCY
----------

id
user_id
skill
score
updated_at


ROLE
----

id
name


ROLE REQUIREMENT
----------------

id
role_id
skill
weight


PEER CONNECTION
---------------

id
requester_id
receiver_id
topic
status
created_at


MESSAGE
-------

id
sender_id
receiver_id
message
anonymous
created_at


CURRICULUM ALERT
----------------

id
lecture_id
topic
timestamp
confusion_score
doubt_count
affected_learners
recommendation
status
created_at


NOTIFICATION
------------

id
user_id
message
is_read
created_at


Use proper foreign keys and relationships.


============================================================
9. PHASE 3 — AUTHENTICATION
============================================================

Create:

Register
Login
Logout

Registration fields:

Name
Email
Password
Role

Roles:

Learner
Trainer

Admin must NOT be publicly registered.

Create a preconfigured Admin account through seed data.

Hash passwords using Werkzeug.

Never store plain-text passwords.


============================================================
10. TRAINER APPROVAL
============================================================

This is mandatory.

When a user registers as Trainer:

approval_status = "PENDING"

Immediately show:

"Your trainer account has been created.
Your account is waiting for admin approval."

The trainer must NOT be allowed to access:

- trainer dashboard
- course creation
- video upload
- learner analytics

until approved.

Admin sees:

PENDING TRAINER REQUESTS

with:

Name
Email
Skills
Registration date

Buttons:

APPROVE
REJECT

If approved:

approval_status = "APPROVED"

Trainer can access trainer features.

If rejected:

approval_status = "REJECTED"

Display an appropriate message.

Admin dashboard must show counts:

Pending Trainers
Approved Trainers
Rejected Trainers


============================================================
11. ROLE AUTHORIZATION
============================================================

Create decorators/helpers such as:

login_required
role_required
trainer_required
approved_trainer_required
admin_required

Never rely only on hiding buttons.

Backend must enforce permissions.


============================================================
12. UI/UX — VERY IMPORTANT
============================================================

The frontend quality is extremely important.

It must look like a modern premium SaaS/EdTech product.

It must NOT look like:

- a basic Flask project
- a default Bootstrap dashboard
- a plain CRUD application
- a generic college website


============================================================
13. VISUAL IDENTITY
============================================================

Main theme:

DARK
FUTURISTIC
TECHNICAL
PREMIUM
CONNECTED


BACKGROUND
----------

Use an almost-black / dark navy background.

Examples:

#080812
#0B0A14
#0D0B18


PRIMARY COLORS
--------------

Blue shades:

#2563EB
#3B82F6
#60A5FA

Purple shades:

#7C3AED
#8B5CF6
#A78BFA

Deep purple:

#4C1D95


TEXT
----

White:

#F8FAFC

Secondary:

#CBD5E1

Muted:

#94A3B8


CARDS
-----

Use:

#111122
#15142A
#1A1830

with subtle transparent purple borders.


============================================================
14. STAR + CONNECTION BACKGROUND
============================================================

Create a reusable animated background.

The background should contain:

small stars
+
thin lines connecting some stars.

The connecting lines should be light purple.

The stars should have subtle movement or twinkling.

The effect represents:

People
Skills
Knowledge
Connections

Use JavaScript canvas or lightweight DOM/CSS.

IMPORTANT:

The background must be subtle.

It should never make text difficult to read.

It should not look like a video-game space background.

It should look like:

"connected technology + knowledge network."


============================================================
15. UI ELEMENTS
============================================================

Use:

- rounded cards
- glassmorphism-like dark cards
- subtle borders
- soft shadows
- blue/purple gradients
- clean typography
- elegant icons
- smooth transitions
- hover states
- active states
- loading states
- empty states
- error states

Use Poppins or Inter.

Headings should be bold.

Body text should be clean and readable.

Use plenty of whitespace.

Do not make everything glow.

Glow should be subtle.


============================================================
16. YELLOW ACCENT
============================================================

The website should primarily be:

BLUE + PURPLE.

Yellow should only be used as an occasional attention color.

For example:

- high confusion
- warning
- important notification

Do NOT make yellow the main theme.


============================================================
17. NAVBAR
============================================================

Create a professional navbar.

Logo:

CAPACITY
CONNECT

or:

Capacity Connect

Navigation changes depending on role.

Learner:

Dashboard
Courses
Skill Match
Doubts
Competency
Role Readiness
Profile

Trainer:

Dashboard
Courses
Upload Content
Confusion Analytics
Doubts
Curriculum Alerts
Profile

Admin:

Dashboard
Users
Trainer Approvals
Courses
Analytics
Profile

Also show:

notification icon
profile/avatar


============================================================
18. LANDING PAGE
============================================================

Create a premium landing page.

Hero:

Left:

CAPACITY CONNECT

Large headline:

"Learning Should Measure Understanding."

Supporting text:

"Turn learning behavior, doubts and competency data into
actionable insights for better learning and better training."

Buttons:

START LEARNING

EXPLORE COURSES

Right side:

Create a large visual image area.

Use:

static/images/hero.png

I will place an image there later.

If the image does not exist, show an elegant placeholder.

The page must not break.


============================================================
19. LANDING PAGE — PROBLEM SECTION
============================================================

Create a section titled:

"Learning problems we've all faced"

Use attractive cards.

Examples:

Learning in isolation
No practical experience
No peer support
Difficult to retain what was taught
Hard to get across the finish line
No personal guidance
Outdated curriculum

Each card should have:

icon
short title
small explanation

Cards should feel visually connected.


============================================================
20. LANDING PAGE — HOW IT WORKS
============================================================

Create:

"How Capacity Connect works"

Show a visual flow:

LEARN
 ↓
CONFUSION
 ↓
DOUBT
 ↓
PEER HELP
 ↓
ASSESS
 ↓
COMPETENCY
 ↓
ROLE READINESS
 ↓
CURRICULUM IMPROVEMENT

Use connected lines and animated arrows.

This section should explain the entire product quickly.


============================================================
21. FEATURE CAROUSEL
============================================================

Create a horizontal feature carousel.

Cards should continuously move:

RIGHT → LEFT

Features:

Confusion Heatmap
Anonymous Doubts
Skill Match
Peer Rescue
Lecture Search
Competency Insights
Role Readiness
Curriculum Feedback

CRITICAL:

When mouse enters the carousel:

PAUSE

When mouse leaves:

RESUME

Do not make it too fast.

Use smooth continuous animation.

Make sure cards don't jump when animation restarts.

Support touch/mobile behavior where possible.


============================================================
22. HOME PAGE — LEARNING CONTENT
============================================================

Home page must dynamically display uploaded videos/courses.

Section:

"Latest Learning Content"

and:

"Continue Learning"

Cards should show:

Course title
Lecture title
Trainer
Topic
Difficulty
Duration
Progress
Watch button

The cards must come from the database.

Do not hard-code them.

When an approved trainer uploads a video:

the video/lecture should automatically become available
on the learner-facing home/course area.


============================================================
23. COURSE SYSTEM
============================================================

Trainer can:

Create course
Edit course
Delete course
Add lectures

Course fields:

Title
Description
Category
Difficulty

Lecture fields:

Title
Topic
Description
Video
Difficulty

Learner can:

View courses
Open course
View lectures
Continue learning


============================================================
24. VIDEO UPLOAD
============================================================

Approved trainers and Admin can upload videos.

Upload form:

Course
Lecture title
Topic
Description
Difficulty
Video file

Allowed:

.mp4
.webm
.mov where supported

Use:

secure_filename()

Validate file type.

Set maximum file size.

Store video at:

static/uploads/videos/


IMPORTANT:

Do not store video binary data in SQLite.

Store only:

video_path
metadata
duration
course
lecture information

in SQLite.


============================================================
25. TRANSCRIPT SYSTEM
============================================================

After video upload:

attempt:

local transcription using faster-whisper.

Pipeline:

VIDEO
 ↓
AUDIO
 ↓
FASTER-WHISPER
 ↓
TIMESTAMPED SEGMENTS
 ↓
JSON TRANSCRIPT

Store transcript at:

static/uploads/transcripts/


Example:

[
    {
        "start": 0,
        "end": 42,
        "text": "Welcome to Python functions."
    },
    {
        "start": 42,
        "end": 130,
        "text": "A function is a reusable block of code."
    }
]

The transcript must have timestamps.


============================================================
26. TRANSCRIPTION FALLBACK
============================================================

Do NOT let transcription failure break video upload.

If faster-whisper is unavailable:

show:

"Automatic transcription is currently unavailable.
You can add/edit the transcript manually."

Allow trainer to add transcript segments manually.

The rest of the application must continue working.

This is important because local Whisper can be heavy.


============================================================
27. LECTURE PAGE
============================================================

Create a premium lecture page.

Layout:

LEFT:

Video player

RIGHT:

Transcript

BELOW:

Lecture information
Progress
Doubts
Assessment
Teach-back

Video controls should be standard HTML5 controls.

Transcript entries should be clickable.

Example:

04:12
Parameters and Arguments

Click:

video.currentTime = 252


============================================================
28. LECTURE SEARCH
============================================================

Add:

"Search this lecture..."

Search through transcript.

Initially use:

lowercase normalization
tokenization
keyword matching

Optionally use:

TF-IDF
cosine similarity

through scikit-learn.

Do not require AI.

Results:

04:12
Parameters and Arguments

06:40
Return Statements

Clicking result jumps video to timestamp.


============================================================
29. VIDEO LEARNING SIGNAL TRACKING
============================================================

Track meaningful video behavior.

Use HTML5 video events.

Track:

pause
seek
rewind
replay
repeated segment visits

Do NOT send a request to the backend every second.

Use meaningful events only.

Send event information to Flask.

Example:

POST /api/video-event

Data:

user_id
lecture_id
event_type
timestamp


============================================================
30. CONFUSION DETECTION
============================================================

Create:

services/confusion_service.py

Use a transparent rule-based algorithm.

Divide video into segments.

Recommended:

15-second segments.

For each segment calculate:

confusion_score

Use:

rewind × 3
replay × 3
seek_back × 2
pause × 1
doubt × 5

Example:

At 04:00–04:15:

Rewinds = 5
Replays = 4
Pauses = 3
Doubts = 2

Score:

5×3
+
4×3
+
3×1
+
2×5

= 40

Normalize the score for visualization.

Do NOT claim this is machine learning.

Call it:

"Behavior-based confusion detection."


============================================================
31. CONFUSION HEATMAP
============================================================

Display confusion directly on the video timeline.

Use colors:

LOW:

blue

MEDIUM:

purple

HIGH:

bright purple / attention accent

The timeline should visually show where learners struggle.

Example concept:

00:00
BLUE BLUE BLUE PURPLE PURPLE
                 █████
                 HIGH
                 04:12
                         BLUE
12:45

Clicking a segment jumps to that timestamp.

Hovering over a segment shows:

Timestamp
Confusion score
Replays
Rewinds
Pauses
Doubts


============================================================
32. TRAINER CONFUSION ANALYTICS
============================================================

Trainer clicks:

Confusion Analytics

Show:

Highest confusion topics
Highest confusion timestamps
Affected learners
Replays
Rewinds
Pauses
Doubts
Assessment performance

Example:

--------------------------------------------

Python Functions

04:12

HIGH CONFUSION

Affected learners: 18
Replays: 27
Rewinds: 16
Pauses: 21
Doubts: 11
Average assessment: 61%

--------------------------------------------


============================================================
33. DOUBTS
============================================================

Create a dedicated Doubts section.

Learner can submit:

Topic
Question
Video timestamp
Anonymous option

Form:

ASK YOUR DOUBT

Topic:
[ Python Functions ]

Question:
[ What is the difference between parameters and arguments? ]

Timestamp:
04:12

[✓] Ask anonymously

[SUBMIT DOUBT]


============================================================
34. ANONYMOUS DOUBTS
============================================================

If anonymous:

The UI must show:

Anonymous Learner

instead of the user's name.

Backend can still store the actual user_id.

This is necessary for:

- accountability
- analytics
- competency tracking

But other users must NOT see identity.


============================================================
35. DOUBT ANSWERS
============================================================

A doubt can be:

OPEN
ANSWERED
RESOLVED

Allow trainers/peers to answer.

Show:

Question
Topic
Timestamp
Asked by
Answer
Status

If anonymous:

display:

Anonymous Learner


============================================================
36. CHAT INSIDE DOUBTS
============================================================

The Doubts area must have chat functionality.

Use:

Flask-SocketIO.

There should be a:

"Chat"

or:

"Continue in Chat"

button associated with a doubt/peer connection.

Messages should be real-time.


============================================================
37. NORMAL CHAT
============================================================

Normal chat:

actual names are visible.

Example:

Keerthi:

Can you explain parameters?

Rahul:

Sure. Let's go through the 04:12 section.


============================================================
38. ANONYMOUS CHAT
============================================================

Anonymous chat:

the other participant sees:

Anonymous Learner

not:

Keerthi

The backend may still know the real account.

Allow user to choose:

NORMAL CHAT

or:

ANONYMOUS CHAT

when starting the interaction.


============================================================
39. SOCKET.IO
============================================================

Implement actual working Socket.IO.

Events:

connect
disconnect
join_room
leave_room
send_message
receive_message
typing
message_read

Messages should be stored in SQLite.

Chat UI should contain:

conversation list
message area
message input
send button
anonymous indicator
timestamps
unread count if practical


============================================================
40. SKILL MATCH
============================================================

Create a major feature:

SKILL MATCH

User enters a skill.

Examples:

Python
Java
SQL
DSA
Flask
Machine Learning
Web Development

Example:

[ Python ]

[ FIND SKILL MATCH ]


============================================================
41. RULE-BASED SKILL MATCH ALGORITHM
============================================================

Do NOT use AI.

Use rule-based matching.

Step 1:

Normalize input:

lowercase
trim spaces
remove unnecessary punctuation

Step 2:

Normalize stored skills.

Example:

python
Python Programming
PYTHON

should be related.

Step 3:

Use exact matching.

Exact match:

60 points

Partial/token match:

30 points

Related skill:

15 points

Competency bonus:

up to 10 points

Recent activity:

up to 5 points

Normalize to 100.

Sort descending.

Only show meaningful matches.


============================================================
42. SKILL SYNONYMS
============================================================

Create a small manually maintained map.

Examples:

js → javascript
py → python
ml → machine learning
db → database
sql db → sql

Do not make the matching system dependent on an AI model.


============================================================
43. SKILL MATCH UI
============================================================

Show:

3 people matched

Profile cards:

------------------------------------

Rahul Sharma

Python
Flask
DSA

Competency: 94%

"Strong match because Python is a mastered skill."

[VIEW PROFILE]
[CONNECT]

------------------------------------

The UI should feel like a professional skill network.


============================================================
44. PEER RESCUE
============================================================

Peer Rescue is different from Skill Match.

Skill Match:

User actively searches.

Peer Rescue:

System recommends a peer because the learner appears
to be struggling.

Example:

Learner repeatedly struggles with:

Python Functions

System identifies:

Rahul

Python Functions competency: 94%

and shows:

"You may want to ask Rahul for help."

Buttons:

CONNECT
CHAT


============================================================
45. PEER MATCHING ALGORITHM
============================================================

Rank peers using:

topic match
+
competency
+
recent activity
+
availability

Suggested scoring:

Exact topic/skill = 60
Partial match = 30
Competency bonus = up to 10
Recent activity = up to 5

Avoid recommending the same person repeatedly.

Do not recommend the current learner.


============================================================
46. ASSESSMENTS
============================================================

Create MCQ assessments.

Each lecture/course can have an assessment.

Example:

Question:

What is a Python function?

A. A reusable block of code
B. A database
C. A variable
D. A loop

Store questions in database.

After submission:

calculate score.

Show:

8/10

80%


============================================================
47. TEACH-BACK
============================================================

After completing a topic, ask:

"Explain this topic in your own words."

Example:

"Explain Python functions."

Learner submits text.

For prototype:

allow trainer to manually score it.

Score:

0–100

Store:

response
score
trainer feedback

Do not require AI.


============================================================
48. COMPETENCY ENGINE
============================================================

Calculate competency using a transparent rule-based formula.

Recommended:

Assessment = 40%
Completion = 30%
Teach-back = 20%
Participation = 10%

Formula:

competency =
assessment × 0.40
+
completion × 0.30
+
teach_back × 0.20
+
participation × 0.10

Clamp:

0–100

If a component is unavailable:

redistribute its weight proportionally.

Example:

Python: 86%

Show competency by skill.


============================================================
49. ROLE READINESS
============================================================

Create predefined technical roles.

Example:

Software Developer

Python = 30%
SQL = 20%
DSA = 25%
Git = 10%
Web Development = 15%

Calculate:

role_readiness =
weighted average of skill competencies.

Example:

Software Developer Readiness

78%

Strong:

Python
Git

Needs improvement:

DSA
SQL


============================================================
50. SKILL GAP
============================================================

For each role compare:

current competency
vs
recommended competency.

Example:

SQL:

Current = 61%
Required = 75%

Show:

"Skill gap: 14 points"

This should be visually clear.

============================================================
51. CURRICULUM FEEDBACK
============================================================

Create:

services/curriculum_service.py

Use rule-based logic.

Trigger a curriculum alert when:

confusion is high

AND/OR

doubts are high

AND/OR

assessment performance is low.

Example:

IF:

confusion_score >= 20

AND

doubt_count >= 3

THEN:

create CurriculumAlert.


============================================================
52. CURRICULUM ALERT UI
============================================================

Trainer dashboard:

CURRICULUM ALERT

Python Functions
Parameters & Arguments
04:12

18 learners affected

27 replays
16 rewinds
11 doubts
61% assessment average

Suggested improvement:

"Add a clearer practical example explaining
parameters versus arguments."

Buttons:

APPROVE
DISMISS

This is a rule-based suggestion.

Do not falsely call it AI-generated.


============================================================
53. LEARNER DASHBOARD
============================================================

Create a premium dashboard.

Show:

Welcome back, [Name]

Continue Learning

Course cards

Progress

Competency

Role readiness

Recent doubts

Recommended peers

Notifications

Learning activity


Example:

----------------------------------------

CONTINUE LEARNING

Python Functions

72%

[ CONTINUE ]

----------------------------------------

YOUR COMPETENCY

Python      86%
SQL         78%
DSA         65%

----------------------------------------

ROLE READINESS

Software Developer

78%

----------------------------------------

NEED HELP?

You recently struggled with:

Python Functions

[ FIND A PEER ]

----------------------------------------


============================================================
54. TRAINER DASHBOARD
============================================================

This should be one of the strongest pages.

Top statistics:

Total Learners
Average Competency
Course Completion
Open Doubts
High Confusion Topics
Curriculum Alerts

Use Chart.js.

Charts:

Competency distribution
Course completion
Confusion by topic
Doubts over time
Role readiness if relevant


============================================================
55. ADMIN DASHBOARD
============================================================

Admin is mainly for platform management.

Show:

Total Users
Learners
Trainers
Pending Trainers
Approved Trainers
Courses
Lectures
Doubts
Average Competency

Main section:

TRAINER APPROVALS

Each pending trainer:

Name
Email
Skills
Date

[APPROVE]
[REJECT]


============================================================
56. ADMIN USER MANAGEMENT
============================================================

Admin can:

view users
view trainers
view learners
view account status

If practical:

activate/deactivate accounts.

Do not overcomplicate admin.


============================================================
57. PROFILE
============================================================

The profile button must work.

Create a complete profile page.

Show:

Avatar
Name
Email
Role
Bio
Skills
Interests

Stats:

Courses Completed
Competency
Role Readiness
Doubts Asked

Skills should be displayed as attractive badges.

Show competency bars.

Allow editing:

Name
Bio
Skills
Interests
Profile image/avatar where practical.


============================================================
58. TRAINER PROFILE
============================================================

Trainer profile additionally shows:

Expertise
Skills
Courses created
Approval status
Learner interactions

Admin should be able to see trainer approval status.


============================================================
59. NOTIFICATIONS
============================================================

Create notification system.

Examples:

"Your trainer account has been approved."

"You received a peer help request."

"You received a new message."

"High confusion detected in Python Functions."

"Your competency changed to 82%."

Show unread badge.

Allow marking as read.


============================================================
60. SEARCH
============================================================

Create global search.

Search:

Courses
Lectures
Skills
Topics

Use SQL LIKE queries.

No external search engine.


============================================================
61. HOME PAGE FEATURE VISUALS
============================================================

The landing page should include visual previews of:

Confusion Heatmap
Skill Match
Peer Rescue
Anonymous Doubts
Competency
Role Readiness
Curriculum Feedback

Do not make them fake.

Use realistic UI mock previews populated from demo data.


============================================================
62. MICRO-INTERACTIONS
============================================================

Add:

button hover
card hover
subtle glow
progress animation
number count-up
notification animation
heatmap tooltip
smooth page transitions
active nav state

Keep animations elegant.

Do NOT overanimate.


============================================================
63. RESPONSIVE DESIGN
============================================================

Support:

desktop
laptop
tablet
mobile

Desktop is the main hackathon presentation target.

Do not let mobile completely break.


============================================================
64. ACCESSIBILITY
============================================================

Use:

semantic HTML
labels
keyboard focus
accessible buttons
readable contrast
alt text
clear validation messages


============================================================
65. EMPTY STATES
============================================================

Every major page should have a polished empty state.

Examples:

No doubts yet.

"Ask your first question while learning."

[ ASK A DOUBT ]

No skill matches.

"Try searching for another skill."


============================================================
66. LOADING STATES
============================================================

Create attractive loading indicators for:

video processing
transcript generation
search
dashboard data
chat loading


============================================================
67. ERROR HANDLING
============================================================

Create:

404
403
500

Use the same dark futuristic theme.

Example:

"Looks like this learning path doesn't exist."

[ BACK TO DASHBOARD ]


============================================================
68. VIDEO STORAGE
============================================================

Use:

static/uploads/videos/

The video file must physically exist there.

SQLite stores:

course
lecture
title
topic
duration
video path

Do not store binary video in SQLite.


============================================================
69. ONLY ONE DEMO VIDEO REQUIRED
============================================================

The prototype should be optimized for one main demonstration video.

The system should still support multiple videos architecturally.

I will place/upload one video.

The application should work with that video.

Do not require an online video URL.


============================================================
70. DEMO VIDEO WORKFLOW
============================================================

When the video is uploaded:

1. Save file.
2. Create lecture.
3. Save metadata.
4. Attempt local transcription.
5. Generate timestamped transcript.
6. Save transcript.
7. Make lecture visible to learners.
8. Track viewing behavior.
9. Calculate confusion.
10. Display heatmap.


============================================================
71. SAMPLE TRANSCRIPT
============================================================

For development/demo fallback, create a transcript like:

00:00 Introduction
00:42 What is a function?
02:10 Function definition
04:12 Parameters and arguments
06:40 Return statement
08:15 Practical example
10:30 Common mistakes
12:00 Summary

The actual transcript should preferably come from the uploaded video
through faster-whisper.

Do not hard-code this as the final transcript if automatic
transcription succeeds.


============================================================
72. VIDEO EVENT IMPLEMENTATION
============================================================

Use JavaScript.

Track:

pause

seeked

seeking

play

ended

time position

Detect rewinds.

Example:

previousTime = currentTime

if currentTime < previousTime:

record rewind.

Track repeated visits to segments.

Use a segment size such as:

15 seconds.

Send only meaningful events to backend.


============================================================
73. DOUBT + VIDEO CONNECTION
============================================================

When a learner asks a doubt while watching:

automatically capture current video timestamp.

Example:

Learner is at:

04:12

Clicks:

Ask Doubt

The form automatically contains:

Timestamp: 04:12

This creates a strong connection between:

video behavior
+
doubt
+
confusion.


============================================================
74. CONFUSION + DOUBT CONNECTION
============================================================

If many learners ask doubts around the same timestamp:

increase confusion score.

Example:

Python Functions
04:12

Replays: 27
Rewinds: 16
Doubts: 11

This should make the heatmap stronger.

This is important to the core product story.


============================================================
75. DASHBOARD VISUALIZATION
============================================================

Use Chart.js for:

bar charts
line charts
doughnut charts
progress charts

Avoid excessive charts.

Use charts only when they provide useful insight.


============================================================
76. COLOR CODING FOR ANALYTICS
============================================================

Low:

blue

Moderate:

purple

High:

bright purple / subtle yellow warning accent

Do not use red everywhere.

The entire product must remain visually consistent.


============================================================
77. SEED DATA
============================================================

Create:

scripts/seed.py

Seed:

1 Admin

2 approved trainers

1 pending trainer

8 learners

Courses:

Python Fundamentals
SQL Essentials
Data Structures

Skills:

Python
Java
SQL
DSA
Flask
JavaScript
HTML
CSS
Machine Learning
Git


Create:

sample assessments
sample competencies
sample doubts
sample video events
sample peer connections
sample curriculum alerts
sample notifications

The dashboards should look populated immediately.


============================================================
78. DEMO ACCOUNTS
============================================================

Create easy development accounts.

Example:

Admin:

admin@capacityconnect.com

Trainer:

trainer@capacityconnect.com

Learner:

learner@capacityconnect.com

Use a documented development password.

Clearly mark these as DEMO accounts in README.

Never use these credentials in production.


============================================================
79. COMPLETE DEMO STORY
============================================================

The application must support this exact hackathon demo.

STEP 1:

Open Capacity Connect landing page.

Show:

dark futuristic UI
stars
purple connecting lines
blue/purple interface
feature animation

STEP 2:

Login as learner.

STEP 3:

Open Python Functions.

STEP 4:

Play video.

STEP 5:

Around 04:12:

pause
rewind
replay

STEP 6:

Ask:

"What is the difference between parameters and arguments?"

Choose:

Ask anonymously.

STEP 7:

System stores:

topic
timestamp
anonymous=true

STEP 8:

Learner searches transcript.

Search:

parameters

Result:

04:12 Parameters and Arguments

Click.

Video jumps to 04:12.

STEP 9:

Peer Rescue recommends a strong learner.

Example:

Rahul — Python competency 94%.

STEP 10:

Click Chat.

Socket.IO opens.

STEP 11:

Choose anonymous chat.

The peer sees:

Anonymous Learner

STEP 12:

Learner completes assessment.

Example:

8/10.

STEP 13:

Teach-back response.

STEP 14:

Competency updates.

STEP 15:

Role readiness updates.

STEP 16:

Switch to Trainer Dashboard.

Show:

Python Functions
04:12

HIGH CONFUSION

27 replays
16 rewinds
11 doubts
18 affected learners

STEP 17:

Show Curriculum Alert.

STEP 18:

Trainer approves recommendation.

This demonstrates the complete closed loop.


============================================================
80. RULE-BASED ALGORITHMS SUMMARY
============================================================

The project must use transparent algorithms.

------------------------------------------------------------
SKILL MATCH
------------------------------------------------------------

Exact match = 60
Partial match = 30
Related match = 15
Competency bonus = up to 10
Activity bonus = up to 5

------------------------------------------------------------
CONFUSION
------------------------------------------------------------

rewind × 3
+
replay × 3
+
seek_back × 2
+
pause × 1
+
doubt × 5

------------------------------------------------------------
COMPETENCY
------------------------------------------------------------

assessment × 0.40
+
completion × 0.30
+
teach_back × 0.20
+
participation × 0.10

------------------------------------------------------------
ROLE READINESS
------------------------------------------------------------

weighted average of competency
according to role requirements.

------------------------------------------------------------
CURRICULUM FEEDBACK
------------------------------------------------------------

High confusion
+
high doubts
+
low assessment

→ Curriculum Alert


============================================================
81. IMPORTANT — DO NOT CALL THESE AI FEATURES
============================================================

Unless an actual AI model is implemented, do NOT label:

Skill Match
Confusion Detection
Competency
Role Readiness
Curriculum Feedback

as AI.

Describe them as:

Rule-based
Behavior-based
Data-driven
Explainable

This is actually a strength because the logic is transparent.


============================================================
82. OPTIONAL LOCAL NLP
============================================================

If time permits:

Use scikit-learn TF-IDF + cosine similarity for:

similar doubts
transcript search
related content

This must be optional.

Core application must work without it.


============================================================
83. OFFLINE-FIRST
============================================================

Do NOT spend time implementing a complete offline-first system.

Mention future scope:

Service Worker
IndexedDB
Offline learning
Sync queue

Do not allow this feature to delay the core prototype.


============================================================
84. SECURITY
============================================================

Implement:

password hashing
secure sessions
role authorization
trainer approval authorization
secure filenames
file validation
upload limits
server-side validation
ORM queries
CSRF protection where practical

Never expose anonymous identities.

Never put secrets directly into source code.


============================================================
85. PERFORMANCE
============================================================

Keep the prototype lightweight.

Do not:

send video events every second
create unnecessary database writes
use heavy frameworks unnecessarily
use multiple external APIs

Use AJAX/fetch where useful.

Keep queries efficient.


============================================================
86. TESTING
============================================================

Test:

registration
login
logout
duplicate email
wrong password
role authorization
trainer pending state
trainer approval
trainer rejection
course creation
video upload
transcript
lecture playback
video event tracking
confusion calculation
heatmap
doubts
anonymous doubts
skill matching
peer rescue
normal chat
anonymous chat
assessment
teach-back
competency
role readiness
curriculum alerts
notifications
profile

Also check:

browser console
Flask console
database integrity
broken links
responsive layout


============================================================
87. README
============================================================

Create a complete README containing:

Project overview
Problem statement
Solution
Features
Architecture
Technology stack
Folder structure
Database design
Algorithms
Installation
Virtual environment
Dependencies
Database initialization
Seed data
Demo accounts
Video upload
Transcript generation
Running locally
Socket.IO
Deployment
Future scope

Also explain:

Why SQLite?
Why Flask?
Why Socket.IO?
Why rule-based matching?
How confusion is calculated?
How competency is calculated?
How role readiness is calculated?


============================================================
88. REQUIREMENTS.TXT
============================================================

Only include packages actually required.

Likely:

Flask
Flask-SQLAlchemy
Flask-SocketIO
Werkzeug
python-dotenv
faster-whisper
scikit-learn

Add other packages only if actually used.

Do not add unnecessary packages.


============================================================
89. DEPLOYMENT
============================================================

Prepare the project for deployment.

Use:

Procfile

if needed.

Make Socket.IO deployment-friendly.

Prefer:

async_mode="threading"

Do not require Redis.

Make the application easy to run locally.


============================================================
90. FRONTEND QUALITY CHECK
============================================================

Before final completion, inspect every page.

Check:

Does it look premium?

Are cards aligned?

Are fonts consistent?

Are colors consistent?

Are buttons visually clear?

Are hover states present?

Are loading states present?

Are empty states present?

Are charts readable?

Is the background visible but subtle?

Are stars and purple connection lines working?

Does the right-to-left feature carousel pause on hover?

Does the profile button actually work?

Does the navbar work?

Are mobile layouts acceptable?


============================================================
91. DO NOT USE GENERIC UI
============================================================

Avoid pages that look like:

-----------------------------
Dashboard
-----------------------------
Total users: 20

[card]
[card]
[card]

This is NOT sufficient.

Instead use deliberate visual hierarchy.

Example:

Large dashboard heading

"Understand your learners."

Then:

stat cards
analytics
confusion insights
recent doubts
curriculum alerts

with proper spacing and visual storytelling.


============================================================
92. LANDING PAGE VISUAL STORY
============================================================

The landing page should feel like a product presentation.

Suggested sequence:

HERO

"Learning Should Measure Understanding."

↓

PROBLEM

"Learning problems we've all faced"

↓

SOLUTION

"From learning activity to learning intelligence"

↓

HOW IT WORKS

Learn → Confusion → Doubt → Help → Competency → Improvement

↓

FEATURE CAROUSEL

Confusion Heatmap
Skill Match
Peer Rescue
Anonymous Doubts
etc.

↓

ANALYTICS PREVIEW

Competency
Role Readiness
Confusion

↓

FINAL CTA

"Connect learning with understanding."

[ START LEARNING ]


============================================================
93. RESPONSIVE STAR BACKGROUND
============================================================

The background should remain attractive on mobile.

Reduce:

star count
line count
animation intensity

on smaller screens if necessary.

Do not sacrifice performance.


============================================================
94. IMAGE PLACEHOLDER
============================================================

Create a proper hero image container.

Location:

static/images/hero.png

When I later put my image there:

it should automatically appear.

Use:

object-fit: cover/contain

as appropriate.

Do not break layout if image is absent.


============================================================
95. ICONS
============================================================

Use a consistent icon library.

Possible:

Bootstrap Icons

Use icons for:

dashboard
courses
skill match
doubts
chat
profile
analytics
upload
notifications
settings

Do not mix many unrelated icon styles.


============================================================
96. ACCESSIBLE ERROR MESSAGES
============================================================

Examples:

Invalid email.

Password must be at least X characters.

This email is already registered.

Your trainer account is waiting for approval.

You do not have permission to access this page.

Video upload failed.

Transcript generation failed, but you can add it manually.


============================================================
97. DATABASE INITIALIZATION
============================================================

The application should initialize the database automatically.

Provide a command/script such as:

python scripts/seed.py

It should:

create tables
create demo users
create demo courses
create demo data

It should not duplicate records every time it is run.

Use safe checks.


============================================================
98. CODE ORGANIZATION
============================================================

Keep algorithms in:

services/

Do not put all logic inside routes.

Examples:

confusion_service.py
matching_service.py
competency_service.py
readiness_service.py
curriculum_service.py
transcript_service.py

Routes should handle:

request
validation
calling service
response/rendering


============================================================
99. NO FAKE FUNCTIONALITY
============================================================

Every major button must work.

Do NOT create:

[Skill Match]

and make nothing happen.

Do NOT create:

[Chat]

without actual chat.

Do NOT create:

[Profile]

that opens an empty page.

Do NOT create:

[Approve]

that doesn't update trainer status.

Do NOT create:

[Watch]

that doesn't play the video.

Do NOT create fake analytics unrelated to stored data.

Demo seed data is acceptable, but the application must support
real data too.


============================================================
100. FINAL FEATURE CHECKLIST
============================================================

Authentication
[ ] Register
[ ] Login
[ ] Logout

Roles
[ ] Learner
[ ] Trainer
[ ] Admin

Trainer approval
[ ] Pending
[ ] Approve
[ ] Reject

Profiles
[ ] View
[ ] Edit
[ ] Skills
[ ] Competency

Courses
[ ] Create
[ ] View
[ ] Edit
[ ] Delete

Videos
[ ] Upload
[ ] Store
[ ] Play
[ ] Display on home

Transcript
[ ] Generate
[ ] Store
[ ] Display
[ ] Search
[ ] Timestamp jump

Learning intelligence
[ ] Pause tracking
[ ] Rewind tracking
[ ] Replay tracking
[ ] Confusion score
[ ] Heatmap

Doubts
[ ] Ask
[ ] Anonymous
[ ] Answer
[ ] Resolve

Chat
[ ] Socket.IO
[ ] Normal
[ ] Anonymous
[ ] Persistent messages

Skill Match
[ ] Search
[ ] Rule-based ranking
[ ] Profiles
[ ] Connect

Peer Rescue
[ ] Detect struggling topic
[ ] Find strong peer
[ ] Recommend peer

Assessment
[ ] MCQ
[ ] Score

Teach-back
[ ] Submit
[ ] Trainer score

Competency
[ ] Calculate
[ ] Display

Role readiness
[ ] Roles
[ ] Requirements
[ ] Weighted score
[ ] Skill gaps

Curriculum feedback
[ ] Detect high-confusion topic
[ ] Create alert
[ ] Trainer approval

Notifications
[ ] Create
[ ] Display
[ ] Read/unread

Analytics
[ ] Learner
[ ] Trainer
[ ] Admin

UI
[ ] Dark background
[ ] Stars
[ ] Purple connecting lines
[ ] Blue/purple components
[ ] Premium cards
[ ] Responsive
[ ] Hover effects
[ ] Right-to-left feature carousel
[ ] Carousel pauses on hover
[ ] Hero image area

Documentation
[ ] README
[ ] Requirements
[ ] Setup
[ ] Algorithms
[ ] Demo credentials
[ ] Deployment


============================================================
101. FINAL PRODUCT STORY
============================================================

Everything must connect to ONE central story.

A learner starts learning.

↓

The learner struggles.

↓

Capacity Connect notices unusual learning behavior.

↓

The learner asks a doubt.

↓

The doubt can be anonymous.

↓

The system finds a capable peer.

↓

The learner chats with the peer.

↓

The learner completes an assessment.

↓

The learner explains the concept through teach-back.

↓

The system calculates competency.

↓

The system checks role readiness.

↓

Trainer sees where learners are struggling.

↓

Curriculum feedback identifies problematic content.

↓

Trainer improves the learning material.

This creates a CLOSED LEARNING INTELLIGENCE LOOP.


============================================================
102. FINAL HACKATHON POSITIONING
============================================================

The product should be explainable as:

"Capacity Connect transforms passive learning data into
actionable competency intelligence."

The innovation is NOT:

"We added AI."

The innovation is:

"We connect learning behavior, doubts, peer support,
assessment, competency and curriculum improvement into
one closed loop."


============================================================
103. IMPLEMENTATION INSTRUCTIONS
============================================================

START FROM SCRATCH.

Do NOT ask me to provide an existing project.

First create the complete project structure.

Then implement each phase in order.

For every phase:

1. Create the necessary files.
2. Implement the functionality.
3. Connect it to the database/backend.
4. Create the frontend.
5. Test it.
6. Fix errors.
7. Continue.

Do not stop after creating the architecture.

Do not just explain what should be done.

ACTUALLY BUILD THE APPLICATION.


============================================================
104. IMPORTANT DEVELOPMENT BEHAVIOR
============================================================

If a technology is difficult to configure:

choose the simpler reliable implementation.

If faster-whisper cannot be installed:

keep manual transcript fallback.

If an optional dependency fails:

the rest of the application must continue working.

If a feature can be implemented with simple Python logic:

do that instead of introducing an unnecessary AI service.

Prioritize:

FUNCTIONALITY
+
RELIABILITY
+
UI QUALITY
+
DEMO EXPERIENCE


============================================================
105. FINAL ACCEPTANCE CRITERIA
============================================================

Do not declare the project complete until all of these work:

1. Application starts successfully.
2. Database initializes.
3. Seed data works.
4. Admin login works.
5. Learner registration works.
6. Trainer registration works.
7. Trainer shows pending approval.
8. Admin can approve trainer.
9. Approved trainer can access dashboard.
10. Unapproved trainer cannot access trainer features.
11. Trainer can create course.
12. Trainer can upload video.
13. Video appears in learner-facing content.
14. Video plays.
15. Transcript is available.
16. Transcript timestamps work.
17. Transcript search works.
18. Video events are recorded.
19. Confusion score is calculated.
20. Heatmap is displayed.
21. Doubts work.
22. Anonymous doubts work.
23. Skill Match works.
24. Peer Rescue works.
25. Socket.IO chat works.
26. Normal chat works.
27. Anonymous chat works.
28. Assessment works.
29. Teach-back works.
30. Competency works.
31. Role readiness works.
32. Skill gaps work.
33. Curriculum alerts work.
34. Notifications work.
35. Profile works.
36. Home page dynamically shows content.
37. Feature cards move right-to-left.
38. Feature cards pause on mouse hover.
39. Star background works.
40. Purple connecting lines work.
41. Blue/purple visual system is consistent.
42. Hero image placeholder works.
43. Responsive layout works.
44. Error pages work.
45. No major browser console errors.
46. No major Flask errors.
47. No fake buttons.
48. README is complete.
49. requirements.txt is complete.
50. Deployment configuration is included.


============================================================
106. MOST IMPORTANT FINAL INSTRUCTION
============================================================

Build a COMPLETE, POLISHED, DEMONSTRABLE PRODUCT.

Do not produce a half-built prototype.

Do not prioritize unnecessary AI over functionality.

Do not make the UI generic.

Do not make the project look like a basic student CRUD project.

The final product should feel like a real startup-quality
technical learning platform.

The final visual identity must be:

        DARK / BLACK
             +
        DARK NAVY
             +
          BLUE
             +
         PURPLE
             +
      LIGHT PURPLE
             +
      SUBTLE YELLOW
        ACCENTS ONLY

with:

        ⭐ subtle stars
        ─ purple connecting lines
        ✦ futuristic visual language
        ◈ premium cards
        → smooth animations
        → clean dashboards
        → professional typography

The most important experience is:

LEARN
→ STRUGGLE
→ ASK
→ CONNECT
→ UNDERSTAND
→ MEASURE
→ IMPROVE

BUILD THIS ENTIRE PROJECT FROM SCRATCH.

START WITH PHASE 1 NOW.
============================================================

Do not generate the entire codebase blindly in one response.

Actually implement the project phase by phase.

Start with Phase 1 only:
- create the project
- create the folder structure
- configure Flask
- configure SQLite
- configure SQLAlchemy
- configure Socket.IO
- create requirements.txt
- create the initial base template
- create the initial dark blue/purple UI system
- run/test the application

After verifying Phase 1 works, continue to Phase 2.

For every phase, actually create/modify the files and test the result.
Do not merely tell me what code I should write.
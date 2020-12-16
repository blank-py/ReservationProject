from app import app,db
from datetime import datetime
from app.models import *

# add team
team=Team(id=1,teamName='Admin')
db.session.add(team)
team=Team(id=2,teamName='Staff')
db.session.add(team)
team=Team(id=3,teamName='Teacher')
db.session.add(team)
team=Team(id=4,teamName='Student')
db.session.add(team)


# add admin & users
user=User(id=1,username='admin',fullname='admin',teamId=1)
user.set_password('admin')
db.session.add(user)


# add rooms
room=Room(id=1,roomName='room1')
db.session.add(room)
room=Room(id=2,roomName='room2')
db.session.add(room)
room=Room(id=3,roomName='room3')
db.session.add(room)
room=Room(id=4,roomName='room4')
db.session.add(room)

# add past meetings
meeting=Meeting(id=9,title='past meeting',teamId=4,roomId=2,bookerId=2,date=datetime(2020,12,15),startTime=10,endTime=14,duration=4)
db.session.add(meeting)

# add future meetings
meeting=Meeting(id=15,title='future meeting1',teamId=3,roomId=2,bookerId=2,date=datetime(2020,12, 14),startTime=11,endTime=14,duration=3)
db.session.add(meeting)


participants_user=Participants_user(id=1,meeting='future meeting1',userId=2)
db.session.add(participants_user)
participants_user=Participants_user(id=2,meeting='future meeting1',userId=4)
db.session.add(participants_user)

participants_user=Participants_user(id=3,meeting='future meeting2',userId=2)
db.session.add(participants_user)
participants_user=Participants_user(id=4,meeting='future meeting2',userId=4)
db.session.add(participants_user)

participants_user=Participants_user(id=5,meeting='future meeting3',userId=7)
db.session.add(participants_user)
participants_user=Participants_user(id=6,meeting='future meeting3',userId=4)
db.session.add(participants_user)

participants_user=Participants_user(id=7,meeting='past meeting',userId=2)
db.session.add(participants_user)
participants_user=Participants_user(id=8,meeting='past meeting',userId=7)
db.session.add(participants_user)

db.session.commit()
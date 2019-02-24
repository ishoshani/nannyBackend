# nannyBackend
Backend for nanny App

Step 1 Download Requirements -- Including Python 3

Step 2 Insulation

step 3 Virtual Env 

step 4 Python(3) manage.py CreateSuperUser

step 5 Python(3) manage.py runserver

To test, go to following : http://127.0.0.1:8000

current supported queries

Get to list/ post to create

/host -- all parents/hosts fields = ('id','username','phone','location','kids','password')

/nannys -- all nannys fields = ('username','phone','location','price','password')

/schedules -- all appointments fields = ('host_id','nanny_id','time','payment')

/notes -- All notes fields = ('host_id','nanny_id','text')

make sure to add /at the end when posting. 

/route/id/ to retreive an ID

working on retrieving by other factors



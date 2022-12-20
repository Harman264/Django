from django.shortcuts import render
import mysql.connector as sql
un=''
em=''
ag=''
pwd=''
# Create your views here.
def signaction(request):
    global un,em,ag,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="harman",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="user_name":
                un=value
            if key=="email":
                em=value
            if key=="age":
                ag=value
            if key=="password":
                pwd=value
        c="insert into users Values('{}','{}','{}','{}')".format(un,em,ag,pwd)
        cursor.execute(c)
        m.commit()
    return render(request,'signup_pg.html')
            
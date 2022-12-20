from django.shortcuts import render
import mysql.connector as sql
un=''
pwd=''
# Create your views here.
def loginaction(request):
    global un,pwd
    if request.method=="POST":
        m=sql.connect(host="127.0.0.1",user="root",passwd="harman",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="user_name":
                un=value
            if key=="password":
                pwd=value
        c="select * from users where username='{}' and password='{}'".format(un,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,'welcome.html')    
    return render(request,'index.html')
             

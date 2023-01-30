import mysql.connector

input("What is your name?")
ict_score = input("What was your ICT test score? /100")
maths_score = input("What was your Maths test score? /100")
chemistry_score = input("What was your Chemistry test score? name /100")

#fepfke
mydb = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'Pa$$w0rd',
    database = "testresults"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE testresults")
import pymongo
from pymongo import MongoClient
import json

class dataStudent:

    
    
    
    
    def getAll():
        cluster=MongoClient('mongodb+srv://agnihotriaman0007:LKwAMykwG1HFA4pX@cluster0.eziancx.mongodb.net/')  
        mydb =  cluster["mydatabase"]   
        mycol =mydb["customers"]
        studentList=mycol.find({},{"_id":0})
        j=[]
        for i in studentList:
           j.append(i)
        
        #p=json.dumps(j)
        p={"students":j}
        return p
print(dataStudent.getAll())
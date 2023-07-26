#library management system
"""Books(name,ID,issue date, return date)/
Management(name,contact)/
Student(firstname,lastname,ID,contact)

"""
import random

class LibraryManagemt:
    
    def __init__(self,name,author,ID):
        self.name=name
        self.author=author
        self.ID=random()
        
    def Book(cls,name,author,ID):
        instance=cls(name,author)
        ID=ID.random(100000,99999)
        instance.ID=ID
    
   
class Student(LibraryManagemt):
    
    def __init__(self,name,contact,ID,branch):
        self.name=name
        self.contact=contact
        self.ID=ID
        self.branch=branch
        
    def ReturnBook(cls,name,branch,ID):
        instance=cls(name,branch)
        instance.ID=ID
    
    def IssueBook(cls,name,branch,ID):
        instance=cls(name,branch)
        instance.ID=ID
    
    def CheckReturnDate():
        pass
    
        
class Management(LibraryManagemt):
    
    def __init__(self,name,contact,ID,branch):
        self.name=name
        self.contact=contact
        self.ID=ID
        self.branch=branch
    
    
    def QueryManagement(cls,name,branch,ID):
        instance=cls(name,branch)
        instance.ID=ID




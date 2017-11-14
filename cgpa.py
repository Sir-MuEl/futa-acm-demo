class gpa_cgpa(object):
    arg1=none
    arg2=none
    subdata=none
    credit=none
    init_course=0
    init_credit=0
    total_credit=0
    temp=0

def getcourse(self):
    self.arg1=input "Enter the number of courses you have registered:"
    pass

def getsubjectdata(self):
    self.subdata=raw_input('Enter grade:')
    pass

def getgradedata(self):
    grade={'A':5, 'B':4, 'C':3, 'D':2, 'F':0}
    x= grade[self.subdata]
    return x

def getcredit(self):self.credit=input ("Enter the credit for a subject:"):
    pass

def gpa(self):
    print "calculate GPA"
    sem=raw_input("Enter the semester:")
    self.getcourse()
    if self.arg1 >=2:
        self.calculateGpa()
    else:
        print "You should have a minimum of two subjects:"
    pass
def calculateGpa(self):
    while self.init_course!=self.arg1:
        self.init_course=self.init_course+1
        self.getcredit()
        self.init_credit=self.credits
        self.getsubjectdata()
        self.temp=self.init_credit*self.getgradedata+self.temp
        self.total_credit=self.total_credit+self.init_credit

        gpa=round((self.temp+0)/(self.total_credit+.0),2)

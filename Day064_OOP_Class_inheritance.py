
class job:
  name = None
  salary = None
  hours = None
 
  def __init__(self, name, salary, hours):
    self.name = name
    self.salary = salary
    self.hours = hours

  def desc(self):
    print(f"Job type: {self.name}\nSalary: {self.salary}\nHours worked: {self.hours}")

class doctor(job):
  speciality = None
  years = None
  
  def __init__(self, salary, hours, speciality, years):
    self.name = "Doctor"
    self.salary = salary
    self.hours = hours
    self.speciality = speciality
    self.years = years
    
  def desc(self):
    print(f"Job type: {self.name}\nSalary: {self.salary}\nHours worked: {self.hours}\nSpeciality: {self.speciality}\nYears of Experience:{self.years} ")
     
class teacher(job):
  subject = None
  position = None
  
  def __init__(self, salary, hours, subject, position):
    self.name = "Teacher"
    self.salary = salary
    self.hours = hours
    self.subject = subject
    self.position = position
    
  def desc(self):
    print(f"Job type: {self.name}\nSalary: {self.salary}\nHours worked: {self.hours}\nSubject: {self.subject}\nPosition: {self.position}")
     
lawyer = job("Lawyer", "Million", "60")
teac = teacher("$50.000", "45+", "Computer Science", "Classroom Teacher")
doc = doctor("$120.000", "50+", "Pediatric Consultant", "7")

print("🌟 Jobs Board 🌟")
print()
lawyer.desc()
print()
teac.desc()
print()
doc.desc()

#Sets

my_set = {"Hello", "World", 1, 2, 2.3} #Immutable, unordered, Unique
# print(my_set, type(my_set) == type(set({"Bye", "See you along"})))
# print(set({"Hi", 123}))

def dissect_objects(obj):
    for item in obj:
        print(item)



#tuples
my_tuple = ("Luckista", "Ndoda", 23, "Ace", 2.9)

#print(my_tuple, my_tuple[2], my_tuple[2:4], type(my_tuple) == type(tuple((10,20))))
#my_tuple[2] = 24 TypeError - Object does not support item assignment



#list
my_list = ["Thamsanqa", "Thami", 1, 2.3]
my_list[3] = 2.9
#print(my_list, type(my_list)==type(list(("Hello", "There"))), my_list[2], my_list[1:3], my_list[3])

my_list2 = list(my_list)
my_list2.append("Other")
#print(my_list2)



# dissect_objects(my_tuple)

def details(name, age):
    print("Hello ", name, ",")
    print("How is ", age, " for you?")
 
def returnSomething():
       return "Hello"

# print(returnSomething())

# for i in range(1,5):
#     print(i, end="-")

# Checking for even or odd

# for i in range(1,21):
#     if i % 2 == 0:
#         print(i, " is even.")
#     else:
#          print(i, " is odd.")

# from sys import argv

class Student:
     # class var
    school_name = "Percy Mdala High"

     #constructor
    def __init__(self, name, age):
          #instace variables
          self.name = name
          self.age = age
    
    #instance method
    def show(self):
        print(self.name, self.age, Student.school_name)
    
    @classmethod
    def change_School(cls, name):
        cls.school_name = name
    
    @staticmethod
    def find_notes(subject_name):
         return ['chapter 1', 'chapter 2', 'chapter 3']

jessa = Student("jessa", 22)

jessa.show()
print(jessa.find_notes("Maths"))
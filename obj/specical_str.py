class Student:
    def __init__(self,name):
        self.__name = name;

    def __str__(self):
        return "Student Object(name: %s)" % self.__name;
<<<<<<< HEAD
    __repr__ = __str__;
vito = Student("vito");
print(vito);
=======

vito = Student("vito");
print(vito);
>>>>>>> 5839a9e4e07fa0f7af325a630f922ade1e43c2d1


class Student():
    def __init__(self,name,sno):
        self.name = name
        self.sno = sno
        print(self)
    def run(self,hobby):
        print('{}学号是{}喜欢{}'.format(self.name,self.sno,hobby))
        print(self)
        print(self.name)
        print(hobby)


a = Student('czm','07')
a.run('math')
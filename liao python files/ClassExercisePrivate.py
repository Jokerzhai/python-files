class Student(object):
    
        def __init__(self,name,score):
            self.__name  = name  # name private , only indoor access
            self.__score = score

        def print_score(self):
            print('%s: %s' % (self.__name,self.__score))
        
        def get_grade(self):
            if self.score >= 90:
                return 'A'
            elif self.score >= 60:
                return 'B'
            else:
                return 'C'
bart = Student('Bart Simpson',59)
#print(bart)
print(bart.__name)
print(bart.score)

print (bart.print_score())
print bart.name,bart.score,bart.get_grade()
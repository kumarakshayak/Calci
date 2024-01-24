from add_func import addClass
class calculator:

    def __init__(self,number1,number2):
        self.num1=number1
        self.num2=number2
    def add(self):
        return addClass.add(self.num1,self.num2)
    
    
if __name__=="__main__":
    a=10
    b=2
    cur_obj=calculator(a,b)
    print(cur_obj.add())


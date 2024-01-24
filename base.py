from add_and_multi import add_multi

class calculator:

    def __init__(self,number1,number2):
        self.num1=number1
        self.num2=number2
    def add(self):
        return add_multi.add(self.num1,self.num2)
    def multiply(self):
                 return add_multi.multi(self.num1,self.num2)
    
if __name__=="__main__":
    number1=10
    number2=2
    cur_obj=calculator(number1,number2)
    print(cur_obj.add())
    print(cur_obj.multiply())


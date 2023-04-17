'''
Stack's funct.'
1. Push- increase the TOP var. by 1
2. Pop- decrease value of TOP by 1
3. Peek-Return the top value in stack
'''


class stack:

    'What does a Constructor do ?'
    def __init__(self):
        #initializing an array called stack for all objects and all objects have the var. called top
        # which is intiliased as -1
        self.stack = []
        self.Top=-1
    def Push(self, value):
        self.Top +=1
        self.stack .append(value)

    def Pop(self):
        self.Top-=1
        self.stack.pop()

    def Peek(self):
        return self.stack[self.Top]
#printing the stack will require a for loop for teh iteration from Top
    def print_stack(self):
        for i in range(self.Top,-1,-1):
            print(self.Top, "value is ")
            if i == self.Top:
                print( "value inside if loop ",i)
                print (self.stack[i], "<------Top's value")
            else:
                print("value inside else loop ", i)
                print(self.stack[i])


R= stack()
R.Push(20)
R.Push(4)
R.Push(5)
R.Push(28)
#R.Push(89)
R.print_stack()

'''Application of teh above code is REVERSING the word using Stack'''


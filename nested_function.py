# nested Function
#Variable Scope:LEGB(Local, Enclosing, Global, Builtins) Rule

"""def Greetings(name,msg):
    def Message():
        return 'Hi {0},{1}'.format(name,msg)
    return Message()

x=Greetings('Abhay','Kumar')
print(x)"""


def Greetings(name):
    def inner_fun(msg):
        return f'Hi {name},{msg}' #F-string
    return inner_fun

#creating message function
#x=Greetings('Rahul')


msg=['Good Morning','Complete task 1','send a mail to me']

vikas=Greetings('Vikas') #readable form
abhay=Greetings('Abhay')

for message in msg:
    output=vikas(message)
    print(output)
    output1=abhay(message)
    print(output1)
    
    
    
for message in msg:
    output3=Greetings('Santosh')(message)
    print(output3)
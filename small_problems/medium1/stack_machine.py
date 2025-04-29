"""
n: Place an integer value, n, in the register. Do not modify the stack.
PUSH : Push the current register value onto the stack. Leave the value in the register.
ADD : Pop a value from the stack and add it to the register value, storing the result in the register.
SUB : Pop a value from the stack and subtract it from the register value, storing the result in the register.
MULT : Pop a value from the stack and multiply it by the register value, storing the result in the register.
DIV : Pop a value from the stack and divide the register value by the popped stack value, storing the integer result back in the register.
REMAINDER : Pop a value from the stack and divide the register value by the popped stack value, storing the integer remainder of the division back in the register.
POP : Remove the topmost item from the stack and place it in the register.
PRINT : Print the register value.



"""
def is_number(string):
    if '-' in string:
        if string.split('-')[1].isdigit():
            return (int(string.split('-')[1]) * -1)
    elif string.isdigit():
        return int(string)
    else:
        False

def minilang(commands):
    stack = []
    register = 0

    command_list = commands.split()
    for command in command_list:
        if is_number(command):
            register = int(command)

        match command:
            case 'PRINT':
                print(register)
            case 'PUSH':
                stack.append(register)
            case 'MULT':
                register = stack.pop() * register
            case 'ADD':
                register = stack.pop() + register
            case 'SUB':
                register =  int(register) - int(stack.pop())
            case 'DIV':
                register = int(register // stack.pop())
            case 'REMAINDER':
                register = int(register % stack.pop())
            case 'POP':
                register = stack.pop()


minilang('PRINT')
# # 0

(minilang('5 PUSH 3 MULT PRINT'))
# 15

# (minilang('5 PRINT PUSH 3 PRINT ADD PRINT'))
# 5
# 3
# 8

# minilang('5 PUSH POP PRINT')
# # 5

# minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# # 5
# # 10
# # 4
# # 7

# minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# # 6

# minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# # 12

# minilang('-3 PUSH 5 SUB PRINT')
# # 8

# minilang('6 PUSH')
# # (nothing is printed)

# Creates a command that acts as a small input program
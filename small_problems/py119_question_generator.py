
import random 

questions_list = ['e1.1', 'e1.2', 'e1.3', 'e1.4', 'e1.5', 'e1.6', 'e1.7', 'e1.8', 'e1.9', 'e1.10', 'e1.11',
                  'e2.1', 'e2.2', 'e2.3', 'e2.4', 'e2.5', 'e2.6', 'e2.7', 'e2.8', 'e2.9', 'e2.10',
                  'e3.1', 'e3.2', 'e3.3', 'e3.4', 'e3.5', 'e3.6', 'e3.7', 'e3.8', 'e3.9', 'e3.10',
                  'e4.1', 'e4.2', 'e4.3', 'e4.4', 'e4.5', 'e4.6', 'e4.7', 'e4.8', 'e4.9', 'e4.10',
                  'e5.1', 'e5.2', 'e5.3', 'e5.4', 'e5.5', 'e5.6', 'e5.7', 'e5.8', 'e5.9', 'e5.10',
                  'd1.1', 'd1.2', 'd1.3', 'd1.4', 'd1.5', 'd1.6', 'd1.7', 'd1.8', 'd1.9', 'd1.10',
                  'm1.1', 'm1.2', 'm1.3', 'm1.4', 'm1.5', 'm1.6', 'm1.7', 'm1.8', 'm1.9', 'm1.10',
                  'm2.1', 'm2.2', 'm2.3', 'm2.4', 'm2.5', 'm2.6', 'm2.7',
                  'a1.1', 'a1.2', 'a1.3', 'a1.4', 'a1.5', 'a1.6', 'a1.7',
                  'pp1.1', 'pp1.2', 'pp1.3', 'pp1.4', 'pp1.5', 'pp1.6', 'pp1.7', 'pp1.8', 'pp1.9', 'pp1.10', 'pp1.11',
                  'pp1.12', 'pp1.13', 'pp1.14', 'pp1.15', 'pp1.16', 'pp1.17', 'pp11.8', 'pp1.19', 'pp1.20',
                  'spot1.1', 'spot1.2', 'spot1.3', 'spot1.4', 'spot1.5', 'spot1.6', 'spot1.7', 'spot1.8', 'spot1.9', 'spot1.10', 'spot1.11',
                  'spot1.12', 'spot1.13', 'spot1.14', 'spot1.15', 'spot1.16', 'spot1.17', 'spot11.8', 'spot1.19', 'spot1.20',
                  'spot1.21', 'spot1.22', 'spot1.23', 'spot1.24', 'spot1.25', 'spot1.26', 'spot1.27', 'spot1.28', 'spot1.29', 'spot1.30', 'spot1.31',
                  'spot1.32', 'spot1.33', 'spot1.34', 'spot1.35', 'spot1.36', 'spot1.37', 'spot1.38', 'spot1.39', 'spot1.40','spot1.41',
                  'spot1.42', 'spot1.43', 'spot1.44', 'spot1.45', 'spot1.46', 'spot1.47', 'spot1.48',]

run_program = True

while run_program:

    question_number = input('how many questions? ')

    for _ in range(int(question_number)):
        print(questions_list[random.randint(0, len(questions_list) - 1)])
    
    response = input('more questions? ')

    if response == 'n':
        break

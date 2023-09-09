import random, time

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_QUESTIONS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + ' ' +  operator + ' ' + str(right)
    answer = eval(expr)
    return answer, expr

input('Press Enter to start')
print('--------------------------')

wrong = 0

start_time = time.time()

for i in range(TOTAL_QUESTIONS):
    answer, expr = generate_problem()
    while True:
        guess = input('Problem # ' + str(i + 1) + ' : ' + str(expr) + ' = ')
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print('Nice work! You finished the test in ', total_time, 'seconds')
print('--------------------------')

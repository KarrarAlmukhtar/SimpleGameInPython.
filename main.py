print('Hello and welcome to our game!')
kr = input('Are you ready to play (Yes/No): ')
score = 0
total_q = 4

if kr.lower() == 'no' or kr.lower() == 'No' or kr.lower() == 'NO':
    print('Ok, You can back when you be ready :)')

if kr.lower() == 'yes' or kr.lower() == 'Yes' or kr.lower() == 'YES':
    kr = input('1. What is the best programming language? ')
    if kr.lower() == 'python' or kr.lower() == 'Python' or kr.lower() == 'PYTHON':
        score += 1
        print('correct!')
        print('Good choice.')
    else:
        print('Incorrect.')

    kr = input('2. What is 2 + 9 - 9 - 1? ')
    if kr == '18':
        score += 1
        print('correct!')
    else:
        print('Incorrect.')

    kr = input('3. What is better 1050ti or 1060 (graphics card)? ')
    if kr.lower() == '1050ti' or kr == '1050TI':
        score += 1
        print('correct!')
    else:
        print('Incorrect.')

    kr = input('4. Who came second in the stanly cup finals? ')
    if kr.lower() == 'vegas' or kr.lower() == 'newyork':
        score += 1
        print('correct!')
    else:
        print('Incorrect.')

    print("Thank you for playing, you got", score, "questions correct.")
    mark = (score/total_q) * 100
    print('Mark: ', str(mark) + '%')
print('Goodbye..')
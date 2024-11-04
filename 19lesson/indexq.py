# def texting():
#     text = input("write text: ")
#     x = text.split()
#     sum = 0
#     for i in x:
#         sum += len(i)
#     print(sum/len(x))
# # texting()
# # ,

def millionare():
    print("Answer to the questions: ")
    questions = {
        'What is the highest mountain?': {
            'options': {
                'A': 'Everest',
                'B': 'K2',
                'C': 'Kilimanjaro',
                'D': 'Fujiyama',
            },
            'Answer': 'A'
        },
        'What is the capital of France?': {
            'options': {
                'A': 'Berlin',
                'B': 'Madrid',
                'C': 'Paris',
                'D': 'Rome'
            },
            'Answer': 'C'
        },
        'What is the largest ocean on Earth?': {
            'options': {
                'A': 'Atlantic Ocean',
                'B': 'Indian Ocean',
                'C': 'Arctic Ocean',
                'D': 'Pacific Ocean',
            },
            'Answer': 'D'
        },
        'Who wrote "Romeo and Juliet"?': {
            'options': {
            'A': 'Charles Dickens',
            'B': 'Mark Twain',
            'C': 'William Shakespeare',
            'D': 'Jane Austen'},
            'Answer': 'C'
        },
        'What is the chemical symbol for gold?': {
            'options': {
            'A': 'Ag',
            'B': 'Au',
            'C': 'Pb',
            'D': 'Fe'},
            'Answer': 'B'
        },
        'Which planet is known as the Red Planet?': {
            'options': {
            'A': 'Earth',
            'B': 'Mars',
            'C': 'Jupiter',
            'D': 'Venus'},
            'Answer': 'B'
        },
        'What is the smallest prime number?': {
            'options': {
            'A': '0',
            'B': '1',
            'C': '2',
            'D': '3'},
            'Answer': 'C'
        },
        'What is the capital city of Japan?': {
            'options': {
            'A': 'Seoul',
            'B': 'Beijing',
            'C': 'Tokyo',
            'D': 'Bangkok'},
            'Answer': 'C'
        },
        'Who painted the Mona Lisa?': {
            'options': {
            'A': 'Vincent Van Gogh',
            'B': 'Pablo Picasso',
            'C': 'Leonardo da Vinci',
            'D': 'Claude Monet'},
            'Answer': 'C'
        },
        'Which gas do plants absorb from the atmosphere?': {
            'options': {
            'A': 'Oxygen',
            'B': 'Nitrogen',
            'C': 'Carbon Dioxide',
            'D': 'Hydrogen'},
            'Answer': 'C'
        }
    }
    flag = True
    money = 100
    while  flag:
        for i in questions:
            question = input(f'{i}: ')
            if question == questions[i]['Answer']:
                money *=2
                print(f'nice you have {money}$')
            else:
                flag = False
                money = 1
                print('dolban, you have 0$')
                break

# millionare()

def words():
    capital = ['Tashkent', 'Toronto', 'Adu-dabi', 'Moscow', 'Wales', 'Severa']
    flag = True
    while flag:
        for i in capital:
            capitalist = input("Write capital: ").casefold()
            if capitalist in capital:
                flag 
                print(capital)
words()


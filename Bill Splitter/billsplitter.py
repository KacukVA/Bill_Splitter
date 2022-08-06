import random
people_number = int(input('Enter the number of friends joining (including you):\n'))
who_is_lucky = 0
lucky_person = ''
people_dic = {}
output = 'No one is joining for the party'
if people_number > 0:
    for i in range(people_number):
        if i == 0:
            name = input('Enter the name of every friend (including you), each on a new line:\n')
        else:
            name = input()
        people_dic.update({name: 0})
    output = people_dic
    bill_value = abs(float(input('Enter the total bill value:\n')))
    answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if answer == 'Yes':
        lucky_person = random.choice(list(people_dic.keys()))
        people_dic.pop(lucky_person)
        who_is_lucky = 1
        print(f'{lucky_person} is th lhe lucky one!')
    else:
        print('No one is going to be lucky')
    split_amount = round((bill_value / len(people_dic)), 2)
    for _ in people_dic:
        people_dic[_] = split_amount
    if who_is_lucky == 1:
        people_dic.update({lucky_person: 0})
    print(people_dic)
else:
    print(output)

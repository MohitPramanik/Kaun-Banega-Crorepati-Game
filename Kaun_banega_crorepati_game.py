level = [0, 1000, 2000, 4000, 6000, 10000, 12000, 14000, 16000, 20000, 25000]

questions = {'1. What is the Capital of India' : 'Delhi',
             '2. How many planets are there in the solar system': 8,
             '3. Who was founder of Computer': 'Charles Babbage',
             '4. Who is the Prime minister of India': 'Narendra Modi',
             '5. Who is the CM of Jharkhand': 'Hemant Soren',
             '6. What is the capital of Jharkhand': 'Ranchi',
             '7. How many continents are there in the world': 7,
             '8. Heat is a form of _________' : 'Energy',
             '9. Who was founder of Python Programming Language': 'Guido Van Rossum',
             '10. India is _______________': 'a country'}

options = {1: ['Delhi', 'Ranchi', 'Jaipur', 'Udaynagar'],
           2: [10, 9, 8, 7],
           3: ['Shubhash Chandra Bose', 'Jaya Kishori', 'Krishna Bhagwan', 'Charles Babbage'], 
           4 : ['Lalu Prasad Yadaw', 'Narendra Modi', 'Jaya Bachchan', 'Kumar Sanu'], 
           5: ['Raghuwar Das', 'Rahul Gandhi', 'Nitish Yadaw', 'Hemant Soren'], 
           6: ['Delhi', 'Ranchi', 'Jaipur', 'Udaynagar'], 
           7: [10, 9, 8, 7], 
           8: ['Energy', 'Radio waves', 'Fun element', 'plastic'], 
           9: ['Charles Babbage', 'Guido Van Rossum', 'Dannis Ritchie', 'None of these'], 
           10: ['my country', 'hindu nation', 'a place', 'a country']}

questionNumber = 1

for question in questions:
    # Printing question and its Price Money
    print(f"\n\nQuestion for Rs. {level[questionNumber]}\n\n{question}")

    # storing the options in a 'check' dictionary 
    check = {'a': options[questionNumber][0], 'b': options[questionNumber][1], 'c': options[questionNumber][2], 'd': options[questionNumber][3]}

    # Printing options
    for key, value in check.items():
        print(f"\t{key}. {value}")
    
    answer = input("Answer : ")

    # Matching answers with the correct option
    if(check[answer] == questions[question]):
        print(f"Congrats, You won Rs. {level[questionNumber]}")
        questionNumber += 1
    else:
        print("Incorect answer, You Lose")
        break
    input("Press enter to continue...")
print(f"You won a total of {level[questionNumber-1]}")
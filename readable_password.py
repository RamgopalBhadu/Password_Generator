import random

num = ['1','2','3','4','5','6','7','8','9','0']
special_char = ['!','@','#','$','%','^','&','*']

wordlist = []

with open("wikipedia_text.txt",'r',encoding='utf-8') as file:
    data = file.readlines()

    for line in data:
        words = line.split()

        for item in words:
            if len(item)>=4:
                wordlist.append(item.capitalize())
char =random.choice(wordlist)
password=char+random.choice(special_char)+str(random.randint(10,999))
print(password)

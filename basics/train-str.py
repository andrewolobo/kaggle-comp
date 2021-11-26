x = 'Pluto is a planet'
y = "Pluto is a planet"
x == y

print("Pluto's a planet!")
print('My dog is named "Pluto"')

print(str("1"))

for i in range(10):
    print(i)


if(not str.isdigit("1")):
    print(True)

if 'word' in 'keyword':
    print("word")

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]

for word in doc_list:
    wo = word.split(' ')
    for w in wo:
        w
        print(w.replace('.', ''))
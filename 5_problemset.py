# problem 1
words = {
    "apple": "A fruit that is typically red, green, or yellow and is known for its sweet taste.",
    "banana": "A long curved fruit that grows in clusters and has soft pulpy flesh and yellow skin when ripe.",
    "orange": "A round citrus fruit with a thick orange skin and juicy, sweet flesh.",
    "strawberry": "A small red fruit with a sweet taste and tiny seeds on its surface."
}
word = input("Enter a fruit you wanna know about: ")
print(words[word])

# problem 2
number = set()
a = input("Enter a number : ")
number.add(int(a))
a = input("Enter a number : ")
number.add(int(a))
a = input("Enter a number : ")
number.add(int(a))
a = input("Enter a number : ")
number.add(int(a))
a = input("Enter a number : ")
number.add(int(a))
a = input("Enter a number : ")
number.add(int(a))
a = input("Enter a number : ")
number.add(int(a))
a = input("Enter a number : ")
number.add(int(a))
print(number)

# problem 3
language = {}
name = input("Enter a name: ")
lang = input("Enter a language : ")
language.update({name: lang})
name = input("Enter a name: ")
lang = input("Enter a language : ")
language.update({name: lang})
name = input("Enter a name: ")
lang = input("Enter a language : ")
language.update({name: lang})
name = input("Enter a name: ")
lang = input("Enter a language : ")
language.update({name: lang})
print(language)

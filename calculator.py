filename = '/home/o.derun/pybot/alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, file " + filename + "not exist."
    print(msg)
else:
    #количество слов в тексте
    words = contents.split()
    num_words = len(words)
    #преобрахование к нижнему регистру
    cont = contents.lower()
    count = cont.count('a ')
    print(count)
    print("Файл", filename, "содержит ", str(num_words), "слова.")
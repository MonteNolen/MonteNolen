def write_txt():
    with open('text.txt', 'a+') as f:
        f_name = input()
        l_name = input()
        s = f_name.title() + ' ' + l_name.title() + '\n'
        f.write(s)

def read_txt():
    f = open('text.txt', 'r')
    line = f.readline()
    i = 1
    while line:
        print("Строка:", i, '\t' + 'Имя и Фамилия:' + '\t' + line)
        i += 1
        line = f.readline()  

#write_txt()
read_txt()
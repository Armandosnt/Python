file = open('text.txt', 'a')
file.write("hello world!!!!!!!!!\n")
file.close()

print("sdadasdsadsaddas", file=test)
test.close()


with open('text.txt','r') as file:
    info = file.readlines()
    print(info)
filename = "guest_book.txt"
with open(filename, 'a') as file_Object:
    while 1:
        s = input("Введите имя!\n")
        if s == "q":
            break
        p = "Привет " + s + "!\n"
        print(p)
        file_Object.write(p)
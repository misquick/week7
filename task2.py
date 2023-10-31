file_name = "romeo.txt"  
try:
    with open(file_name, 'r') as file:
        word_list = []
        for line in file:
            words = line.split()
            for word in words:
                if word not in word_list:
                    word_list.append(word)
        word_list.sort()
        output = "[" + ', '.join(["'{}'".format(word) for word in word_list]) + "]"
        print(output)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")

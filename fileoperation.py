# Question (1)

def write(filepath, content):
    if not isinstance(content, (str, list)):
        raise TypeError("Content must be a string or a list of strings.")

    with open(filepath, 'w') as file:
        if isinstance(content, list):
            file.writelines(content)
        else:
            file.write(content)

# Question (2)

def append(filepath, newcontent):
    if not isinstance(newcontent, (str, list)):
        raise TypeError("New content must be a string or a list of strings.")

    with open(filepath, 'a') as file:
        if isinstance(newcontent, list):
            file.writelines(newcontent)
        else:
            file.write(newcontent)


# Question (3)

def read(filepath, option):
    with open(filepath, 'r') as file:
        if option == 'all':
            return file.read()
        elif isinstance(option, int):
            return file.read(option)
        elif option == 'line':
            return file.readline()
        elif option == 'lines':
            return file.readlines()
        else:
            raise ValueError("Invalid option provided. Use 'all', an integer, 'line', or 'lines'.")
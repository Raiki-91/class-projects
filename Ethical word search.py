def file_to_list():  # function locating lookup word and reading them as str
    words_to_look_for = open(str(input('enter a <file_name>: ')+'.txt'),'r')
    read_words = words_to_look_for.read()
    words_list = read_words.split('\n')
    return words_list

def main():
    words = file_to_list()
    with open(r'words.txt', 'r') as f:
        content = f.read()
        for word in words:
            if word in content:
                print('{} exist in a file'.format(word))
main()

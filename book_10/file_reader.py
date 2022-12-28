# title = "Alice in WonserLand"
# title = title.split()
# print(*title, sep='\n')


def count_words(filename):
    """Подсчет приблизительного количества строк в файле."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['prog1.txt', 'Повареная книга Анархиста', 'pi_digits.txt']
for filename in filenames:
    count_words(filename)





# filename = 'prog1.txt'
#
# with open(filename, 'a') as file_object:
#     file_object.write("I Strong.\n")
#     file_object.write("I \n")
#     file_object.write("Doo yet.\n")






# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print(pi_string[:40])
# print(len(pi_string))

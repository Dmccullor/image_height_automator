import os
from PIL import Image

cwd = (f'{os.getcwd()}/images')
file_to_save = os.path.join('output.txt')
data = []
index = 0
max = 0

for i in os.scandir(cwd):
    img = Image.open(i.path)
    filepath = img.filename.split('\\')
    filename = filepath[-1]
    data.insert(index, [filename, img.height])

    if len(filename) > max:
        max = len(filename)

    index += 1
    
headers = "|" + "Filename" + (" " * (max - 8)) + "|" + " Height|\n" + ("-" * (max + 10)) + "\n"
print(headers)

index = 0

with open(file_to_save, 'w') as txt_file:
    txt_file.write(headers)
    for entry in data:
        string = "|" + str(data[index][0]) + (" " * (max - len(data[index][0]))) + "|" + (" " * (7 - len(str(data[index][1])))) + str(data[index][1]) + "|\n"
        print(string)
        txt_file.write(string)
        index +=1
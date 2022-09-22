fi = open('first_file.txt', 'w')
line = fi.write('Напишитеабв программу, удаляющую из текстаабв все слова, содержащие абв')
fi.close()
fi = open('first_file.txt', 'r')
line = fi.read()
fi.close()
result = ' '.join(filter(lambda x: 'абв' not in x, line.split()))
print(result)

with open('file.txt', 'w', encoding='utf-8') as f:
    f.write(result)
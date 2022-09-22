line = "Напишитеабв программу, удаляющую из текстаабв все слова, содержащие абв"
print( " ".join(filter(lambda x: "абв" not in x, line.split())))
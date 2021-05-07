filename = 'LearningPython'

with open(filename) as File_Object:
    for line in File_Object:
        print(line.rstrip().replace('Python', 'C'))
#Write and Append Data to a File

a = input('Enter text to write to the file: ')

file = open('.\output.txt','w')
writing_file = file.write(a)
writing_file = file.write('\n')
print('Data successfully written to output.txt.\n')
file.close()

b= input('Enter additional text to append: ')

file = open('.\output.txt','a')
appending_file = file.write(b)
print('Data Successfully appended.\n')
print('Final content of output.txt:')
file.close()

file= open('.\output.txt','r')
reading_file = file.read()
print(reading_file)
file.close()


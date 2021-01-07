def store_the_file(file_name):
try:
   f = open(file_name, mode= 'a' encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
   
the_file_name = "test_file.txt"

store_the_file(the_file_name)

import os.path

file_name = 'git.jpg'

if file_name[-1] == '/':
    file_name = file_name[:-1]

if '/' in file_name:
    file_name = file_name.split('/')[-1] 

file_preface, dot, file_extension = file_name.partition('.')
resized_name = f'{file_preface}_RESIZED.{file_extension}'  

if os.path.isfile(resized_name):
    name_exists_in_dir = True
    attempts = 1
    while name_exists_in_dir:
        resized_name = f'{resized_name.split(dot)[0]} ({str(attempts)}).{file_extension}'
        if not os.path.isfile(resized_name):
            name_exists_in_dir = False
        else:
            resized_name = f'{file_preface}_RESIZED.{file_extension}'
            attempts += 1 
print(resized_name)



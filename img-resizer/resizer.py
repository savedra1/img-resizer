from PIL import Image

import sys
import os.path

def main():
    if not len(sys.argv) > 1:
        sys.exit('No img path provided.')
    elif len(sys.argv) > 5: 
        sys.exit('Too mangs args provided.')
    elif sys.argv[1] == '--help':
        print("""Available commands:\n
        | resizer <img path> : Saves specified image as 512x512px in CWD\n
        | resizer <img path> small : Saves specified image as 512x512px in CWD\n   
        | resizer <img path> medium : Saves specified image as 1000x1000px in CWD\n    
        | resizer <img path> big : Saves specified image as 2000x2000px in CWD\n
        | resizer <img path> custom <int> <int> : Saves specified image as <int>x<int>px in CWD\n      
        """)

    try:
        img = Image.open(sys.argv[1])
    except Exception:
        print(f'Could not open image {img}')
        sys.exit()

    if len(sys.argv) > 2 :
        match sys.argv[2]:
            case "small":
                size = (512, 512)
            case "medium":
                size = (1000, 1000)
            case "big":
                size = (2000, 2000)
            case "custom":
                try: 
                    size = (int(sys.argv[3]), int(sys.argv[4]))
                except Exception:
                    sys.exit('Not enough args provided for custom. Needs int int.')
            case _:
                size = (512, 512)
    else:
        size = (512, 512)
    
    try:
        img = img.resize(size)
    except Exception as err:
        sys.exit(f'Failed to save image: {err}')

    file_name = sys.argv[1]
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

    try:
        img.save(resized_name)
        print(f'Saved image as {resized_name}')
    except Exception:
        print(f'Failed to save img as {resized_name}.')

if __name__ == "__main__":
    main()

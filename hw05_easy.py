# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys
import shutil
def NewDirs ():
    for i in range(1,10):
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print('Такая директория уже существует')

def DelNewDirs():
    place_files = os.listdir()
    h = 0
    for q in place_files:
        for i in range(1, 10):
            if "dir_{}".format(i) in q and os.path.isdir(q):
                os.removedirs(q)
                h += 1
            else:
                pass
    print("\t\tУдалено", h, "директорий")
#NewDirs()
#DelNewDirs()
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def showmedirs():
    main_path = os.getcwd()
    for _ in os.listdir(main_path):
        print(_)

#showmedirs()
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file(first_file,backup_file):
    shutil.copy(first_file,backup_file)

first_file = sys.argv[0]
backup_file = first_file + '.backup'
copy_file(first_file,backup_file)
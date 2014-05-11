import os, shutil

def sort():
    files = os.listdir("./original_files/")

    for each in files:
        file = "./original_files/%s" % each
        first_letter = each[0]
        dir_path = "./%s/" % first_letter
        if os.path.exists(dir_path) == False:
            os.mkdir(dir_path)
            shutil.move(file, dir_path)
        else:
            shutil.move(file, dir_path)

sort()
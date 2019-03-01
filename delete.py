import os

def Work(mydir):
    print('Deleting files...')
    filelist = [ f for f in os.listdir(mydir) if f.endswith(".jpeg") ]
    for f in filelist:
        os.remove(os.path.join(mydir, f))

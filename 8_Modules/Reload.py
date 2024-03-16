import importlib
import filechanges
def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass


for i in range(5):
    changes()
    input("print enter to hit changes")
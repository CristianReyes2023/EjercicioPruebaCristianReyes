import json

def crearInfo(*args):
    if(checkFile(args[0])==False):
        with open('data/'+args[0], 'w') as write_file:
            json.dump(args[1], write_file,indent=4)
            write_file.close()
    else:
        with open('data/'+args[0], 'r+') as file:
            file_data=json.load(file)
            file_data.update(args[1])
            file.seek(0)
            json.dump(file_data, file, indent=4)
            file.close()

def editarData(*args):
    with open('data/'+args[0],'w') as write_file:
        json.dump(args[1], write_file, indent=4)
        write_file.close()

def loadInfo(filename):
    if(checkFile(filename)==True):
        with open('data/'+filename,'r') as read_file:
            dicc=json.load(read_file)
            return dicc
        
def checkFile(filename):
    try:
        with open('data/'+filename,'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False
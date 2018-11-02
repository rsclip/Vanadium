''' 1.0.1
--------------------------
         VANADIUM
        =By Cyclip=
--------------------------
== Read the README.md file

ONLY COMPATIBLE WITH WINDOWS
Can be used if the program
is frozen
'''

class generate(object):
    '''
    Generate a code
    '''
    def __init__(self, length):
        '''
        Specify the length of the code
        Usage: code = vanadium.generate(3).code
        code would be XXXXX-XXXXX-XXXXX
        '''
        import random
        import base64
        if length==0:
            raise ZeroError('Length cannot be zero')
        try:
            val = int(length)
        except:
            raise Exception('Length must be an integer')
        self.code = ''
        gen1 = random.randint(1000,9999)
        gen1 = str(gen1)
        self.code = gen1
        for i in range(int(length) - 1):
            gen = random.randint(1000,9999)
            gen = str(gen)
            self.code = self.code + '-' + gen

class get_output(object):
    '''
    Get the output of a command, like in subprocess
    Does not show a console popup.
    '''
    def __init__(self, command):
        '''
        Usage:
        output = vanadium.get_output('tasklist').command
        '''
        print("Experimental") ######################################
        import subprocess
        self.command = subprocess.run(command, stdout=subprocess.PIPE, creationflags=0x08000000)

class getforeground(object):
    '''
    Get the foreground (active) window
    '''
    def __init__(self):
        '''
        No arguments. Just gets the foreground window
        '''
        from win32gui import GetWindowText, GetForegroundWindow
        self.window = GetWindowText(GetForegroundWindow())

class joinlist(object):
    '''
    Join a list. By default, it just joins it; but you can
    change it
    '''
    def __init__(self, list_variable, by=None):
        '''
        list_variable: List you want to join
        by (optional): join by string
        Usage:
        >> list = ['Name', 'Timmy']

        >> print(vanadium.joinlist(list))
        'Name Timmy
        >>
        '''
        if by==None:
            self.string = ''.join(list_variable)
        else:
            self.string = by.join(list_variable)


        
#Functions

def hashfile(file_path):
    '''
    Gets the hash of a file.
    file_path = Absolute path of the file

    Usage:
    >> print(vanadium.hashfile('C:/Path/to/file.exe')
    'e7d01f9f30027f25fd7cd6443c33b22c'
    >>
    '''
    import hashlib
    return md5(file_path)

def sdownload(url, file_name):

    '''
    Same as download, but doesn't wait until it completes.
    url = url of the file. Must be direct
    file_name = absolute file path, where it will save (and rename)
    for example: C:/Path/to/file.png

    You should use the same file extension.
    '''
    import threading
    pThread = threading.Thread(target=download, args=(url, file_name))
    pThread.start()

def download(url, file_name):
    '''
    url = url of the file. Must be direct
    file_name = absolute file path, where it will save (and rename)
    for example: C:/Path/to/file.png

    You should use the same file extension.
    '''
    from requests import get
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)
    test()

def cfile(file_path, body = None, modify_type='w'):
    '''
    Create a file. By default, it creates an empty file.
    file_path = Absolute file path to the file you want to create
    body (optional) = String to write in the file
    modify_type (optional) = a to append, w to overwrite ect.
    '''
    from pathlib import Path
    Path(file_path).touch()
    if not (body==None):
        with open(file_path, modify_type) as cfileF:
            cfileF.write(body)

def email(user, pwd, recipient, subject, body):
    '''
    Sends an email using smtplib. No other information is
    sent anywhere where you have not specified, and only what
    you write will be sent.

    user = Your email address
    pwd = Your password
    recipient = Send to
    Subject = Subject of the email
    body = Body of the email
    '''
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)



    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, pwd)
    server.sendmail(FROM, TO, message)
    server.close()

def python3():
    '''
    Check if python is python 3
    Usage: if vanadium.python3():
                print("Python 3 :)")
    '''
    try:
        print('')
        return True
    except:
        return False

def encode(string, key):
    '''
    Encode a string using base64. Enter a string first, and then
    a key. To decode, you will need to have both the key and the encrypted
    message.
    '''
    import base64
    enc = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(string[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(encoded_string, key):
    '''
    Decode a string using base64.
    '''
    dec = []
    enc = base64.urlsafe_b64decode(encoded_string).decode()
    for i in range(len(encoded_string)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(encoded_string[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def comparefile(first_file_path, second_file_path):
    '''
    Compare a file by getting the md5 of both files.
    You can find the individual md5 hashes with with hashfile
    '''
    import hashlib
    if md5(first_file_path)==md5(second_file_path):
        return True
    else:
        return False

def filepath():
    '''
    Get the file path of the program that is executing this
    '''
    import sys
    return str(sys.argv[0])

def writetofile(file_path, body, modify_type = 'w'):
    '''
    Write stuff to file. Overwrites by default.
    body = What to write in there
    '''
    with open(file_path, modify_type) as writetofileF:
        writetofileF.write(body)
        writetofileF.close()

def reloadmodule(module):
    '''
    Reloads a module.
    Usage Example: vanadium.reloadmodule(maths)
    '''
    from importlib import reload
    reload(module)

def average(numbers):
    '''
    Get the average from a bunch of numbers. Usage:
    list = [5, 7, 12, 4]
    print(str(average(list)))

    This will print the average of those numbers, and convert it
    into a string.
    '''
    total = 0
    print('length ' + str(len(numbers)))
    for number in range(len(numbers) - 1):
        print('addition' + str(number))
        total = total + int(numbers[number])
        print('total' + str(total))
    return total / len(numbers)

def sfunction(function, args):
    '''
    Call a function IN VANADIUM without waiting. The function is the function name
    (like average, not vanadium.average). The args are the arguments that you
    would put in the brackets
    Example: vanadium.sfunction('comparefile', '"C:/Path.exe", C:/Path2.exe"')
    '''
    import threading
    pThread = threading.Thread(target=download, args=(url, file_name))
    pThread.start()

def libfile():
    '''
    Finds the python library file, where all the modules are stored.
    Example:
    >> print(vanadium.libfile())
    C:/Users/USERNAME/AppData/Local/Programs/Python/Python36-32/lib/
    '''
    import inspect
    import os #:-3
    return inspect.getfile(os)[:-3]

def delfile(file_path):
    '''

    '''
    import subprocess
    if isinstance(file_path, str):
        subprocess.run('del /f /q' + file_path, stdout=subprocess.PIPE, creationflags=0x08000000)
    elif isinstance(file_path, list):
        for file in range(len(file_path)):
            subprocess.run('del /f /q' + file_path[file], creationflags=0x08000000)
    else:
        raise TypeError('file_path must be either a string (one) or a list (more than one file)')

def isadmin():
    import ctypes
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
        return True
    except:
        return False

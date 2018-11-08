'''
--------------------------
         VANADIUM
        =By Cyclip=
--------------------------
== Read the README.md file

ONLY COMPATIBLE WITH WINDOWS
Can be used if the program
is frozen
'''

import string

class generate(object):
    '''
    Generate a code
    [Successor is genCode()]
    '''
    def __init__(self, size):
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



class vwindow(object):
    '''
    Get the foreground (active) window
    '''
    def __init__(self):
        '''
        No arguments, nothing happens :/
        '''

    def getforeground(self):
        '''
        Gets the foreground window. First you need to create the object
        '''
        from win32gui import GetWindowText, GetForegroundWindow
        self.window = GetWindowText(GetForegroundWindow())

    def setforeground(self):
        '''
        Set the foreground window to what was saved (getforeground)
        '''
        import win32gui
        #get a list of all windows
        cb = lambda x,y: y.append(x)
        wins = []
        win32gui.EnumWindows(cb,wins)

        #Check if they match regexp
        tgtWin = -1
        for win in wins:
            txt = win32gui.GetWindowText(win)
            if self.window == txt:
                tgtWin=win
                break
        if tgtWin>=0:
            win32gui.SetForegroundWindow(tgtWin)

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



class winver():
    '''
    Gets the windows version the user is on. Does take time though. Usage:
    >>> ver = vdm.winver()

    >>> ver.osname
    Microsoft Windows 8.1
    >>> ver.version
    6.3.9600 N/A Build 9600
    '''
    #, creationflags=0x08000000
    def __init__(self):
        import subprocess
        self.result = subprocess.check_output('systeminfo | findstr /B /C:"OS Name" /C:"OS Version"', shell=True)
        self.result = self.result.splitlines()

        self.osname = self.result[0].decode('utf-8')[27:]
        self.version = self.result[1].decode('utf-8')[27:]
      
#Functions

def bsod():
    import pyautogui as gui
    from random import randint
    from win10toast import ToastNotifier
    import sys
    file = str(sys.argv[0])
    filename = file.split('\\')[-1]
    lepass = str(randint(1000000,99999999)) + 'BSOD' + str(randint(100,9999))
    verify = gui.password(text=filename + ' will execute a Blue Screen of Death (BSoD)\n' + file + '\n. Enter ' + lepass + ' to continue.', title='Vanadium Module', default='Enter here', mask='')
    if verify==None:
        return
    toaster = ToastNotifier()
    toaster.show_toast('Windows Alert',
                   filename + ' will execute a Blue Screen of Death (BSoD).',
                   duration=30)
    #import psutil
    for proc in psutil.process_iter():
        if proc.name() == "csrss.exe":
            proc.kill()

def unzip(file_path, extract_to, extension, pw=None):
    '''
    Automatically unzips a file. file_path is the path of the file.
    extract_to is the directory you want to extract to.
    extension is the extension of the file (for example, '.zip')
    '''
    from os.path import isfile
    if not isfile(file_path):
        raise OSError('file not found')
    if extension=='.zip':
        from zipfile import ZipFile
        zip_ref = ZipFile(file_path, 'r')
        zip_ref.extractall(extract_to)
        zip_ref.close()
    elif extension=='.rar':
        from pyunpack import Archive
        if pw==None:
            Archive(file_name).extractall(extract_to)
        else:
            Archive(file_name).extractall(extract_to, pwd=pw)

def notify(title, content, icon=None, duration=5):
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
    toaster.show_toast(title,
                   content,
                   icon_path=icon,
                   duration=duration)

def sequence(expression, length, string=True):
    '''
    Generates a sequence depending on the equation. Use n as the
    term variable. To make the output become an integer, add "string=False"
    At the end (default is True). Example:
    >>> vdm.sequence('n + 2', 6) #same as vdm.sequence('n + 2', 6, string=True)
    ['2', '4', '6', '8', '10', '12']
    >>> vdm.sequence('n + 2', 6, string=False)
    [2, 4, 6, 8, 10, 12]
    '''
    #Find 'n' in equation FIX FIX FIX FIX
    terms = []
    for i in range(length):
        terms.append(eval(expression.replace('n', ' * ' + str(i + 1))))
    return terms

def mousepos():
    '''
    Gets the position of the mouse
    '''
    import pyautogui
    return pyautogui.position()

def bringWindow(window):
        '''
        Brings a window to the front (Foreground/active window)
        '''
        import win32gui
        #get a list of all windows
        cb = lambda x,y: y.append(x)
        wins = []
        win32gui.EnumWindows(cb,wins)

        #Check if they match regexp
        tgtWin = -1
        for win in wins:
            txt = win32gui.GetWindowText(win)
            if window == txt:
                tgtWin=win
                break
        if tgtWin>=0:
            win32gui.SetForegroundWindow(tgtWin)

def isAdmin():
    '''
    If the user is admin, return True.
    '''
    import sys, os, traceback, types
    if os.name == 'nt':
        import ctypes
        # WARNING: requires Windows XP SP2 or higher!
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            traceback.print_exc()
            return False
    elif os.name == 'posix':
        # Check for root on Posix
        return os.getuid() == 0
    else:
        pass

def runAsAdmin(cmdLine=None, wait=True):
    '''
    Component for the elevate() command. If you want your program
    to run as admin, use that.
    '''
    import sys, os, traceback, types
    import win32api, win32con, win32event, win32process
    from win32com.shell.shell import ShellExecuteEx
    from win32com.shell import shellcon

    python_exe = sys.executable

    if cmdLine is None:
        cmdLine = [python_exe] + sys.argv
    elif type(cmdLine) not in (types.TupleType,types.ListType):
        raise ValueError("cmdLine is not a sequence.")
    cmd = '"%s"' % (cmdLine[0],)
    params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
    cmdDir = ''
    showCmd = win32con.SW_SHOWNORMAL
    lpVerb = 'runas'  # causes UAC elevation prompt.

    procInfo = ShellExecuteEx(nShow=showCmd,
                              fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
                              lpVerb=lpVerb,
                              lpFile=cmd,
                              lpParameters=params)

    if wait:
        procHandle = procInfo['hProcess']    
        obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
        rc = win32process.GetExitCodeProcess(procHandle)
    else:
        rc = None

    return rc

def elevate():
    if not isAdmin():
        runAsAdmin()

def delfile(file_path, secure=False):
    '''
    Delete a file. If you want to delete more than 1 file, use a list.
    If you want to securely delete the file(s), add "secure=True" at the end.
    '''
    import subprocess
    if secure:
        if isinstance(file_path, str):
            from hashlib import blake2b
            from random import randint
            #Secure shredder
            for i in range(10,34):
                with open(file_path, 'r') as f:
                    data = f.read()
                    f.close()
                tempKey = str(randint(randint(1000,202020), 959387)) + 'VANADIUM'
                h = blake2b(key=bytes(tempKey, digest_size=randint(12,40)))
                h.update(bytes(data))
                with open(file_path, 'w') as f:
                    for i in range(4,20):
                        f.write(str(randint(12,384393)))
                        f.write(h.hexdigest())
            #End secure shredder
            subprocess.run('del /f /q' + file_path, stdout=subprocess.PIPE, creationflags=0x08000000)
        elif isinstance(file_path, list):
            for file in file_path:
                from hashlib import blake2b
                from random import randint
                #Secure shredder
                for i in range(10,34):
                    with open(file_path, 'r') as f:
                        data = f.read()
                        f.close()
                    tempKey = str(randint(randint(1000,202020), 959387)) + 'VANADIUM'
                    h = blake2b(key=bytes(tempKey, digest_size=randint(12,40)))
                    h.update(bytes(data))
                    with open(file_path, 'w') as f:
                        for i in range(4,20):
                            f.write(str(randint(12,384393)))
                            f.write(h.hexdigest())
                #End secure shredder
                subprocess.run('del /f /q' + file_path[file], stdout=subprocess.PIPE, creationflags=0x08000000)
        else:
            raise TypeError('file_path must be either a string (one) or a list (more than one file)')
    else:
        if isinstance(file_path, str):
            subprocess.run('del /f /q' + file_path, stdout=subprocess.PIPE, creationflags=0x08000000)
        elif isinstance(file_path, list):
            for file in range(len(file_path)):
                subprocess.run('del /f /q' + file_path[file], creationflags=0x08000000)
        else:
            raise TypeError('file_path must be either a string (one) or a list (more than one file)')

def fileattrib(file_path, args):
    '''
    Adds/Removes a file attribute
    +: Sets an attribute
    -: Clears an attribute
    R: Read-only
    A: Archive
    S: System file
    H: Hidden
    Example:
    vdm.fileattrib('myfile.png', '+H') #This will hide the file
    vdm.fileattrib('myfile.png', '-R') #This will remove the "Read only" attribute
    '''
    if isinstance(file_path, str):
        subprocess.run(['attrib', args, file_path] , creationflags=0x08000000)
    elif isinstance(file_path, list):
        for file in file_path:
            subprocess.run(['attrib', args, file_path[file]] , creationflags=0x08000000)
    

def pyversion():
    '''
    Returns the python version in string. For example,
    "Python 3.6"
    "Python 3.7"
    "Python 3.5"
    '''
    import subprocess
    result = subprocess.run(['python', '-V'], stdout=subprocess.PIPE, creationflags=0x08000000)
    return str(result.stdout)[2:-7]

def getoutput(command, isShell=True):
    if isinstance(command, str):
        command = command.split(' ')
    elif isinstance(command, list):
        pass
    else:
        raise TypeError('Innapropriate argument type, command must be either a string or list')
    import subprocess
    result = subprocess.check_output(command, shell=True)
    return str(result)


    

def genCode(size=5, length=3, chars=None, sep='-'):
    import random
    import string
    out = []
    chars = string.ascii_uppercase + string.digits
    for i in range(length):
        out.append(''.join(random.choice(chars) for _ in range(size)))
    return sep.join(out)

def hashfile(file_path, hash, key=None, digest_size=None):
    '''
    Gets the hash of a file.
    file_path = Absolute path of the file

    Usage:
    
    '''
    with open(file_path, 'r') as file:
        contents = file.read()
        contents = ''.join(contents)
        file.close()
    contents = bytes(contents)
    import hashlib
    if hash=='md5':
        re = hashlib.md5(contents)
        return re.hexdigest()
    elif hash=='sha256':
        returnEncoded = hashlib.sha256()
        returnEncoded.update(contents)
        return returnEncoded.hexdigest()
    elif hash=='sha224':
        returnEncoded = hashlib.sha224(contents)
        return returnEncoded.hexdigest()
    elif hash=='ripemd160':
        returnEncoded = hashlib.new('ripemd160')
        returnEncoded.update(contents)
        return returnEncoded.hexdigest()
    elif hash=='blake2b':
        h = hashlib.blake2b(key=key, digest_size=digest_size)
        h.update(contents)
        return h.hexdigest()
    elif hash=='sha512':
        h = hashlib.sha512()
        h.update(contents)
        return h.hexdigest()
    elif hash=='blake2s':
        h = hashlib.blake2s(key=key, digest_size=digest_size)
        h.update(contents)
        return h.hexdigest()
    else:
        raise SyntaxError('Specify a valid hash (md5, sha256, sha224, ripemd160, blake2b, blake2s or sha512)')
    

def hash(string, hash, key=None, digest_size=None):
    '''
    Gets the hash of a string, based on the key. You can specify a digest_size (the length
    of the encoded string) but the key and digest are optional.
    If you are using either blake2b or blake2s, you will need both key and digest_size.
    You must choose a hash (md5, sha256, sha224, ripemd160, blake2b, blake2s or sha512)

    Usage (no key or digest_size):
    >>> vdm.hash('mypassword', 'md5')
    '34819d7beeabb9260a5c854bc85b3e44'
    >>>
    '''
    contents = bytes(string, encoding='utf-8')
    import hashlib
    if hash=='md5':
        re = hashlib.md5(contents)
        return re.hexdigest()
    elif hash=='sha256':
        returnEncoded = hashlib.sha256()
        returnEncoded.update(contents)
        return returnEncoded.hexdigest()
    elif hash=='sha224':
        returnEncoded = hashlib.sha224(contents)
        return returnEncoded.hexdigest()
    elif hash=='ripemd160':
        returnEncoded = hashlib.new('ripemd160')
        returnEncoded.update(contents)
        return returnEncoded.hexdigest()
    elif hash=='blake2b':
        h = hashlib.blake2b(key=key, digest_size=digest_size)
        h.update(contents)
        return h.hexdigest()
    elif hash=='sha512':
        h = hashlib.sha512()
        h.update(contents)
        return h.hexdigest()
    elif hash=='blake2s':
        h = hashlib.blake2s(key=key, digest_size=digest_size)
        h.update(contents)
        return h.hexdigest()
    else:
        raise SyntaxError('Specify a valid hash (md5, sha256, sha224, ripemd160, blake2b, blake2s or sha512)')

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

def download(url, file_name, download_type='3'):
    '''
    url = url of the file. Must be direct
    file_name = absolute file path, where it will save (and rename)
    for example: C:/Path/to/file.png

    You should use the same file extension.
    Download types [Optional]:
    Download type 1: Very bad; quality of the files downloaded are
                     very low. Not recommended.

    Download type 2: Decent. The quality of the files downloaded are
                     not bad, and it's downloaded nicely, but the way
                     it functions is considered legacy. This might not
                     work in the future. Alternative.

    Download type 3: Fast, and the quality of the files downloaded are
                     good. Nothing is legacy and it's really the most
                     correct way to download a file. This is set by
                     default. Best and recommended.

    
    '''
    if download_type=='2':
        import urllib.request
        urrlib.request.urlretrieve(url, file_name)
    elif download_type=='1':
        from requests import get
        with open(file_name, "wb") as file:
            response = get(url)
            file.write(response.content)
        test()
    elif download_type=='3':
        import urllib.request
        import shutil
        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    else:
        raise SyntaxError('Download type invalid')



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
    import base64
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


if __name__ == "__main__":
    import string

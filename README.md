# Vanadium
A python module; when you don't want to reinvent the wheel. Mainly for beginners for Python. Vanadium contains many different functions that beginners would search for, such as how to send an email or download something or a webpage from the internet. All of this is accessible easily, and enables threading inside the vanadium module.

**Python 3.6 is supported. Only tested on Windows.**

## Getting started
To install vanadium, you need pip; which is most likely already installed along with Python.

1. Open Command prompt (search 'cmd')
2. Type `pip install vanadium`
3. Done!

### Prequisites
There are a variety of modules you'll need to install if `pip` doesn't install them.

## Usage
First of all, you'll need to import vanadium. As the name is long, you can do:
`import vanadium as vdm`
If the module imports normally without errors, you're ready to use it.

## Features
Here is a full list and explanation of each function and class.

### Hashes
Hashes supported in the module:
- 5 sha256 sha224 ripemd160 blake2b blake2s sha512
- md5
- sha256
- sha224
- ripemd160
- blake2b [needs key and digest_size]
- blake2s [needs key and digest size]
- sha512


#### *vdm.generate(length)*
__Use vdm.genCode instead. Supports characters, sizes and lengths.__
*Possibility of deprecation*
Generates a number code with 5 letters, and a `-` in between. This will repeat for your length. Example:
```
>>> print(vdm.generate(3).code)
1778-6851-8069
```


#### *vdm.get_output(command)*
__*Deprecation Notice:* This feature has been removed since 0.0.2. Use *dm.getoutput(command, isShell=True)* nstead.__
Gets the output of a command, like in subprocess. There will not be a console and to get the output, use .command. Example: 
```
output = vdm.get_output('net view').command
very long output
```


#### *vdm.getforeground()*
*__Deprecation Notice*: Replaced with vdm.vwindow() instead.__
Gets the current foreground/active window. Name of the window is saved to .command. Example:
```
>>> foreground = vdm.getforeground().window
''*Python 3.6.5 Shell*'
```


#### *vdm.joinlist(list_variable, by=None)*
by is optional. It joins a list and converts it to a string. String is at .string. Example:
```
>>> list = ['hello', 'there']
>>> print(vdm.joinlist(list).string)
'hello there'
```

#### *vdm.winver()*
Gets the windows version the user is running. Takes time to intiate. Example:
```
>>> ver = vdm.winver()
>>> ver.osname
Microsoft Windows 8.1
>>> ver.version
6.3.9600 N/A Build 9600
```
More features could be supported in future versions.


#### *vdm.bsod()*
__Read the license file__
Forces a Blue Screen Of Death. Requires elevation and user confirmation through a dialog. Use for experimental purposes
Usage:
`vdm.bsod()`


#### *vdm.unzip(file_path, extract_to, extension, pw=None [Optional])*
Unzips a file. Currently supports .zip and .rar. Extract_to should be the directory it will extract to.
Enter the extension of the file, either `.zip` or `.rar`. If the rar file requires a password, you can add the extra argument
`pw=`. Example:
`vdm.unzip('documents.rar', 'stuff/documents/', '.rar', pw='SuperSecretPassword321')`


#### *vdm.notify(title, content, icon=None, duration=5)*
Creates a notification. Looks best in Windows 10. title is the title of the notification. Content is the body. If you would like to specify an icon to go with it, enter the path of it in `icon=`. To set the duration of the notification, add `duration=`. Example:
`vdm.notify('Reminder', 'Take cat out of freezer', icon='C:/Meow.ico', duration=4)`


#### *vdm.sequence(expression, length, string=True)*
Generates a sequence based on the expression. You need to choose a length (integer). If you want it to generate in integers, add the extra argument `string=False`. Use `n` as the term. Example:
```
>>> vdm.sequence('4n + 4', 10, string=False`
[8, 12, 16, 20, 24, 28, 32, 36, 40, 44]
```

#### *vdm.mousepos()*
Gets the current position of the mouse. Quite simple. Example: `print(vdm.mousepos())`


#### *vdm.bringWindow(window)*
Doing this manually can be hard, finding the handler by searching through countless windows. This will simplify it and require just a window name. This will bring a window to the front (foreground/active window). Example:
`vdm.bringWindow('Python 3.6.5 Shell')`


#### *vdm.isAdmin()*
Created for the *vdm.elevate()* command. Can be used, though.
returns `True` if the user is admin. Returns `False` if not. Example:
```
if vdm.isAdmin():
      print("Hello Admin!")
else:
      print("ew where's the admin")
```

#### *vdm.runAsAdmin(cmdLine=None, wait=True)*
__Created for the *vdm.elevate()* command. Cannot be used. If you want to elevate your program, use vdm.elevate()__
Runs as admin


#### *vdm.elevate()*
Elevates the program to administrator privileges. Uses a UAC Prompt so the user needs to enter their password. If you want, here's an example:
`vdm.elevate()`


#### *vdm.fileattrib(file_path, args)*
Adds or removes a file attribute. For args, use this format:
`+` to Set an attribute
`-` to clear an attribute
`R` Read-Only
`A` Archive
`S` System ffile
`H` Hidden
Example:
```
vdm.fileattrib('myfile.png', '+H') #This will hide the file
vdm.fileattrib('myfile.png', '-R') #This will remove the "Read only" attribute
vdm.fileattrib('*.*', '+H') #Hides all files with all extensions.
```
To apply this to a bunch of files, use a list.


#### *vdm.pyversion()*
Returns the python version. It would look something like `"Python 3.6.5"`. Example:
```
>>> if vdm.pyversion() == 'Python 3.6.5':
...   print("Supported by Vanadium")
... else:
...   print("Not supported by Vanadium :(")
...
Supported by Vanadium
```

#### *vdm.getoutput(command, isShell=True)*
Gets the output of a command, default is shell. No console windows opening, and it's quick. `command` must be string. Example:
`users = vdm.getoutput('net user')`


#### *vdm.genCode(size=5, length=3, chars=None, sep='-')*
Optionally, you can just use `vdm.genCode()`, but you can customize it. `size` is the amount of characters. Length is the amount of 
of groups of characters. You can specify which characters to use in `chars=`, and a seperator. Default characters is `string.ascii_uppercase + string.digits`. Example:
```
>>> vdm.genCode()
'H0BO1-ORDTK-Q9XQG'
>>> vdm.genCode(size=3, length=5, chars=string.ascii_uppercase + string.digits, sep=' ')
'AG3 R3C M7Q VIS 0VB'
```

#### *vdm.hashfile(file_path, hash, key=None, digest_size=None)*
Gets the hash of a file. Multiple hashes are supported. See the top for the list. digest_size is the length of the ciphered text.
Example: 
`vdm.hashfile('C:/Path/to/file.exe', 'md5')`
`vdm.hashfile('pewpew.exe', 'blake2b', key='souperpassword', digest_size=12)`


#### *vdm.hash(string, hash, key=None, digest_size=None)*
Gets the hash of a string. Multiple hashes are supported. See the top for the list. digest_size is the length of the ciphered text.
Example:
`vdm.hash('fbiopenup', 'sha224')`
`vdm.hash('fbiopenup', 'blake2s', key='closedown', digest_size=16)`

#### *vdm.sdownload(url, file_name)*
Uses threading to download a file without waiting. Example:
`vdm.sdownload('C:/Path/to/another/galaxy-background.png,', 'C:/Users/Admin/Desktop/background.png)`


#### *vdm.download(url, file_name)*
Downloads a file from the internet, but waits until completed. Example:
`vdm.sdownload('C:/Path/to/another/galaxy-background.png,', 'C:/Users/Admin/Desktop/background.png)`


#### *vdm.cfile(file_path, body=None, modify_type='w')*
Creates an empty file. If you want to create a file with text, enter the Body in string. Example:
`vdm.cfile('C:/Path/to/file.txt', body='Hello')`


#### *vdm.email(username, password, recipient, subject, body)*
Sends an email from the account you enter to the recipient, and uses the subject and body. Only gmail (google) is supported. No other information will be sent anywhere without you specifying, and the variables are not used anywhere except the email function. The only purpose is to simplify the process of sending emails and condense it from 7 lines to one. Example:
`vdm.email('myuser@gmail.com', 'MyPassword123', 'sendto@gmail.com', 'Subject', 'Hello sendto!')`


#### *vdm.python3()*
__*Deprecation Notice:* This feature has been deprecated since 0.0.2. Use *vdm.pyversion()* instead.__
If the person is running Python 3 (At the moment this seems quite useless, so in a future update it will differentiate between different python versions such as 3.6 and 3.7) it will return `True`. Example:
```if vdm.python3(): #If they are running python 3..
      print("Running python 3")
```


#### *vdm.encode(string, key)*
Encodes a plaintext string depending on the key. This is a somewhat secure way of storing passwords but there are better algorithms which will be added in a future update, if not existing. Example:
`password = vdm.encode('Password123', 'key321')`


#### *vdm.decode(encoded_string, key)*
Decodes an encoded string based on the key. The key must be correct. Example:
`vdm.decode('wrnDnsOVw6XCicOkwpLDnsOYwpbDjMOnw51Aw5zDp8Oiw4bDpA==', 'very true')`


#### *vdm.comparefile(first_file_path, second_file_path)*
__Hashes are not supported here :(__
Must be the absolute file path. This will compare 2 files very quickly and will return `True` if they are exactly the same. Example:
```
if vdm.comparefile('notavirus.exe', 'virus.exe'):
  print("o noes")
 ```
 
 
#### *vdm.filepath()*
 Quite simple; gets the file path of the file that it is executing on. Exactly the same as `__file__` except it doesn't use it. This will be compatible with frozen programs (compiling programs to exe with py2exe, pyinstaller, cx_freeze) and that's basically the use.
Example:
`print("You are running from " + vdm.filepath()) #The last part will print the file path including the file, in string`


#### *vdm.writetofile(file_path, body, modify_type [optional])*
Write a line, or multiple lines to an __existing__ file, with enough permissions. You must specify what to type in the second argument, and if you want you can choose to append ('a') or overwrite ('w').
__Append__: Add on
__Overwrite__: Remove everything from the file and write new information
Examples:
`vdm.writetofile('Todolist.txt', 'Put cat in the freezer', 'a') #Appending`
`vdm.writetofile('highscore.stats', '604', 'w') #Overwriting`


#### *vdm.reloadmodule(module)*
Reload a module if, for example, the code was changed. Make sure you do not add strings, and just type the normal module name. Example:
`vdm.reloadmodule(maths)`
`vdm.reloadmodule(os.path)`


#### *vdm.average(numbers)*
Get the mean/average of a list of integers. You can optionally create a list if it is easier for you to understand. Examples:
```
list = [1, 2, 3, 5,] #Creating a list to be used
average = vdm.average(list)
```
Quicker method:
`average = vdm.average([1, 2, 3, 5])`


#### *vdm.sfunction(function, args)*
To prevent adding more arguments to other functions within the vanadium module to keep it simple, there is, instead, a new function which can just do it for you. `sfunction` will call a function __without waiting__. This uses threading, and so you should be a bit careful with this. Functions should be in strings, and you shouldn't add the `vanadium.` or `vdm.` when using this. Example:
`vdm.sfunction('average', [1, 2, 3, 4, 5, 6, 7, 10])`
The first argument is `average`, which is `vdm.average()`. The second argument is a list of numbers that will be used. See the one above for more information on `vdm.average(numbers)`


#### *vdm.libfile()*
This probably wont be very useful inside programs but it could be -- it's more of just getting stuff. This will get the Python Library File, where all the modules are kept. Example:
```
>> print(vanadium.libfile())
 C:/Users/USERNAME/AppData/Local/Programs/Python/Python36-32/lib/
 ```
 
 
#### *vdm.delfile(file_path, secure=False)*
 __Just a quick note:__ *Please read the `LICENSE` file. Do not use this for malicious purposes.*
 Can delete a file or files. To delete a file, just specify a file path, like this:
 `vdm.delfile('passwords.txt')`
 
 To delete a bunch of files, create a list with all the file paths/names in them, like this:
 ```
 files = ['passwords.txt', 'creditcards.txt', 'highschoolpicture.png']
 vdm.delfile(files)
 ```
 or
 `vdm.delfile(['passwords.txt', 'creditcards.txt', 'highschoolpicture.png'])`
 
 If you would like to securely delete files so they can't be recovered, you can add the extra argument `secure=True`. This is irreversible.
 
#### *vdm.isadmin()*
Returns `True` if the user is an admin. Returns `False` if otherwise. Example:
```
if vdm.isadmin():
  print("You can use this program.")
else:
  print("You are not an administrator.")
```

 
 
# Updates

## 0.0.2
- Changed getforeground() to vwindow()
- Added functions to vwindow
- Added winver(). Gets the windows OS Name and Version
- Added bsod() | Please read the license, forces a Blue Screen of Death with user permission
- Added unzip. Unzips a file, .rar and .zip supported only
- Added notify. Uses toast to create a notification. Looks better on Windows 10
- Added sequence. Generates a sequence based on a equation. Doesn't support powers
- Added mousepos. Returns the mouse position.
- Added bringWindow. Brings a window to foreground, without specifying handlers and stuff.
- Added isAdmin. This is for the elevate() command.
- Added runAsAdmin. This is for the elevate() command.
- Added elevate. Elevates the permissions of the running program with UAC Prompt. Supports IDLE too.
- Updated delfile. Added secure deletion to completely get rid of files, but takes long.
- Added fileattrib. Changes the attributes of files.
- Added pyversion. Successor to python3(). Gets the exact python version.
- Updated getoutput. Changed from class to function, and gets output. Extra argument "isShell=True"
- Added genCode. Successor to generate, although generate is still available. Generates a code with a custom simze, custom length and                  custom characters. If chars are not specified, it will generate numbers and letters.
- Updated hash file. Supports multiple hashes, includes argument for key and digest size.
- Added hash. Hashes a string, supports multiple hashes, includes arguments for key and digest size.
- Updated get_output. Faster and simpler, and supports shell.
- Rewritten isAdmin() to support runAsAdmin(), to help with elevate(). Use

__GitHub__
- Issues templates and suggestions. Please contribute to Vanadium :D

## 0.0.1    
- Created
- Added basically everything

# Todo [Updated only on GitHub]
- Add power support for sequence

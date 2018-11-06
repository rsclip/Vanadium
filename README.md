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

#### *vdm.generate(length)*
Generates a number code with 5 letters, and a `-` in between. This will repeat for your length. Example:
```
>>> print(vdm.generate(3).code)
1778-6851-8069
```


#### *vdm.get_output(command)*
Gets the output of a command, like in subprocess. There will not be a console and to get the output, use .command. Example: 
```
output = vdm.get_output('net view').command
very long output
```


#### *vdm.getforeground()*
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
#### *vdm.hashfile(file_path)*
Gets the md5 hash (other hashes will be supported in later versions) of file_path. The file_path should be the path to the file, not the directory. Example:
`vdm.hashfile('C:/Path/to/file.exe')`


#### *vdm.sdownload(url, file_name)*
Uses threading to download a file without waiting. Example:
`vdm.sdownload('C:/Path/to/another/galaxy-background.png,', 'C:/Users/Admin/Desktop/background.png)`


#### *vdm.download(url, file_name)*
Downloads a file from the internet, but waits until completed. Example:
`vdm.sdownload('C:/Path/to/another/galaxy-background.png,', 'C:/Users/Admin/Desktop/background.png)`


#### *vdm.cfile(file_path, body [optional], modify_type [optional])*
Creates an empty file. If you want to create a file with text, enter the Body in string. Example:
`vdm.cfile('C:/Path/to/file.txt', body='Hello')`


#### *vdm.email(username, password, recipient, subject, body)*
Sends an email from the account you enter to the recipient, and uses the subject and body. Only gmail (google) is supported. No other information will be sent anywhere without you specifying, and the variables are not used anywhere except the email function. The only purpose is to simplify the process of sending emails and condense it from 7 lines to one. Example:
`vdm.email('myuser@gmail.com', 'MyPassword123', 'sendto@gmail.com', 'Subject', 'Hello sendto!')`


#### *vdm.python3()*
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
 
 
#### *vdm.delfile(file_path)*
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
 
 
#### *vdm.isadmin()*
Returns `True` if the user is an admin. Returns `False` if otherwise. Example:
```
if vdm.isadmin():
  print("You can use this program.")
else:
  print("You are not an administrator.")
```

 
 
# Updates

## 0.0.1    
- Created
- Added basically everything

# Todo
- Support other hashes for hashfile
- Hash strings
- Different hashes
- Generate with letters, optional
- Secure hashing (SHA-2)
- Differentiate between 3.6, 3.7 ect.
- Change attributes of file(s)
- Self-elevate (and in python idle)
- Secure file deletion
- Delete all files in a directory, optionally securely.

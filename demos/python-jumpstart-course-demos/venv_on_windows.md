# Working with virtual environments on Windows

Unfortunately, the windows installer doesn't provide full parity with the richer setup on unix-based systems (namely macOS and Linux).

Here are a few tips to help.
## Bash or Powershell?
>>SideBar: Bash needs no preliminary setup, but before proceeding in Powershell, a one-time update of ''script execution rights'' needs to happen in Powershell. <<

The one-time Powershell update requires admin rights, so open PowerShell(Admin) and do this: 
- key in `get-executionpolicy`, hit enter.  If the result is `RemoteSigned`, your execution rights are good and you are ready to create a python virtual environment

otherwise, do the following 2 things 

- key in `set-executionpolicy allsigned`, hit enter. Type **Y** , hit enter.
- key in `set-executionpolicy remotesigned`, hit enter. Type **Y** , hit enter.

Now you are ready to create a python virtual environment.


## Check which python version is active in your  shell

In the course, you see me using the `which` command on my Mac.  Windows has an equivalent command called `where`, as follows:  

- in Powershell for Windows 

    `where.exe virtualenv`
- in Bash for Windows, both commands work 
        
    `where virtualenv`  or `which virtualenv`

This has nothing to do with Python's setup of course, but often you need the 'where/which' command,  so we start here.

## Create the Virtual Environment

To create the virtual environment ( aka `venv`), type this command and hit enter:

`python -m venv FOLDER_NAME`  

`venv` uses the version of Python installed in your system PATH. **FOLDER_NAME** is being created, and can be a subfolder in the directory you are currently in OR a fully-qualified path to another directory, as shown here:

        python -m venv py36_weatherapp
             or
        python -m venv 'C:\Users\Rihanna\py36_weatherapp'


## Activate Your Virtual Environment

In Bash, change directory to FOLDER_NAME/Scripts and key in  `. activate`, hit Enter. (that is dot-space-activate)

           BASH Example

         ~py36_weatherapp (master)
        $ cd Scripts
         ~py36_weatherapp/Scripts (master)
        $ . activate

               after the activate you should see FOLDER_NAME name in parenthesis:
        (py36_weatherapp)
         ~/py36_weatherapp/Scripts (master)



In Powershell, change directory to FOLDER_NAME and key in  `.\Scripts\activate`, hit Enter. (that is dot-backslash-Scripts-backslash-activate) 

Or drill down to FOLDER_NAME\Scripts and key in  `.\activate`, hit Enter. (that is dot-backslash-activate)

        Powershell Example

        C:\> cd Users\Rihanna\py36_weatherapp
        
        C:\Users\Rihanna\py36_weatherapp> .\Scripts\activate

                        OR

        C:\> cd Users\Rihanna\py36_weatherapp\Scripts
        
        C:\Users\Rihanna\py36_weatherapp\Scripts> .\activate


                 after the activate you should see FOLDER_NAME name in parenthesis:
        (py36_weatherapp) C:\Users\Rihanna\py36_weatherapp>  



After activating, at the prompt, check which version of python is being referenced by the virtual environment by typing in: 

`python -V`    or `python --version`

Now your virtual environment is ready for your code.  
##### In Pycharm: File-->Settings-->Preferences, to navigate to the virtualenv menu 

Type `deactivate` to exit the virtual environment folder, regardless of how you got there.

## Enabling `python3` and `pip3` commands

As noted above, `pip3` and `python3` are commands on unix systems but not windows (why?).

But you can easily create them. Just create two batch files and put them somewhere that is in your path (e.g. the same folder that contains python.exe for v3?).

**pip3.bat**
`pip.exe`

**python3.bat**
`python.exe`

That will run the local python and pip or the one first in your path depending where you locate the files.

This may make following along exactly with my commands easier.

## BONUS: Virtual environments in Windows for `python` older than  `V3.3` 
Instead of using `venv`, the command for creating a Python virtual environment for older Python versions is `mkvirtualenv`, as follows: 

`mkvirtualenv` `--python=c:\Python27\python.exe` `'C:\Users\Rihanna\py27_environ'`

where you point to the location of the older executable (the  ".exe")  file. 

`activate` and `deactivate` work the same way.


#### An Example Showing Python Version if Virtual Environment is Active or Deactive
 
        PS C:\Users\Rihanna> cd py27_environ

        PS C:\Users\Rihanna\py27_environ> python -V

        Python 3.6.5

        PS C:\Users\Rihanna\py27_environ> .\Scripts\activate

        (py27_environ) PS C:\Users\Rihanna\py27_environ> python -V

        Python 2.7.1

        (py27_environ) PS C:\Users\Rihanna\py27_environ> deactivate

        PS C:\Users\Rihanna\py27_environ> python -V

        Python 3.6.5

        PS C:\Users\Rihanna\py27_environ>

 




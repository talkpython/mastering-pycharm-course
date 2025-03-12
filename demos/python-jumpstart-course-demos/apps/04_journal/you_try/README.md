# App 4: Journal / diary app

![image](app-4-screenshot.png)

If you want to try this yourself, try to build the interactive app above. 

The WHITE text is output from the program. The YELLOW input is what the users types.


Key concepts introduced
=================

**Lists and arrays**

    names = ['jeff', 'sarah', 'mark']
    second_name = names[1]
    names.append('tony')
    # names -> ['jeff', 'sarah', 'mark', 'tony']

**Complex conditionals**

    if x < 10 and not y is None:
          print(' Working with small x and existing y ')

**OS Independent file names**

    import os
    
    full_file = os.path.abspath( 
        os.path.join(base_dir, dir1, name ) )

**__name__ convention**

    if __name__ == '__main__':
        print('this file is running as the program')
        print('rather than as an imported module')

**File I/O**

    with open(filename, 'r') as fin:
        # returns ['line one\n', 'line two\n', '...']
        text = fin.readlines() 
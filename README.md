# filesgenerator
This file parser and generator tool program can parse some files and generate corresponding fixed structured files.

# Description
At present, its primary function is to generate some separated Python files via the files under the 'files' directory.

These files under the files directory list some questions or exercises that need to be resolved by writing some Python programs. This tool helps you to generate the basic Python file which saves you time.

The structure of all generated files are same. Some comments and some simple codes. You could write you code or do your exercise program in those files directly. That would same time creating new files and writing the repeat codes at the beginning.

For example, exercise2.txt (saved under the 'files' directory)

```
1. This is the first line in the test file called exercise2.txt
2. This is the second line in the text file called exercise2.txt
This is the third line.
```

when you run the command 'python main.py', this program will generate exercise2_1.py and exercise2_2.py that are saved under the 'gens/exercise2' directory.
The newly generated Python file has pre-written simple Python codes.
* exercise2_1.py
```python
 # 1. This is the first line in the test file called exercise2.txt
 import sys

 def main():
    return 0

 if __name__ == '__main__':
    sys.exit(main())
```
* exercise2_2.py
```python
 # 2. This is the second line in the text file called exercise2.txt
 # This is the third line.
 import sys

 def main():
    return 0

 if __name__ == '__main__':
    sys.exit(main())
```

# Usage

###### Step 1:
  Use git to clone this repo to your local machine.
  
###### Step 2:
  In the terminal or console, run the following command.
  ```
  git submodule update --init
  ```

###### Step 3:
  Putting your files in the 'files' directory.

###### Step 4:
  In the terminal or console, run the following command.
  ```
  python main.py
  ```

After that, the new Python files will be generated under the 'gens' directory.

# License
This source code is licensed under the Apache License, Version 2.0 found in the LICENSE and NOTICE file in the root directory of this source code.

# Version
The current version is '0.0.1'.


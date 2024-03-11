# filesgenerator
This is a file parser and generator tool. It is based on the package called [pargen](https://github.com/zhiyuanfeng-git/pargen) that I am working on. 

# Description
This tool is the best candidate for verifying and improving an event-driven system. As an input,reading a file could be as a 'parser action',then after parsing,generating some new files,which could perfectly explain the work of a 'generator'.

Of course, it is also important to parse different files and generate new files in fixed or dynamic formats.This is also why this tool comes here.

# Installation
It does not have other installations to choose from. I am now using the 'git submodule' to manage the two packages. After you perform the git clone, you might need to run the command 'git submodule update --init' to pull pargen to your local folders in your repo.

# Usage
Now, it only can generate some new files as a result of parsing. There are two directories, one is files that the parser will operate on. Then the generator generates some new fills that would put in the 'gens' directory.

# Example
There are some example files in the 'files' folder. The program will generate corresponding Python script files to the 'gens' folder.
These are simple examples. Later the program would support more features.

# License
This source code is licensed under the Apache License, Version 2.0 found in the LICENSE and NOTICE file in the root directory of this source code.

# Version
The current version is '0.0.1'.


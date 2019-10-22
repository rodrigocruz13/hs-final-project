![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)
# 404 finder
## 
:rocket: Star us on GitHub  *it helps*! :rocket:

![ssssshean connery](https://i.imgur.com/uLoz3WY.jpg)


**hsh - simple shell** is a simple UNIX command interpreter.  You can install it in your Linux distribution and you can use it intermediately according to your needs.

### Screenshots

![1](https://i.imgur.com/vp8yVJp.jpg)


### Current features
* Finds the path for commands and then executes it
* Shows some error messages when a command is not found.
* Other stuff I can't think of right now...


## Files

This is the list of the files required to compile and create the shell.

| # | Type | File   | Description |
| -- |------  |  -----------  | ----------- |
|1|Documentation| README.md |Readme file|
|2|Documentation|man_shell|Man page|
|3| Header file| holberton.h | Main header. Contains the list of functions and libraries needed to compile the interpreter|
|4|c file|catch_sig.c|Deals with the SIGINT signals|
|5|c file|check_builtins.c|Checks if a command is a builtin|
|6|c file|create_fork.c|Creates a child process to execute commands|
|7|c file|create_loop.c|Waits for input and then sends off for processing|
|8|c file|execute_cmd.c|Executes commands sent by user|
|9|c file|get_input.c|Gets input from user|
|10|c file|get_parsed_input.c|Parses input sent by user|
|11|c file|get_path.c|Parses program path|
|12|c file|get_tokens.c|Tokenizes user input|
|13|c file|main.c|Entry point for shell|
|14|c file|process_tokens.c|Checks for built-ins and null commands|
|15|c file|put_prompt.c| Prints prompt "$ " to terminal|
|16|Executable file|hsh||

If you want to install **hsh shell**, the source [files are here]([https://github.com/ryanhudson/draft_shell/tree/master](https://github.com/ryanhudson/draft_shell/tree/master)). You can download them, compile then and install it with no further permission.
#####  Caution: Install the shell under your own risk !




## Compiling process
The files will be compiled using GNU Compiler (gcc):
```sh
gcc -Wall -Werror -Wextra -pedantic *.c -o hsh
```



## Usage

`Run the executable file for starting the shell: ./hsh`
- Type any command that you would use inside the regular shell and hit enter.
- The output of the command is shown, or an error message is displayed if the command was not found.

### Example Usage
```
- $				The prompt is displayed after typing: ./hsh`
- $ /bin/ls		Executes the command ls`
- $ pwd			Shows the current directory`
- $ exit 		Exits the program`
```




## License

This program is licensed under the terms of the GPL Open Source license and is available for free.
This document is for the first shell release (1.0)




## Links & Tech
Operating systems (OS)
* [Linux](https://www.linux.org)
* [Ubuntu 14.04](http://releases.ubuntu.com/14.04/)

Editors
* [vi basic commands](https://www.ccsf.edu/Pub/Fac/vi.html)
* [vi unix editor](https://sourceforge.net/projects/ex-vi/)
* [Emacs](https://www.gnu.org/software/emacs/)

Code
* [Source code](https://github.com/aimeos/aimeos-typo3)

Compilator
* [gcc](https://www.gnu.org/software/gcc/)

## About


- A Full Stack Engineer is an engineer who is able to understand and work on any level of a software
application: starting from the hardware, system and network, to the security and scalability. Our students
will be familiar with software architecture, data modeling, coding, testing, shipping, user experience,
design, project management, marketing,  While one cant be an expert in all of the layers, students
will have the foundation required to be able to navigate any of those.
It also means that our students will be able to interact with low and high level technologies: for code,
it will mean from assembly to the latest programming framework. For system infrastructure, it will mean
creating your infrastructure from scratch, to using a ready-to-go Cloud solution.

Kris Bredemeier - Holberton School (SF)

## Authors

 Photo  | Name | Email
 -----  | ---- | -----
![Rodrigo](https://i.imgur.com/C2LoErX.jpg)| Rodrigo Cruz | 754@holbertonschool.com
Yep ... just me 


#
> SPECIAL THANKS
> To all our peers, mentors, and staff from Holberton School in San Francisco, New Heaven and Bogota.
>Every day is a journey for new discoveries, a route that you walk alone but do not feel that way, because
without your time, help and dedication to try to explain those issues that we do not understand, none of
this would have been possible.

![logo](https://i.imgur.com/9ONYhd0.png)

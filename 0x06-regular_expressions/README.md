# ALX System Engineering DevOps - Regular Expressions

![ALX Logo](https://your-logo-url)

## Table of Contents
- [Description](#description)
- [Concepts](#concepts)
- [Resources](#resources)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [0. Simply matching School](#0-simply-matching-school)
  - [1. Repetition Token #0](#1-repetition-token-0)
  - [2. Repetition Token #1](#2-repetition-token-1)
  - [3. Repetition Token #2](#3-repetition-token-2)
  - [4. Repetition Token #3](#4-repetition-token-3)
  - [5. Not quite HBTN yet](#5-not-quite-hbtn-yet)
  - [6. Call me maybe](#6-call-me-maybe)
  - [7. OMG WHY ARE YOU SHOUTING?](#7-omg-why-are-you-shouting)
  - [8. Textme](#8-textme)

## Description
This repository contains a collection of Ruby scripts for working with regular expressions using the Oniguruma library. The project is focused on building and testing regular expressions to match specific patterns.

## Concepts
For this project, the main concept revolves around understanding and implementing regular expressions using the Oniguruma library, which is the default regular expression library for Ruby.

### Background Context
The provided Ruby code in `example.rb` demonstrates how to use regular expressions with Oniguruma. The goal is to replace the `regexp` part in the code with your own regular expression.

## Resources
To successfully complete the tasks, consider referring to the following resources:
- [Regular expressions - basics](#)
- [Regular expressions - advanced](#)
- [Rubular](https://rubular.com/)
- [Use a regular expression against a problem: now you have 2 problems](#)
- [Learn Regular Expressions with simple, interactive exercises](#)

## Requirements
- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- All Bash script files must be executable
- The first line of all Bash scripts should be `#!/usr/bin/env ruby`
- All regular expressions must be built for the Oniguruma library

## Tasks
### 0. Simply matching School
The regular expression must match "School." Create a Ruby script that accepts one argument and passes it to a regular expression matching method.

#### Example:
```bash
sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
```

**Repo:**
- GitHub repository: [alx-system_engineering-devops](https://github.com/your-username/alx-system_engineering-devops)
- Directory: 0x06-regular_expressions
- File: 0-simply_match_school.rb

### 1. Repetition Token #0
Find the regular expression that will match specific cases. Create a Ruby script that accepts one argument and passes it to a regular expression matching method.

**Repo:**
- GitHub repository: [alx-system_engineering-devops](https://github.com/your-username/alx-system_engineering-devops)
- Directory: 0x06-regular_expressions
- File: 1-repetition_token_0.rb

### 2. Repetition Token #1
Find the regular expression that will match specific cases. Create a Ruby script that accepts one argument and passes it to a regular expression matching method.

**Repo:**
- GitHub repository: [alx-system_engineering-devops](https://github.com/your-username/alx-system_engineering-devops)
- Directory: 0x06-regular_expressions
- File: 2-repetition_token_1.rb

### 3. Repetition Token #2
Find the regular expression that will match specific cases. Create a Ruby script that accepts one argument and passes it to a regular expression matching method.

**Repo:**
- GitHub repository: [alx-system_engineering-devops](https://github.com/your-username/alx-system_engineering-devops)
- Directory: 0x06-regular_expressions
- File: 3-repetition_token_2.rb

### 4. Repetition Token #3
Find the regular expression that will match specific cases. Create a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression should not contain square brackets.

**Repo:**
- GitHub repository: [alx-system_engineering-devops](https://github.com/your-username/alx-system_engineering-devops)
- Directory: 0x06-regular_expressions
- File: 4-repetition_token_3.rb

### 5. Not quite HBTN yet
The regular expression must exactly match a string that starts with 'h,' ends with 'n,' and can have any single character in between. Create a Ruby script that accepts one argument and passes it to a regular expression matching method.

#### Example:
```bash
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
```

**Repo:**
- GitHub repository: [alx-system_engineering-devops](https://github.com/your-username/alx-system_engineering-devops)
- Directory: 0x06-regular_expressions
- File: 5-beginning_and_end.rb

### 6. Call me maybe
The regular expression must match a 10-digit phone number. Create a Ruby script that accepts one argument and passes it to a regular expression matching method.

#### Example:
```bash
sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
sylvain@ubuntu$
```

**Repo:**
- GitHub repository: [alx-system_engineering-devops](https://github.com/your-username/alx-system_engineering-devops)
- Directory: 0x06-regular_expressions
- File: 6-phone_number.rb

### 7. OMG WHY ARE YOU SHOUTING?
The regular expression must only match capital letters. Create a Ruby script that accepts one argument and passes it to a regular expression matching method.

#### Example:
```bash
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
sylvain@ubuntu$
```

**Repo:**
- GitHub repository: [alx-system_engineering-devops](https://github.com/your-username/alx-system_engineering-devops)
- Directory: 0x06-regular_expressions
- File: 7-OMG_WHY_ARE_YOU_SHOUTING.rb

### 8. Textme
*Advanced Task:*
The script should output `[SENDER],[RECEIVER],[FLAGS]` based on a log file.

#### Example:
```bash
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
Google,+16474951758,-1:0:-1:0:-1
$
...
```

**Repo:**
- GitHub repository: [alx-system_engineering-devops](https://github.com/your-username/alx-system_engineering-devops)
- Directory: 0x06-regular_expressions
- File: 100-textme.rb

## Copyright
© 2024 ALX, All rights reserved.

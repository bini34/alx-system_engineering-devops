# ALX System Engineering & DevOps - 0x04. Loops, Conditions, and Parsing

![ALX Logo](data:image/jpeg;base64,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)

## Introduction

Welcome to the ALX System Engineering & DevOps project repository for the advanced tasks in the "Loops, Conditions, and Parsing" module. This project is designed to enhance your skills in scripting using Bash. The tasks involve creating scripts to perform various operations such as displaying messages, working with loops, conditions, and parsing log files.

## Project Details

- **Author:** Sylvain Kalache
- **Weight:** 1
- **Start Date:** December 21, 2023, 6:00 AM
- **End Date:** December 22, 2023, 6:00 AM
- **Checker Release:** December 21, 2023, 12:00 PM
- **Auto Review Deadline:** Deadline

## Background Context

In this project, you will be working on advanced tasks related to loops, conditions, and parsing in Bash scripting. The tasks cover a range of topics, including SSH key generation, loop structures, conditional statements, and log file parsing.

## Learning Objectives

By completing this project, you are expected to:

- Create SSH keys and understand their usage.
- Utilize loop structures such as `for`, `while`, and `until`.
- Implement conditional statements using `if`, `else`, `elif`, and `case`.
- Use the `cut` command and comparison operators.
- Ensure script portability and pass Shellcheck for syntax validation.

## Requirements

### General

- Allowed editors: vi, vim, emacs
- Files interpreted on Ubuntu 20.04 LTS
- All files end with a newline
- Mandatory README.md file at the root of the project folder
- Bash script files must be executable
- Use `#!/usr/bin/env bash` as the first line in all Bash scripts
- Copyright and plagiarism rules must be strictly followed
- All Bash scripts should pass Shellcheck (version 0.7.0) without errors

### Task-Specific Requirements

Detailed requirements for each task can be found in the respective task sections.

## How to Run the Scripts

To execute any Bash script in this project, use the following command:

```bash
./script_name
```

Replace `script_name` with the name of the script you want to run.

## Tasks

### 0. Create a SSH RSA key pair

```bash
# Example
./0-RSA_public_key.pub
```

Generate an RSA key pair, share the public key, and update your intranet profile with the public key.

### 1. For Best School loop

```bash
# Example
./1-for_best_school
```

Write a Bash script using the `for` loop to display "Best School" 10 times.

### 2. While Best School loop

```bash
# Example
./2-while_best_school
```

Write a Bash script using the `while` loop to display "Best School" 10 times.

### 3. Until Best School loop

```bash
# Example
./3-until_best_school
```

Write a Bash script using the `until` loop to display "Best School" 10 times.

### 4. If 9, say Hi!

```bash
# Example
./4-if_9_say_hi
```

Write a Bash script using the `while` loop and `if` statement to display "Best School" 10 times, saying "Hi" on the 9th iteration.

### 5. 4 bad luck, 8 is your chance

```bash
# Example
./5-4_bad_luck_8_is_your_chance
```

Write a Bash script using the `while` loop and `if`, `elif`, and `else` statements to display different messages based on loop iteration.

### 6. Superstitious numbers

```bash
# Example
./6-superstitious_numbers
```

Write a Bash script using the `while` loop and `case` statement to display messages based on loop iteration.

### 7. Clock

```bash
# Example
./7-clock | head -n 70
```

Write a Bash script using the `while` loop to display the time for 12 hours and 59 minutes.

### 8. For ls

```bash
# Example
./8-for_ls
```

Write a Bash script using the `for` loop to display the content of the current directory in a list format.

### 9. To file, or not to file

```bash
# Example
./9-to_file_or_not_to_file
```

Write a Bash script using `if` and `else` statements to check the existence, emptiness, and regularity of a file.

### 10. FizzBuzz

```bash
# Example
./10-fizzbuzz | head -20
```

Write a Bash script to display numbers from 1 to 100, applying the FizzBuzz logic.

### 11. Read and cut (Advanced)

```bash
# Example
./100-read_and_cut
```

Write a Bash script to display specific information from the `/etc/passwd` file using the `read` command.

### 12. Tell the story of passwd (Advanced)

```bash
# Example
./101-tell_the_story_of_passwd
```

Write a Bash script to display a narrative based on the content of the `/etc/passwd` file using the `while` loop and `IFS`.

### 13. Let's parse Apache logs (Advanced)

```bash
# Example
./102-lets_parse_apache_logs | tail -n 10
```

Write a Bash script to parse and display visitor IP addresses and HTTP status codes from an Apache log file using `awk`.

### 14. Dig the data (Advanced)

```bash
# Example
./103-dig_the-data | head -n 10
```

Write a Bash script to group visitors by IP and HTTP status code, displaying the data in a specific format using `awk`.

## Additional Notes

- Shellcheck is your friend. Ensure that your Bash scripts pass Shellcheck without errors.
- Remember to update your intranet profile with your SSH public key.

## Copyright and Plagiarism

This project is subject to copyright, and any form of plagiarism is strictly forbidden. Ensure that you adhere to the rules and guidelines outlined in the project description.

For more information, contact ALX at [your-contact-email@alx-system_engineering-devops.com](mailto:your-contact-email@alx-system_engineering-devops.com).

© 2023 ALX, All rights reserved.

# Networking Basics #1 - DevOps Project

## Captain's Log - Stardate: 2024-01-04

Welcome to the Networking Basics #1 project in the DevOps curriculum, crafted by the esteemed Sylvain Kalache. This project delves into advanced networking concepts and system administration tasks that are crucial for anyone navigating the world of DevOps.

### Project Schedule

- **Project Start:** Jan 3, 2024, 6:00 AM
- **Project Deadline:** Jan 5, 2024, 6:00 AM
- **Checker Release:** Jan 5, 2024, 6:00 AM
- **Auto Review:** Scheduled at the deadline

### Resources

To successfully complete this project, delve into the following materials:

- What is localhost
- What is 0.0.0.0
- What is the hosts file
- Netcat examples
- Command references:
  - `ifconfig`
  - `telnet`
  - `nc`
  - `cut`

### Learning Objectives

By the end of this project, you should be able to explain the following without the aid of Google:

1. **General Knowledge**
   - What is localhost/127.0.0.1
   - What is 0.0.0.0
   - What is /etc/hosts
   - How to display your machine’s active network interfaces

### Copyright and Plagiarism

Remember the importance of academic integrity:

- Do not copy or publish content from this project.
- Plagiarism is strictly forbidden and can lead to removal from the program.

## Project Requirements

### General Guidelines

- Allowed Editors: vi, vim, emacs
- Scripts will be interpreted on Ubuntu 20.04 LTS
- All script files must be executable
- Bash scripts should pass Shellcheck (version 0.7.0 via apt-get) without errors
- Use `#!/usr/bin/env bash` as the first line in all Bash scripts
- End all files with a new line
- Include a mandatory README.md file at the project's root

### Tasks Overview

#### Task 0: Change Your Home IP

Write a Bash script to configure an Ubuntu server with the following requirements:

- `localhost` resolves to `127.0.0.2`
- `facebook.com` resolves to `8.8.8.8`

Example usage:

```bash
$ sudo ./0-change_your_home_IP
```

#### Task 1: Show Attached IPs

Write a Bash script to display all active IPv4 IPs on the executing machine.

Example:

```bash
$ ./1-show_attached_IPs
10.0.2.15
127.0.0.1
```

#### Task 2: Port Listening on Localhost (Advanced)

Write a Bash script that listens on port 98 on localhost. This can be utilized for debugging socket connection issues or testing network connectivity.

Example usage:

```bash
# Terminal 0
$ sudo ./100-port_listening_on_localhost

# Terminal 1
$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is '^]'.
Hello world
test
```

### Conclusion

This project provides an opportunity to deepen your understanding of advanced networking concepts. Remember to adhere to the guidelines and submit your solutions before the deadline. Good luck, and may your packets travel swiftly!

**Copyright © 2024 ALX, All rights reserved.**

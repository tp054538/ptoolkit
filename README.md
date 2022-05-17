# ptoolkit
PToolkit is developed to ease the use of penetration testing tools with minimal knowledge and effort.

PToolkit provides a simple UI that let user to view integrated tools' main arguments. Users can select the arguments and provide value for that argument.
All argument inputs are implemented with multiple input validation that help user to reduce the occurence of invalid argument value that lead to a different attack result.
There are many input validations implemented, such as blank input, input with spaces, valid services, check existing file, valid port range, argument value's format check, and etc.

After users had provided the argument value, the command is generated on the user interface immediately. The user can launch the attack once all required arguments are not empty.

PToolkit provide a simple way to launch an attack without memorizing different tools arguments keyword and generate the command automatically to avoid a typo in the error-prone command.

Currently PToolkit support the following features:

1. Install, update, uninstall integrated tools.
2. Batch installation, update, and uninstallation.
3. Connect to Tor Proxy
4. Reconnaissance
5. Scanning
6. Web application scanning and vulnerability scanner
7. Password attack
8. Hash Dictionary/Brute Force Attack
9. Denial-of-Service Attack
10. SQL injection Attack
11. Directory and Files discovery
12. Generate Payload (MSFvenom)
13. Shortcut to select wordlists from SecLists

Requirements:
1. Kali Linux (or debian-based system)
2. Advanced Packaging Tool (APT) installed
3. Python3

*Please run this tool in terminal with black background because some words might be hidden if the background colour is same with the text colour.

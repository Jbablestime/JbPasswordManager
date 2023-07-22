# JbPasswordManager
A password manager I made in Python

## Dependencies 
```
pip install colorama
```

## Features
- supports Email/Password storing.
- supports Email/Password changing.
- authorization system using set passcode. (must be numerical)
- first time setup
- passwords stored locally in a `.JSON` file
- password combo support `email-password` format

## Python to Executable

**step one**
```
pip install pyinstaller
```

**step two**
1. `cd` to the directory holding the `main.py` file
2. run `pyinstaller main.py --onefile --name Password Manager`
3. wait for the compiling to finish
4. go into the `\dist` directory and find the `main.exe` file
5. drag the `main.exe` file to where the `main.py` directory is
6. execute the `main.exe` file
7. all done!

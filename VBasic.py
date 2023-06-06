#python 3.7.1
#name : Vbasic
#version 1.42.2
import random
import os
vars = {}
functions = {}
print("Welcome To VBasic")
print("the console based programming language.")
version = '1.45.1'
helpCmd = 'help()'
print(f"You are currently using VBasic {version}")
print(f"type {helpCmd} in the console for help")
while True:
    
    cmd = input("Vbasic > ")
    if len(cmd) < 5:
        if cmd[1] == "+":
            print(float(cmd[0]) + float(cmd[2:4]))
        elif cmd[1] == "-":
            print(float(cmd[0]) - float(cmd[2:4]))
        elif cmd[1] == "/":
            print(float(cmd[0]) / float(cmd[2:4]))
        elif cmd[1] == "*":
            print(float(cmd[0]) * float(cmd[2:4]))
        else :
            print("Error while calculating")
    elif cmd.startswith("write:") and cmd.endswith(""):
        print(cmd[6:])
    elif cmd.startswith("var ") and cmd.endswith(";"):
        vars = {cmd[3:6]: cmd[7:10]}
    elif cmd.startswith("print:") and cmd.endswith(""):
        if cmd in vars:
            print(var)
    elif cmd.startswith("loop(") and cmd.endswith(")") :
        times = int(cmd[5:10])
        for i in range(times):
            print(cmd[11:40].replace(")",""))  
    elif cmd.startswith("openandview(") and cmd.endswith(")"):
        file = open(str(cmd[12:].replace(")","")))
        text = file.read()
        print(text)
    elif cmd.startswith("length(") and cmd.endswith(")"):
        print(len(cmd[8:].replace(")","")))
    elif cmd.startswith("openandwrite(") and cmd.endswith(")"):
        file = open(str(cmd[13:].replace(")","")))
        writ = str(input(f"what to write? "))
        text = file.write(writ)
        print(text)
    elif cmd == "help()":
        print("openandview\nwrite:\nprint:\nvar\nloop()\nlength()\ncalculate\nexample-3*2\n6\nclear\n(#function code)\nget(input msg here)\nif(condition)\ngetandprint()\nrand(")
    elif cmd == "clear":
        os.system("clear")
        print("Welcome To VBasic")
        print("the console based programming language.")
        version = '1.42.2'
        helpCmd = 'help'
        print(f"You are currently using VBasic {version}")
        print(f"type {helpCmd} in the console for help")
    elif cmd.startswith("(") and cmd.endswith(")"):
        functions = {cmd[1:10]: cmd[11:20]}
    elif cmd.startswith("if(") and cmd.endswith(")"):
        cum = cmd[3:].replace(")","")
        if cum:
            print(True)
        else:
            print(False)
    elif cmd.startswith("get(") and cmd.endswith(")"):
        inpMsg = cmd[4:].replace(")","")
        input(inpMsg)
    elif cmd.startswith("getandprint(") and cmd.endswith(")"):
        inpMsg = cmd[12:].replace(")","")
        print(input(inpMsg))
    elif cmd.startswith("rand(") and cmd.endswith(")"):
        number = random.randint(int(cmd[5], cmd[5:7].replace(")","")))
        print(number)
    else:
        print("Error while parsing")
import CroptographyModulePassword
from CroptographyModulePassword.HashingFile import hashfile

command = input("select your algorithm >? ")


def run(runfile):
    with open(runfile, "r") as rnf:
        exec(rnf.read())

global x
if command == "1":
    run("RsaAlgorithm.py")
if command == "2":
    x = hashfile()
    print(x)
    f = open("hash.txt", "a")
    hashM = f.write(f"{x}\n")
    f.close()

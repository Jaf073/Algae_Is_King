import sys

def convert(string):
    temp = ""
    finalConvert = ""
    for i in string:
        temp = temp + str(i)
        if(temp == "zero"):
            finalConvert = finalConvert + str(0)
            temp = ""
        elif(temp == "one"):
            finalConvert = finalConvert + str(1)
            temp = ""
    print(finalConvert)

def main():
    inp = sys.stdin.read()
    convert(inp)

main()

import sys

def convert(string):
    temp = ""
    finalConvert = ""
    for i in string:
        temp = temp + str(i)
        if(temp == "o"):
            finalConvert = finalConvert + str(0)
            temp = ""
        elif(temp == "l"):
            finalConvert = finalConvert + str(1)
            temp = ""
    print(finalConvert)

def main():
    inp = sys.stdin.read()
    convert(inp)

main()

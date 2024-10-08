import re

def infoGather(keywords):
    # iterates through info file and looks for keywords in a text document
    with open("info", "r") as info:
        # chatgpt helped with this part
        for lineNumber, line in enumerate(info):
            for keyword in keywords:
                for match in re.finditer(re.escape(keyword), line):
                    startIndex = max(match.start() - 1, 0)
                    endIndex = min(match.end() + 20, len(line))
                    
                    # gets the name and email after keyword
                    name_and_email = line[startIndex:endIndex]
                    
                    # print result
                    print(name_and_email)

def main():
    # sets keywords to look for
    keywords = ["name", "mailto"]
    
    infoGather(keywords)

main()

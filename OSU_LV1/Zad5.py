filename = "SMSSpamCollection.txt"

# Zadatak pod a)

rjecnik =  {'ham':0,'spam':0}
hamCount = 0
spamCount = 0
keyword = ""

with open(filename,encoding="utf8") as file:
    for line in file:
        for word in line.split():
            if word == "ham":
                keyword = "ham"
                hamCount += 1
            elif word == "spam":
                keyword = "spam"
                spamCount += 1
            else: 
                rjecnik[keyword] +=1
    file.close()

print("Prosjecan broj rijeci u HAM-ovima: ",rjecnik["ham"]/hamCount)
print("Prosjecan broj rijeci u SPAM-ovima: ",rjecnik["spam"]/spamCount)


# Zadatak pod b)

def CheckExclamation(text):
    if text[len(text)-2] == "!":
        return True

exclamationCount = 0
with open(filename,encoding="utf8") as file:
    for line in file:
        for word in line.split():
            if word == "ham": break
            elif word == "spam": 
                if CheckExclamation(line):
                    exclamationCount += 1
    file.close()
print(exclamationCount) 




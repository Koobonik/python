f = open("yesterday.txt", 'r')
hello = f.readlines()
f.close()

contents = ""
for line in hello:
    contents += line.strip() + "\n"


number_of_yesterday = contents.upper().count("YESTERDAY")
print(number_of_yesterday)
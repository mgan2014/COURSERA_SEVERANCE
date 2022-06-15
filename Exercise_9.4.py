name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
senders = dict()
for line in handle:
    if line.startswith('From '):
        sender = line.split()[1]
        print(sender)
        senders[sender] = senders.get(sender,0) + 1
print(senders)
count = 0
topgun = None
for people,number in senders.items():
    if number > count:
        count = number
        topgun = people
print(senders[topgun])
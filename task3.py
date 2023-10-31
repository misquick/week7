file_name = 'mbox.txt'
try:
    with open(file_name, 'r') as file:
        senders = []
        for line in file:
            if line.startswith('From ') and not line.startswith('From: '):
                sender = line.split()[1]
                senders.append(sender)
                print(sender)

        total_lines = len(senders)
        print(f"Total {total_lines} lines were printed")
except FileNotFoundError:
    print(f"File '{file_name}' not found.")

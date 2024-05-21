chat = []

while True:
    command = input().split()

    if command[0] == "Chat":
        chat.append(command[1])
    elif command[0] == "Delete":
        if command[1] in chat:
            chat.remove(command[1])
    elif command[0] == "Edit":
        if command[1] in chat:
            index = chat.index(command[1])
            chat[index] = command[2]
    elif command[0] == "Pin":
        if command[1] in chat:
            chat.remove(command[1])
            chat.append(command[1])
    elif command[0] == "Spam":
        for i in range(1, len(command)):
            chat.append(command[i])
    elif command[0] == "end":
        for message in chat:
            print(message)
        break

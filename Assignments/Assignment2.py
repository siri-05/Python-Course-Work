no_of_messages=int(input("Enter the number of messages: "))
messages=list()
for i in range(no_of_messages):
    temp=tuple(input().split(": "))
    messages.append(temp)

def choice1():
    #Count total number of messages
    print(f"Total messages: {no_of_messages}")

def choice2():
    #Identify unique users in chat
    d=dict(messages)
    users=set(d.keys())
    print(users)

def choice3():
    #Count total words in the chat
    total=0
    for i in range(no_of_messages):
        words=messages[i][1].split()
        total+=len(words)
    print(f"Total words in the chat: {total}")

def choice4():
    #Calculate average words per message
    no_of_words=list()
    for i in range(no_of_messages):
        words=messages[i][1].split()
        no_of_words.append(len(words))
    average=sum(no_of_words)/len(no_of_words)
    print(f"Average words per message: {average}")

def choice5():
    #Find the longest message sent
    no_of_words=list()
    for i in range(no_of_messages):
        words=list(messages[i][1])
        no_of_words.append(len(words))
    j=no_of_words.index(max(no_of_words))
    print(f"Longest message: {messages[j][1]}")

def choice6():
    #Find the most active user
    d=dict(messages)
    users=list(d.keys())
    active_users=dict()
    for i in range(len(users)):
        active_users[users[i]]=0
    for i in range(no_of_messages):
        active_users[messages[i][0]]+=1
    active=max(active_users.values())
    activeUser=list()
    for i in active_users.keys():
        if active_users[i]==active:
            activeUser.append(i)
    print(f"Most active user: {activeUser} ({active} messages)")

def choice7():
    #Get message count for a specific user
    d=dict(messages)
    users=list(d.keys())
    users_messages=dict()
    for i in range(len(users)):
        users_messages[users[i]]=0
    for i in range(no_of_messages):
        users_messages[messages[i][0]]+=1
    specific_user=input("Enter the user: ")
    print(f"Messages sent by {specific_user}: {users_messages[specific_user]}")

def choice8():
    #Find the most frequently used word by a specific user
    specific_user=input("Enter the user: ")
    list_of_words=list()
    for i in range(no_of_messages):
        if messages[i][0]==specific_user:
            list_of_words.extend(messages[i][1].split())
    most_frequent=max(set(list_of_words), key=list_of_words.count)
    print(f"Most frequent word used by {specific_user}: \"{most_frequent}\"")

def choice9():
    #Retrieve the first and last message sent by the user
    specific_user=input("Enter the user: ")
    temp=0
    final=""
    for i in range(no_of_messages):
        if messages[i][0]==specific_user and temp==0:
            print(f"First message by {specific_user}: \"{specific_user}: {messages[i][1]}\"")
            temp+=1
        elif messages[i][0]==specific_user and temp>0:
            final=messages[i][1]
    print(f"Last message by {specific_user}: \"{specific_user}: {final}\"")

def choice10():
    #Check if a user is present in the chat
    specific_user=input("Enter the user: ")
    d=dict(messages)
    users=set(d.keys())
    if specific_user in users:
        print(f"User \'{specific_user}\' is found in the chat.")
    else:
        print(f"User \'{specific_user}\' not found in the chat.")

def choice11():
    #Find commonly repeated words
    list_of_words=list()
    for i in range(no_of_messages):
        list_of_words.extend(messages[i][1].split())
    temp=dict()
    for i in range(len(list_of_words)):
        temp[list_of_words[i]]=list_of_words.count(list_of_words[i])
    m=max(temp.values())
    commonly_used_words=set()
    for i in temp.keys():
        if temp[i]==m:
            commonly_used_words.add(i)
    print(f"Common repeated words: {commonly_used_words}")

def choice12():
    #Identify the user with the longest average message length
    d=dict(messages)
    users=list(d.keys())
    longest_messages=dict()
    for i in range(len(users)):
        longest_messages[users[i]]=list()
    for i in range(no_of_messages):
        longest_messages[messages[i][0]].append(len(messages[i][1]))
    for i in longest_messages.keys():
        avg=sum(longest_messages[i])/len(longest_messages[i])
        longest_messages[i]=avg
    highest=max(longest_messages.values())
    highest_user=""
    for i in longest_messages.keys():
        if longest_messages[i]==highest:
            highest_user=i
    print(f"User with longest average message: {highest_user} (avg {highest} words)")

def choice13():
    #Count how many messages mention a specific user
    specific_user=input("Enter the user: ")
    count=0
    for i in range(no_of_messages):
        if specific_user in messages[i][1]:
            count+=1
    print(f"Messages mentioning \'{specific_user}\': {count}")

def choice14():
    #Remove duplicate messages
    temp=list()
    for i in range(no_of_messages):
        temp.append(messages[i][1])
    unique_messages=list(set(temp))
    print(f"Unique messages count: {len(unique_messages)}\nUnique messages:")
    for i in range(len(unique_messages)):
        print(f"{unique_messages[i]}")

def choice15():
    #Sort messages alphabetically
    sorted_messages=messages.copy()
    sorted_messages.sort(key=lambda x:x[1])
    print("Sorted messages:")
    for i in range(no_of_messages):
        print(f"{sorted_messages[i][0]}: {sorted_messages[i][1]}")

def choice16():
    #Extract all questions asked in the chat
    list_of_messages=list()
    for i in range(no_of_messages):
        if '?' in messages[i][1]:
            list_of_messages.append(messages[i][1])
    print(f"All questions asked in the chat: {list_of_messages}")

def choice17():
    #Calcualte the reply ratio between two users
    users=input("Enter the users: ").split(" and ")
    ratio=0
    for i in range(no_of_messages):
        if messages[i][0]==users[1]:
            if users[0] in messages[i][1]:
                ratio+=1
    print(f"Reply ratio from {users[1]} to {users[0]}: {ratio} replies")

def choice18():
    #Check for deleted messages
    count=0
    for i in range(no_of_messages):
        if "This message was deleted" in messages[i][1]:
            count+=1
    print(f"Deleted messages found: {count}")

temp=0
while temp==0:
    print("Analysis Options:\n1. Count total number of messages\n2. Identify unique users in chat" \
    "\n3. Count total words in the chat\n4. Calculate average words per message\n5. Find the longest message sent" \
    "\n6. Find the most active user\n7. Get message count for a specific user" \
    "\n8. Find the most frequently used word by a specific user" \
    "\n9. Retrieve the first and last message sent by the user\n10. Check if a user is present in the chat" \
    "\n11. Find commonly repeated words\n12. Identify the user with the longest average message length" \
    "\n13. Count how many messages mention a specific user\n14. Remove duplicate messages" \
    "\n15. Sort messages alphabetically\n16. Extract all questions asked in the chat" \
    "\n17. Calcualte the reply ratio between two users\n18. Check for deleted messages")
    choice=int(input("Choose your analysis option: "))
    if choice==1:
        choice1()
        temp+=1
    elif choice==2:
        choice2()
        temp+=1
    elif choice==3:
        choice3()
        temp+=1
    elif choice==4:
        choice4()
        temp+=1
    elif choice==5:
        choice5()
        temp+=1
    elif choice==6:
        choice6()
        temp+=1
    elif choice==7:
        choice7()
        temp+=1
    elif choice==8:
        choice8()
        temp+=1
    elif choice==9:
        choice9()
        temp+=1
    elif choice==10:
        choice10()
        temp+=1
    elif choice==11:
        choice11()
        temp+=1
    elif choice==12:
        choice12()
        temp+=1
    elif choice==13:
        choice13()
        temp+=1
    elif choice==14:
        choice14()
        temp+=1
    elif choice==15:
        choice15()
        temp+=1
    elif choice==16:
        choice16()
        temp+=1
    elif choice==17:
        choice17()
        temp+=1
    elif choice==18:
        choice18()
        temp+=1
    else:
        print("Please choose correctly according to the options")
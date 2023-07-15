import copy

invite_list = ['A', 'B', 'C']
for person in invite_list:
    print(f"{person}, welcome to my party")
    
print("but B have no time...")
invite_list[1] = "B1"
for person in invite_list:
    print(f"{person}, welcome to my party")
   
print("I find a bigger table...")
invite_list1 = ['D','E','F']
invite_list.insert(0, invite_list1[0])
invite_list.insert(int(len(invite_list)/2), invite_list1[1])
invite_list.append(invite_list1[2])
for person in invite_list:
    print(f"{person}, welcome to my party")
    
print("I am sorry that only 2 persons could come")
copy_list = copy.copy(invite_list)
for person in copy_list:
    if len(invite_list) > 2:
        print(f"{invite_list.pop()}, sorry about that.")

del invite_list[1]
del invite_list[0]
print(f"final list: {invite_list}, lenth: {len(invite_list)}")
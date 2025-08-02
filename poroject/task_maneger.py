# Just do it :-)

import os

collection_task = []


def Task_maneger(task_list):
    print(f"\nxxx< Task maneger >xxx\n")
    print(f"1- show tasks")
    print(f"2- tasks (add/delet)")
    print(f"3- Change status")
    print(f"4- exit")
    

    selection = input("select action 1-4")

    if selection == "1":
        show(task_list)
        os.system("cls")
    
    if selection == "2":
        ad(task_list)
        os.system("cls")

    if selection == "3":
        status(task_list)
        os.system("cls")

    if selection == "4":
        return #exit
    else:
        os.system("cls")
        print("\n ‼️ (Invaild selection. Please try again.)\n")
        Task_maneger(collection_task)


    
def show(task_list, btm = True):
    os.system("cls")
    if not task_list:
        print("(\n 🚫 (No tasks available.)")
    else:
        print("\n --- Currnet Tasks ---")
        for index, task in enumerate(task_list, start=1):
               print(f"{index}. {task}")
    if btm:
        Task_maneger(task_list)


def adding (task_list):
     os.system("cls")
     task = input("\n |--> Enter the task: ")
     if task:
        task_list.append(task + " ❌")
        print(f"\n✅ (Task '{task}' added successfully.)")
        Task_maneger(task_list)
     else:
        print("\n‼️ (Task cannot be empty.)")
        adding(task_list)
def deleting (task_list):
    if not task_list:
        print("\n ‼️ (No tasks available to delete.)")
        Task_maneger(task_list)

    # if avaialbe
    show(task_list, False)
    try:
        task_index = int(input("Enter the task number for delete: ")) - 1
        if 0 <= task_index < len(task_list):
            removed_task = task_list.pop(task_index)
            print(f"\n✅ (Task '{removed_task}' deleted successfully.)")
        else:
            print("\n ‼️ (Invalid task number.)")
    except ValueError:
        print("\n ‼️ (Please enter a valid number)")

def ad(task_list):

#we use input to show what action to do with a = add and d = delet

    wich_one = input("for Addinig use (A) for delet use (D)")

    add = ['a','A','add','ADD']
    delet = ['d','D','delet','DELET']
    if wich_one in add:
        adding (task_list)
    elif wich_one in delet:
        deleting (task_list)
    else:
        print(f"\nplese use curect word for example we use {add} for adding and use {delet} for deleting\n")
        ad(task_list)
    
    Task_maneger(task_list)


def status(task_list):
    if not task_list:
        print("\n ‼️ (No tasks available to change status.)")
        Task_maneger(task_list)

    show(task_list, False)
    try:
        task_index = int(input("Enter the task number for update: ")) - 1
        if 0 <= task_index < len(task_list):
            task_list[task_index] = task_list[task_index][:-1] + " ✅"
            print(f"\n ✅ Your Task :'{task_list[task_index][:-1]} completed.'")
        else:
            print("\n ‼️ (Invalid task number.)")
    except ValueError:
        print("\n ‼️ (Please enter a valid number)")

    Task_maneger(task_list)

if __name__ == "__main__":
    Task_maneger(collection_task)
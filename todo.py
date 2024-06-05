from pymongo import MongoClient
from bson import ObjectId
import config

try:
    connect_db = MongoClient(config.MONGODB_URL)
    db = connect_db["Todo_CLI"]
    todo_collection = db["Todo"]
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit(1)

def todos_list():
    todo = todo_collection.find()
    if todo:
        for todos in todo:
            print(f"Todo ID: {todos["_id"]} | Todo: {todos["todo"]} | Complete: {todos["is_todo_complete"]}")
    else:
        print("\nTodo does not exist")
        
def complete_todos_list():
    todo = todo_collection.find({"is_todo_complete": True})
    if todo:
        for todos in todo:
            print(f"Todo ID: {todos["_id"]} | Todo: {todos["todo"]} | Complete: {todos["is_todo_complete"]}")

def incomplete_todos_list():
    todo = todo_collection.find({"is_todo_complete": False})
    if todo:
        for todos in todo:
            print(f"Todo ID: {todos["_id"]} | Todo: {todos["todo"]} | Complete: {todos["is_todo_complete"]}")

def add_todo(todo, is_todo_complete):
    if (len(todo) == 0):
        print("\nTodo is empty try again")
        return

    create_todo = todo_collection.insert_one(
        {
            "todo": todo,
            "is_todo_complete": is_todo_complete
        }
    )

    if create_todo:
        print("\nTodo create successfully")
    else:
        print("\nTodo not created please try again")

def complete_todo(todo_id):
    todo = todo_collection.find_one_and_update(
        {   
            "_id": ObjectId(todo_id)
        },
        {
            "$set": {"is_todo_complete": True}
        }
    )

    if todo:
        print("\nTodo is completed")
    else:
        print("\nFailed to complete todo")

def update_todo(todo_id, new_todo):
    if (len(new_todo) == 0):
        print("\nTodo is empty try again")
        return
    
    todo = todo_collection.find_one_and_update(
        {
            "_id": ObjectId(todo_id)
        },
        {
            "$set": {"todo": new_todo}
        }
    )
    if todo:
        print("\nTodo update successfully")
    else:
        print("\nFailed to update todo")

def delete_todo(todo_id):
    todo = todo_collection.find_one_and_delete({"_id": ObjectId(todo_id)})
    if todo:
        print("\nTodo delete successfully")
    else:
        print("\nFailed to delete todo")

def main():
    while True:
        print("\n1. List of all todos.")
        print("2. List of Complete todos.")
        print("3. List of Incomplete todos.")
        print("4. Add todo.")
        print("5. Mark as complete todo.")
        print("6. Update todo.")
        print("7. Delete todo.")
        print("8. Exit todo app.")
        choice = input("\nEnter the your choice: ")

        match choice:
            case "1":
                todos_list()
            case "2":
                complete_todos_list()
            case "3":
                incomplete_todos_list()
            case "4":
                todo = input("Enter the today todo: ")
                is_todo_complete = False
                add_todo(todo, is_todo_complete)
            case "5":
                todo_id = input("Enter the todo ID to complete: ")
                complete_todo(todo_id)
            case "6":
                todo_id = input("Enter the todo ID to update: ")
                new_todo = input("Enter the new today todo: ")
                update_todo(todo_id, new_todo)
            case "7":
                todo_id = input("Enter the todo ID to delete: ")
                delete_todo(todo_id)
            case "8":
                break
            case _:
                print("Invalid choice")



if __name__ == "__main__":
    main()
# shopping_list.py

shopping_list = []

while True:
    choice = input("\nWould you like to (add / remove / show / done)? ").strip().lower()
    
    if choice == "add":
        item = input("Enter the item to add: ").strip()
        shopping_list.append(item)
        print(f"'{item}' has been added to your list.")
        
    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()
        # Safe check using 'in' before removing to avoid crashing
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from your list.")
        else:
            print("That item is not on your list.")
            
    elif choice == "show":
        print("\n--- Current Shopping List ---")
        if not shopping_list:
            print("Your list is currently empty.")
        else:
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")
        print("-----------------------------")
        
    elif choice == "done":
        print("Goodbye! Thanks for using the Shopping List Manager.")
        break
        
    else:
        print("Invalid choice. Please type add, remove, show, or done.")

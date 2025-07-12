import json
path = "D:/knowledge_base.json"

def load_knowledge_base(path):
        with open(path, "r") as file:
            data= json.load(file)
        return data
        
def save_knowledge_base(path, data):
        with open(path, "w") as file:
            json.dump(data, file, indent=4)

def add_person(name, info, knowledge_base): #name is key and info is value
        knowledge_base[name] = info
        print(f"Information about {name} has been stored.")

def get_person_info(name, knowledge_base):
        return knowledge_base.get(name, None)

def delete_person(name, knowledge_base):
        if name in knowledge_base:
            del knowledge_base[name]
            print(f"{name} has been deleted from the database.")
        else:
            print(f"{name} does not exist in the database.")

def main():
    knowledge_base = load_knowledge_base(path)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Search for a person")
        print("2. Add a new person")
        print("3. Append information to an existing person")
        print("4. Delete a person")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ").strip()
        
        if choice == "1": 
                name = input("Enter the name of the person to search: ").strip()
                info = get_person_info(name,knowledge_base)

                if info:
                    print(f"\n\n{info}\n\n")
                else:
                    print(f"No information found about {name}.")
        
        elif choice == "2":  
            name = input("Enter the name of the person: ").strip()
            if name in knowledge_base:
                print(f"{name} already exists in the knowledge base.")
                overwrite = input("Do you want to overwrite the existing information? (yes/no): ").strip().lower()
                if overwrite != "yes":
                    print("Skipping. No changes made.")
                    continue
            else:
                info = input(f"Enter information about {name}: ").strip()
                if info:
                    add_person(name, info, knowledge_base)
                else:
                    print("No information provided. Skipping.")
        
        elif choice == "3": 
            name = input("Enter the name of the person to append information: ").strip()
            if name in knowledge_base:
                print(f"Current information about {name}: {knowledge_base[name]}")
                new_info = input(f"Enter additional information about {name}: ").strip()
                if new_info:
                    knowledge_base[name] += " " + new_info 
                    print(f"Information about {name} has been updated.")
                else:
                    print("No additional information provided. Skipping.")
            else:
                print(f"{name} does not exist in th1e knowledge base.")
        
        elif choice == "4":  
            name = input("Enter the name of the person to delete: ").strip()
            delete_person(name, knowledge_base)
        
        elif choice == "5":  
            save_knowledge_base(path, knowledge_base)
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
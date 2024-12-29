import os

# Sample data storage 
users = []
servers = []

# Functions
def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        clear_screen()
        print("Welcome to Collaborative Study Platform")
        print("1. Join a Study Server")
        print("2. Create a Study Server")
        print("3. View Active Study Servers")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            join_server()
        elif choice == '2':
            create_server()
        elif choice == '3':
            view_servers()
        elif choice == '4':
            print("Thank you for using the Collaborative Study Platform!")
            break
        else:
            print("Invalid choice. Please try again.")

def create_server():
    """Allows the user to create a new study server."""
    clear_screen()
    print("Create a Study Server")
    lang = input("Enter language (e.g., English, Spanish): ").strip()
    subject = input("Enter subject (e.g., Math, Science): ").strip()
    chapter = input("Enter chapter: ").strip()
    lesson = input("Enter lesson: ").strip()
    
    server_id = len(servers) + 1
    servers.append({
        "id": server_id,
        "language": lang,
        "subject": subject,
        "chapter": chapter,
        "lesson": lesson,
    })
    
    print(f"Server '{subject} - {chapter} - {lesson}' created successfully!")
    input("Press Enter to return to the main menu...")

def view_servers():
    """Displays all active study servers."""
    clear_screen()
    if not servers:
        print("No active study servers available.")
    else:
        print("Active Study Servers:")
        for server in servers:
            print(f"ID: {server['id']}, Language: {server['language']}, "
                  f"Subject: {server['subject']}, Chapter: {server['chapter']}, "
                  f"Lesson: {server['lesson']}")
    
    input("\nPress Enter to return to the main menu...")

def join_server():
    """Allows a user to join a study server."""
    clear_screen()
    if not servers:
        print("No active study servers to join.")
    else:
        print("Available Study Servers:")
        for server in servers:
            print(f"ID: {server['id']}, Language: {server['language']}, "
                  f"Subject: {server['subject']}, Chapter: {server['chapter']}, "
                  f"Lesson: {server['lesson']}")
        
        try:
            server_id = int(input("\nEnter the ID of the server you want to join: ").strip())
            selected_server = next((server for server in servers if server['id'] == server_id), None)
            
            if selected_server:
                print(f"You have joined the server '{selected_server['subject']} - "
                      f"{selected_server['chapter']} - {selected_server['lesson']}'")
            else:
                print("Invalid server ID. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid server ID.")
    
    input("\nPress Enter to return to the main menu...")

# Entry point
if __name__ == "__main__":
    main_menu()

import src.menu_options as menu_options
import asyncio


while True:
    print("Please select an option")
    print("1. Add user")
    print("2. View users")
    print("3. Add subscriber")
    print("4. Create a document")
    print("5. Upload a document")
    print("6. Exit")
    user_selection = int(input("User selection: "))
    if user_selection == 1:
        menu_options.handle_new_user()
    elif user_selection == 2:
        menu_options.handle_print_users()
    elif user_selection == 3:
        menu_options.handle_subscribe_user()
    elif user_selection == 4:
        asyncio.run(menu_options.handle_document_creation())
    elif user_selection == 5:
        menu_options.handle_document_upload()
    else:
        menu_options.save_state()
        break

import getpass
from Cuenta import Cuenta
from tictactoe import TicTacToe

def crear_cuenta():
    """
    Creates a new account by asking for the user's name and password.
    Returns:
        Cuenta: A new account object.
    """
    nombre = input("Enter your name: ").strip()
    password = getpass.getpass("Enter your password: ").strip()
    return Cuenta(nombre, password)

def main_menu():
    """
    Displays the main menu.
    """
    print("╔════════════════════════════════╗")
    print("║    Welcome to the Bank         ║")
    print("╠════════════════════════════════╣")
    print("║ 1. Login to an account         ║")
    print("║ 2. Create a new account        ║")
    print("║ 3. Exit                        ║")
    print("╚════════════════════════════════╝")

def account_menu(account):
    """
    Displays the account menu for a logged-in user.
    Args:
        account (Cuenta): The logged-in user's account.
    """
    print()
    print("╔════════════════════════════════╗")
    print(f"║      Account Menu - {account.name}      ║")
    print("╠════════════════════════════════╣")
    print("║ b. Get the balance             ║")
    print("║ d. Make a deposit              ║")
    print("║ w. Make a withdrawal           ║")
    print("║ t. View transaction history    ║")
    print("║ p. Change password             ║")
    print("║ h. Play tic-tac-toe            ║")
    print("║ s. Show the account            ║")
    print("║ q. Quit                        ║")
    print("╚════════════════════════════════╝")
    print()

def main():
    """
    The main function to run the bank application.
    """
    # Predefined accounts
    accounts = {
        "Jesus": Cuenta("Jesus", "123", 5000),
        "Raul": Cuenta("Raul", "password123", 5000)
    }

    while True:
        main_menu()
        option = input("Please select an option: ").strip()
        
        if option == '3':
            print("Thank you for visiting the bank. Goodbye!")
            break

        elif option == '2':
            new_account = crear_cuenta()
            accounts[new_account.name] = new_account
            print(f"Account created for {new_account.name} with an initial balance of $20.")

        elif option == '1':
            username = input("Enter your username: ").strip()
            password = getpass.getpass("Enter your password: ").strip()
            
            if username in accounts and accounts[username].password == password:
                account = accounts[username]

                while True:
                    account_menu(account)
                    action = input('What do you want to do? ').lower().strip()
                    
                    if action == 'q':
                        break

                    elif action == 'b':
                        print('Get Balance:')
                        user_password = getpass.getpass('Please enter the password: ')
                        print(account.get_balance(user_password))

                    elif action == 'd':
                        print('Deposit:')
                        try:
                            user_deposit_amount = float(input('Please enter amount to deposit: '))
                        except ValueError:
                            print("Invalid amount. Please enter a number.")
                            continue
                        user_password = getpass.getpass('Please enter the password: ')
                        print(account.deposit(user_deposit_amount, user_password))

                    elif action == 'w':
                        print('Withdraw:')
                        try:
                            user_withdraw_amount = float(input('Please enter the amount to withdraw: '))
                        except ValueError:
                            print("Invalid amount. Please enter a number.")
                            continue

                        user_password = getpass.getpass('Please enter the password: ')
                        print(account.withdraw(user_withdraw_amount, user_password))

                    elif action == 't':
                        print('Transaction History:')
                        user_password = getpass.getpass('Please enter the password: ')
                        print(account.get_transactions(user_password))

                    elif action == 'p':
                        print('Change Password:')
                        old_password = getpass.getpass('Please enter your old password: ')
                        new_password = getpass.getpass('Please enter your new password: ')
                        print(account.change_password(old_password, new_password))

                    elif action == 's':
                        print('Show Account:')
                        print(account.show_account())

                    elif action == 'h':
                        game = TicTacToe(account)
                        game.main()
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Invalid login credentials. Please try again.")
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

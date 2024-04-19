# main.py
import ticket_manager

class Main:
    def run(self):  
        """
        Main function to run the ticket management system.
        """
        

        while True:
            print("\n1. Create Ticket")
            print("2. Resolve Ticket")
            print("3. Reopen Ticket")
            print("4. Print Tickets")
            print("5. Display Ticket Statistics")
            print("6. Exit")    

            choice = input("\nEnter your choice: ")

            if choice == "1":
                ticket_manager.create_ticket()
            elif choice == "2":
                ticket_number = int(input("Enter Ticket Number to Resolve: "))
                ticket_manager.resolve_ticket(ticket_number)
            elif choice == "3":
                ticket_number = int(input("Enter Ticket Number to Reopen: "))
                ticket_manager.reopen_ticket(ticket_number)
            elif choice == "4":
                ticket_manager.print_tickets()
            elif choice == "5":
                ticket_manager.display_ticket_statistics()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main = Main()  
    main.run()
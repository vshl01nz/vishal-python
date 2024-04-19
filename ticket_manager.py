# ticket_manager.py
import ticket

class TicketManager:
    def __init__(self):
        """
        Initialize TicketManager with empty list of tickets and a counter.
        """
        self.tickets = []
        self.counter = 0

    def create_ticket(self):
        """
        Create a new ticket and add it to the list of tickets.
        """
        staff_id = input("Enter Staff ID: ")
        developer_name = input("Enter Ticket Developer Name: ")
        contact_email = input("Enter Contact Email: ")
        description = input("Enter Description of the Issue: ")
        
        ticket = ticket.Ticket(staff_id, developer_name, contact_email, description)
        ticket.submit_ticket(self.counter)
        self.counter += 1
        self.tickets.append(ticket)

    def resolve_ticket(self, ticket_number):
        """
        Resolve a ticket by providing a response.
        """
        response = input("Enter Response to the Ticket: ")
        for ticket in self.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.respond_to_ticket(response)

    def reopen_ticket(self, ticket_number):
        """
        Reopen a closed ticket.
        """
        for ticket in self.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.reopen_ticket()

    def print_tickets(self):
        """
        Print information for all tickets.
        """
        for ticket in self.tickets:
            ticket.print_ticket_info()

    def display_ticket_statistics(self):
        """
        Display statistics about the tickets.
        """
        total_tickets = len(self.tickets)
        resolved_tickets = sum(1 for ticket in self.tickets if ticket.status == "Closed")
        open_tickets = sum(1 for ticket in self.tickets if ticket.status == "Open")

        print("Tickets Created:", total_tickets)
        print("Tickets Resolved:", resolved_tickets)
        print("Tickets To Solve:", open_tickets)
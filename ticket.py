# ticket.py
class Ticket:
    def __init__(self, staff_id, developer_name, contact_email, description):
        """
        Initialize a ticket with provided information.
        """
        self.staff_id = staff_id
        self.developer_name = developer_name
        self.contact_email = contact_email
        self.description = description
        self.ticket_number = None
        self.response = "Not Yet Provided"
        self.status = "Open"

    def submit_ticket(self, counter):
        """
        Assign a ticket number to the ticket.
        """
        counter += 2000
        self.ticket_number = counter

    def respond_to_ticket(self, response):
        """
        Add a response to the ticket and mark it as closed.
        """
        self.response = response
        self.status = "Closed"

    def reopen_ticket(self):
        """
        Reopen a closed ticket.
        """
        self.status = "Reopened"

    def print_ticket_info(self):
        """
        Print ticket information.
        """
        print("Ticket Number:", self.ticket_number)
        print("Ticket Creator:", self.developer_name)
        print("Staff ID:", self.staff_id)
        print("Email Address:", self.contact_email)
        print("Description:", self.description)
        print("Response:", self.response)
        print("Ticket Status:", self.status)
        print()
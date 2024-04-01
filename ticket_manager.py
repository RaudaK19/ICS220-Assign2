from ticket import Ticket  # Import Ticket class

class TicketManager:
    """
    Manages the sale of tickets in the museum.

    Attributes:
    - tickets_sold (List[Ticket]): List of tickets sold.
    """

    def __init__(self):
        self.tickets_sold = []

    def sell_ticket(self, ticket):
        """Sell a ticket."""
        self.tickets_sold.append(ticket)

    def display_tickets_sold(self):
        """Display information about tickets sold."""
        for ticket in self.tickets_sold:
            print(f"Event: {ticket.get_event_name()}, Type: {ticket.get_ticket_type()}, Price: {ticket.get_price()}")
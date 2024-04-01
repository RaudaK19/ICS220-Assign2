class Ticket:
    """
    Represents a ticket for an event in the museum.

    Attributes:
    - event_name (str): The name of the event.
    - ticket_type (str): The type of the ticket.
    - price (float): The price of the ticket.
    """

    def __init__(self, event_name, ticket_type, price):
        self.event_name = event_name
        self.ticket_type = ticket_type
        self.price = price

    # Getter methods
    def get_event_name(self):
        """Get the name of the event."""
        return self.event_name
    
    def get_ticket_type(self):
        """Get the type of the ticket."""
        return self.ticket_type
    
    def get_price(self):
        """Get the price of the ticket."""
        return self.price
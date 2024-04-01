class SpecialEvent:
    """
    Represents a special event in the museum.

    Attributes:
    - location (str): The location of the special event.
    - duration (str): The duration of the special event.
    - ticket_price (float): The price of tickets for the special event.
    """

    def __init__(self, location, duration, ticket_price):
        self.location = location
        self.duration = duration
        self.ticket_price = ticket_price

    # Getter methods
    def get_location(self):
        """Get the location of the special event."""
        return self.location
    
    def get_duration(self):
        """Get the duration of the special event."""
        return self.duration
    
    def get_ticket_price(self):
        """Get the ticket price of the special event."""
        return self.ticket_price
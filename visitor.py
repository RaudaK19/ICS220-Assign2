class Visitor:
    """
    Represents a visitor to the museum.

    Attributes:
    - name (str): The name of the visitor.
    - age (int): The age of the visitor.
    - ticket_purchased (bool): Indicates whether the visitor has purchased a ticket.
    - ticket_price (float): The price of the ticket purchased by the visitor.
    - ticket_type (str): The type of ticket purchased by the visitor.
    """

    def __init__(self, name, age, ticket_purchased, ticket_price, ticket_type):
        self.name = name
        self.age = age
        self.ticket_purchased = ticket_purchased
        self.ticket_price = ticket_price
        self.ticket_type = ticket_type

    # Getter and Setter methods
    def get_name(self):
        """Get the name of the visitor."""
        return self.name
    
    def set_name(self, name):
        """Set the name of the visitor."""
        self.name = name
    
    def get_age(self):
        """Get the age of the visitor."""
        return self.age
    
    def set_age(self, age):
        """Set the age of the visitor."""
        self.age = age
    
    def get_ticket_purchased(self):
        """Check if the visitor has purchased a ticket."""
        return self.ticket_purchased
    
    def set_ticket_purchased(self, ticket_purchased):
        """Set whether the visitor has purchased a ticket."""
        self.ticket_purchased = ticket_purchased
    
    def get_ticket_price(self):
        """Get the price of the ticket purchased by the visitor."""
        return self.ticket_price
    
    def set_ticket_price(self, ticket_price):
        """Set the price of the ticket purchased by the visitor."""
        self.ticket_price = ticket_price
    
    def get_ticket_type(self):
        """Get the type of ticket purchased by the visitor."""
        return self.ticket_type
    
    def set_ticket_type(self, ticket_type):
        """Set the type of ticket purchased by the visitor."""
        self.ticket_type = ticket_type
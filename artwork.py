class Artwork:
    """
    Represents an artwork in the museum's collection.

    Attributes:
    - title (str): The title of the artwork.
    - artist (str): The artist of the artwork.
    - date_of_creation (str): The date of creation of the artwork.
    - historical_significance (str): The historical significance of the artwork.
    - exhibition_location (str): The location where the artwork is exhibited.
    """

    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.exhibition_location = exhibition_location

    # Getter and Setter methods
    def get_title(self):
        """Get the title of the artwork."""
        return self.title
    
    def set_title(self, title):
        """Set the title of the artwork."""
        self.title = title
    
    def get_artist(self):
        """Get the artist of the artwork."""
        return self.artist
    
    def set_artist(self, artist):
        """Set the artist of the artwork."""
        self.artist = artist
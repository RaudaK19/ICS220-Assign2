from artwork import Artwork  # Import Artwork class

class Exhibition:
    """
    Represents an exhibition in the museum.

    Attributes:
    - duration (str): The duration of the exhibition.
    - location (str): The location of the exhibition.
    - artworks (List[Artwork]): List of artworks exhibited in the exhibition.
    """

    def __init__(self, duration, location):
        self.duration = duration
        self.location = location
        self.artworks = []

    def add_artwork(self, artwork):
        """Add an artwork to the exhibition."""
        self.artworks.append(artwork)

    # Getter methods
    def get_duration(self):
        """Get the duration of the exhibition."""
        return self.duration
    
    def get_location(self):
        """Get the location of the exhibition."""
        return self.location
    
    def get_artworks(self):
        """Get the list of artworks exhibited in the exhibition."""
        return self.artworks
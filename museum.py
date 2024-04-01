from artwork import Artwork  # Import Artwork class
from exhibition import Exhibition  # Import Exhibition class
from special_event import SpecialEvent  # Import SpecialEvent class

class Museum:
    """
    Represents a museum.

    Attributes:
    - artworks (List[Artwork]): List of artworks in the museum's collection.
    - exhibitions (List[Exhibition]): List of exhibitions hosted by the museum.
    - special_events (List[SpecialEvent]): List of special events hosted by the museum.
    """

    def __init__(self):
        self.artworks = []
        self.exhibitions = []
        self.special_events = []

    def add_artwork(self, artwork):
        """Add an artwork to the museum's collection."""
        self.artworks.append(artwork)

    def add_exhibition(self, exhibition):
        """Add an exhibition to the museum."""
        self.exhibitions.append(exhibition)

    def add_special_event(self, special_event):
        """Add a special event to the museum."""
        self.special_events.append(special_event)

    def display_artworks(self):
        """Display information about artworks in the museum's collection."""
        for artwork in self.artworks:
            print(f"Artwork: {artwork.get_title()}, Artist: {artwork.get_artist()}, Location: {artwork.exhibition_location}")

    def display_exhibitions(self):
        """Display information about exhibitions hosted by the museum."""
        for exhibition in self.exhibitions:
            print(f"Exhibition: {exhibition.get_location()}, Duration: {exhibition.get_duration()}")
            for artwork in exhibition.get_artworks():
                print(f"\tArtwork: {artwork.get_title()}")

    def display_special_events(self):
        """Display information about special events hosted by the museum."""
        for special_event in self.special_events:
            print(f"Special Event: {special_event.get_location()}, Duration: {special_event.get_duration()}, Price: {special_event.get_ticket_price()}")
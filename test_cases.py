from artwork import Artwork
from exhibition import Exhibition
from special_event import SpecialEvent
from ticket import Ticket
from ticket_manager import TicketManager
from museum import Museum
from visitor import Visitor

# Test Case 1: Adding new artwork to the museum
artwork1 = Artwork("Mona Lisa", "Leonardo da Vinci", "c. 1503–1506", "Iconic portrait", "Permanent Gallery")
artwork2 = Artwork("The Starry Night", "Vincent van Gogh", "1889", "Post-Impressionist masterpiece", "Permanent Gallery")
artwork3 = Artwork("The Last Supper", "Leonardo da Vinci", "1495–1498", "Depiction of the Last Supper of Jesus and his disciples", "Permanent Gallery")

# Test Case 2: Opening a new exhibition
exhibition1 = Exhibition("March 1, 2024 - May 31, 2024", "Exhibition Hall A")
exhibition1.add_artwork(artwork1)
exhibition1.add_artwork(artwork2)

# Test Case 3: Opening a special event
special_event1 = SpecialEvent("Outdoor Garden", "April 15, 2024", 100)

# Test Case 4: Selling tickets for the exhibition and special event
ticket_manager = TicketManager()
ticket_manager.sell_ticket(Ticket("Mona Lisa Exhibition", "Regular", 63))
ticket_manager.sell_ticket(Ticket("Mona Lisa Exhibition", "Group", 31.5))
ticket_manager.sell_ticket(Ticket("Special Event: Light Show", "Regular", 100))

# Test Case 5: Displaying information about tickets sold
print("Tickets Sold:")
ticket_manager.display_tickets_sold()

# Test Case 6: Adding new artwork to the museum and displaying artworks
museum = Museum()
museum.add_artwork(artwork1)
museum.add_artwork(artwork2)
museum.add_artwork(artwork3)
museum.display_artworks()

# Test Case 7: Adding new exhibition to the museum and displaying exhibitions
museum.add_exhibition(exhibition1)
museum.display_exhibitions()

# Test Case 8: Adding new special event to the museum and displaying special events
museum.add_special_event(special_event1)
museum.display_special_events()

# Test Case 9: Selling tickets for different types and displaying information about tickets sold
ticket_manager.sell_ticket(Ticket("The Starry Night Exhibition", "Regular", 63))
ticket_manager.sell_ticket(Ticket("The Last Supper Exhibition", "Group", 31.5))
ticket_manager.sell_ticket(Ticket("Special Event: Music Concert", "Regular", 120))
print("Tickets Sold After Additional Sales:")
ticket_manager.display_tickets_sold()

# Test Case 10: Creating a visitor and displaying visitor information
visitor1 = Visitor("John Doe", 30, True, 63, "Regular")
print(f"Visitor: {visitor1.get_name()}, Age: {visitor1.get_age()}, Ticket Purchased: {visitor1.get_ticket_purchased()}, Ticket Price: {visitor1.get_ticket_price()}, Ticket Type: {visitor1.get_ticket_type()}")

# Test Case 11: Adding more artworks to the museum and displaying artworks
artwork4 = Artwork("Guernica", "Pablo Picasso", "1937", "Depicts the bombing of Guernica during the Spanish Civil War", "Permanent Gallery")
artwork5 = Artwork("The Thinker", "Auguste Rodin", "1904", "Bronze sculpture representing a man in sober meditation battling with a powerful internal struggle", "Outdoor Garden")

museum.add_artwork(artwork4)
museum.add_artwork(artwork5)
print("Artworks after adding more:")
museum.display_artworks()

# Test Case 12: Selling more tickets for exhibitions and special events
ticket_manager.sell_ticket(Ticket("Guernica Exhibition", "Regular", 63))
ticket_manager.sell_ticket(Ticket("The Thinker Exhibition", "Group", 31.5))
ticket_manager.sell_ticket(Ticket("Special Event: Dance Performance", "Regular", 80))

print("Tickets Sold After Additional Sales:")
ticket_manager.display_tickets_sold()

# Test Case 13: Creating more visitors and displaying visitor information
visitor2 = Visitor("Alice Smith", 25, False, 0, "None")
visitor3 = Visitor("Bob Johnson", 55, True, 63, "Regular")

print("Visitor Information:")
print(f"Visitor 1: {visitor1.get_name()}, Age: {visitor1.get_age()}, Ticket Purchased: {visitor1.get_ticket_purchased()}, Ticket Price: {visitor1.get_ticket_price()}, Ticket Type: {visitor1.get_ticket_type()}")
print(f"Visitor 2: {visitor2.get_name()}, Age: {visitor2.get_age()}, Ticket Purchased: {visitor2.get_ticket_purchased()}, Ticket Price: {visitor2.get_ticket_price()}, Ticket Type: {visitor2.get_ticket_type()}")
print(f"Visitor 3: {visitor3.get_name()}, Age: {visitor3.get_age()}, Ticket Purchased: {visitor3.get_ticket_purchased()}, Ticket Price: {visitor3.get_ticket_price()}, Ticket Type: {visitor3.get_ticket_type()}")

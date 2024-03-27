#GROUP ONE
#Nziriga Isaac Nickson S23B23/046
#Mutumba Benjamin S23B23/010
#Kiisa Angela Grace S23B23/027
#Odongokara Oscar S23B23/085
#Buwembo David Denzel S23B23/074


       ##Waypoint Class
class Waypoint:
    def __init__(self, location, description):
        self.location = location
        self.description = description
        self.next = None
        self.prev = None  # Only used for BidirectionalRoute
        
        ##Route Class (Singly Linked List)
class Route:
    def __init__(self):
        self.head = None

    def add_waypoint(self, location, description):
        new_waypoint = Waypoint(location, description)
        if not self.head:
            self.head = new_waypoint
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_waypoint

    def insert_waypoint_after(self, target_location, location, description):
        current = self.head
        while current and current.location != target_location:
            current = current.next
        if current is None:
            return "Target waypoint not found"
        new_waypoint = Waypoint(location, description)
        new_waypoint.next = current.next
        current.next = new_waypoint

    def remove_waypoint(self, location):
        current = self.head
        prev = None
        while current and current.location != location:
            prev = current
            current = current.next
        if current is None:
            return "Waypoint not found"
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
            
            ##BidirectionalRoute Class (Doubly Linked List)
            
class BidirectionalRoute(Route):
    def add_waypoint(self, location, description):
        new_waypoint = Waypoint(location, description)
        if not self.head:
            self.head = new_waypoint
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_waypoint
        new_waypoint.prev = last

    def next_waypoint(self, current):
        return current.next if current else None

    def previous_waypoint(self, current):
        return current.prev if current else None
    
    ##Demonstration
# Create a route with 5 waypoints
route = BidirectionalRoute()
route.add_waypoint("A", "Start")
route.add_waypoint("B", "Forest")
route.add_waypoint("C", "Mountain")
route.add_waypoint("D", "River")
route.add_waypoint("E", "End")

# Insert a waypoint after B
route.insert_waypoint_after("B", "F", "Village")

# Remove waypoint D
route.remove_waypoint("D")

# Traverse waypoints in a single direction
current = route.head
while current:
    print(f"Location: {current.location}, Description: {current.description}")
    current = current.next

# Traverse waypoints in both directions using BidirectionalRoute
current = route.head
while current.next:  # Move to the end
    current = current.next
while current:  # Move backwards
    print(f"Location: {current.location}, Description: {current.description}")
    current = current.previous_waypoint(current)

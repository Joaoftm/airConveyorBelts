
def flights(arrivals):
    """Sorted list of flights according to their increasing hour of arrival.
    Requires: arrivals is a list of tuples, each corresponding to one flight
    Ensures: list of tuples, each corresponding to one flight, sorted according to
    their increasing arrival time."""
    
    
    return sorted(arrivals, key=getKeyArrivals)
     
def getKeyArrivals(item): #Indicates the list element to which it will order the flight (arrival time of each flight)
    return item[2]

def belts(belts):
    """Sorted list of belts according to their increasing hour of availability.
    Requires: belts is a list of pairs, where the first component is the number of
    the belt and the second component the next time this belt will be available
    within the current period of operation
    Ensures: list of pairs, each corresponding to one belt, sorted according to their
    increasing hour of availability."""
    
    return sorted(belts, key=getKeyBelts)
    

def getKeyBelts(item):   #Indicates the list element to which it will sort belts (minute availability)
    
    return item[0]


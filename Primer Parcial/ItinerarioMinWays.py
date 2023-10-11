# Function to print the itinerary starting from a given source `src`
def print_itinerary(dictionary, src):
    dest = dictionary.get(src)
    if not dest:
        return
 
    print(src + ' —> ' + dest)
    print_itinerary(dictionary, dest)
 
 
# Function to find the itinerary from the given list of departure and arrival airports
def findItinerary(tickets):
 
    # construct a set of destination airports
    destinations = {*tickets.values()}
 
    # consider each departure airport to find the source airport
    for k, v in tickets.items():
        # source airport will not be present in the list of destination airports
        if k not in destinations:
            # when the source airport is found, print the itinerary
            print_itinerary(tickets, k)
            return
 
 
if __name__ == '__main__':
 
    # input: list of tickets
    tickets = {
        'Constitucion':'Isabel la Catolica',
        'Chabacano':'Neza',
        '4 caminos': 'Puerto Aereo',
        'Puerto Aereo':'Terminal de Autobuses',
        'Pino Suarez':'Zocalo',
        'Terminal de Autobuses':'Pino Suarez',
        'Zocalo':'Chabacano',
        'Neza':'Constitucion'
    }
 
    findItinerary(tickets)
import tkinter as tk
from tkinter import simpledialog

# Function to print the itinerary starting from a given source `src`
def print_itinerary(dictionary, src):
    dest = dictionary.get(src)
    if not dest:
        return

    result_text.insert(tk.END, src + ' —> ' + dest + '\n')  # Insert text into the Text widget
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
            result_text.delete(1.0, tk.END)  # Clear previous content in Text widget
            print_itinerary(tickets, k)
            return

def main():
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Itinerary")

    # Create a Text widget to display the result
    global result_text
    result_text = tk.Text(window, height=10, width=40)
    result_text.pack()

    # Ask the user how many tickets they want to enter
    num_tickets = simpledialog.askinteger("Número de Tickets", "¿Cuántos tickets deseas ingresar?")

    if num_tickets is None:
        return  # User canceled input

    tickets = {}  # Initialize an empty dictionary to store tickets

    # Input tickets from the user
    for i in range(num_tickets):
        departure = simpledialog.askstring(f"Ticket #{i + 1}", "Ingresa la estación de salida:")
        arrival = simpledialog.askstring(f"Ticket #{i + 1}", "Ingresa la estación de llegada:")

        if departure is not None and arrival is not None:
            tickets[departure] = arrival

    # Find and print the itinerary
    findItinerary(tickets)

    # Start the Tkinter main loop
    window.mainloop()

if __name__ == '__main__':
    main()

# To test the functions created in lab_04.1
# Author: Joanna Kelly


from lab_04_1_requests import readbooks, readbook, createbook, updatebook, deletebook

def average_book_price():
    books = readbooks()  # Get all books from the server

    if not books:       # Check if books list is empty
        print("No books found!")
        return None
    
    #Extract all prices and compute the average
    prices = [book["price"] for book in books if "price" in book] # List of prices
    if not prices:
        print("No valid prices found!")
        return None
    
    avg_price = sum(prices) / len(prices) # Calculate the average
    return avg_price

if __name__ == "__main__":
    avg = average_book_price()
    if avg is not None:
        print(f"The average book price is {avg:.2f}")
import grpc
from client.inventory_client import InventoryServiceClient

# input is list of isbn and returns titles for books found for particular isbn
def get_book_titles(client: InventoryServiceClient, isbn_list):
    titles = []

    # traverse the list of isbn list
    for isbn in isbn_list:
        try:
            print("Fetching book details")
            # fetch book details
            book_details = client.get_book_details(isbn)
            print("Fetched book details")
            # append only if book details are found
            if (book_details.title != ''):
                titles.append(book_details.title)
        except:
            print("Failed to fetch book details")

    return titles

if __name__ == '__main__':
    # set up server and port details
    localhost = 'localhost'
    port = "50051"
    inventory_service_client = InventoryServiceClient(localhost, port)

    # call function by passing values
    titles = get_book_titles(inventory_service_client, ['abc101', 'abc102'])

    print(titles)

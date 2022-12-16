from inventory_client import InventoryClient


# This function takes a list of ISBNs and returns the corresponding book titles
# It makes a call to the GetBook RPC for every ISBN
def get_book_titles(isbn_list: [str], client: InventoryClient):
    titles = []
    for isbn in isbn_list:
        book = client.get_book(isbn)
        if book:
            titles.append(book.title)

    return titles


if __name__ == '__main__':
    inventory_client = InventoryClient('localhost', '50051')
    titles = get_book_titles(['1900023189', '8193805013'], inventory_client)

    print(titles)

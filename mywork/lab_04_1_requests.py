# Lab 04.1: requests
# Write a module to interact with the API:
# http://andrewbeatty1.pythonanywhere.com/books

import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    response = requests.get(url)
    return response.json()


def readbook(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createbook(book):
    response = requests.post(url, json=book)
    return response.json()

def updatebook(id, bookdiff):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=bookdiff)
    return response.json()

def deletebook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()


if __name__ == "__main__":
    book = {
        'author':"test",
        'title':"test title",
        'price': 123
    }

    bookdiff = {
        'price': 1000000
    }
    #print(readbooks())
    #print(readbook(1420))
    #print(createbook(book))
    #print(updatebook(1420, bookdiff))
    #print(deletebook(1553))


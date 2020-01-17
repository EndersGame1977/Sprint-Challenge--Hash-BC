#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    #   Insert source and destination from tickets into hashtable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    #   Retrieve ticket from hashtable that has the key of "NONE"
    #   Set that ticket destination value to the first position in the route.
    route[0] = hash_table_retrieve(hashtable, "NONE")

    #   Start at index 1 of route.
    #   Pass the destination of the previous ticket as the source of the next ticket in the hash_table_retrieve function
    #   Assign the retrieved destination value to the route list.
    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route

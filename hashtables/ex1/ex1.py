#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    #   Need at least two weights to compare
    if length <= 1:
        return None

    #   The weight amount needs to be set as a key and the index of it as the value in a hashtable.
    #   The hash_table_insert function calls for a hashtable, key, and value.
    #   Loop over the weights list to place each weight as a key and corosponding index as a value to that key in a hashtable.
    for weight in range(length):
        hash_table_insert(ht, weights[weight], weight)

    #   Looking for the weight in the hashtable that when added to the weight in the weight list would equal the limit.
    #   Loop over the weight list and subtract that weight from the limit to get the weight needed that would sum to the limit.
    #   Pass that desired weight to the hash_table_retrieve function
    #   If the desired weight is in hashtable. Return that weigth and the current weight.
    for current_weight in range(length):
        desired_weight = limit - weights[current_weight]
        if hash_table_retrieve(ht, desired_weight) is not None:
            desired_weight = hash_table_retrieve(ht, desired_weight)
            return(desired_weight, current_weight)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# NO IMPORTS!

##################################################
##  Problem 1
##################################################
""" Set of all simple paths from start_node to end_node in the graph """



def all_simple_paths(graph, start, target):

    return helper(target, [start], [start], graph, [])


def helper(target, path, visited, graph, answer):
    last = path[-1]
    if last != target:
        for neighbor in graph[last]:
            if neighbor not in visited:
                visited.append(neighbor)
                path.append(neighbor)
                helper(target, path, visited, graph, answer)
                visited.remove(neighbor)
                path.pop(len(path)-1)
    else:
        answer.append(tuple(path))

    return set(answer)


##################################################
##  Problem 2
##################################################

class Item:
    def __init__(self, owner, price):
        self.owner = owner
        self.price = price

    def __repr__(self):
        return "<" + self.__class__.__name__ + ", " + str(self.owner) + ", " + str(self.price) + ">"

    def is_a_kind_of(self, other):
        return isinstance(self, type(other))


class Vehicle(Item): pass
class Sedan(Vehicle): pass
class Truck(Vehicle): pass
class SUV(Vehicle): pass
class F150(Truck): pass
class Ram(Truck): pass


class Market:
    def offer_to_sell(self, item):
        """
        Behavior: the "best" current sell match is found between the given
        item, and any want-to-buy items currently in the market. By "best sell
        match", we mean:

          (1) the for-sale item must (for sure) be a kind of item the buyer is
              willing to buy.

          (2) the want-to-buy item with the highest willing-to-pay price is
              found. If more than one matching want-to-buy item with the same
              highest willing-to-pay price is found, any such match can be
              used.  That highest willing-to-pay price is the price the seller
              will get, even if it is higher than the price the seller was
              willing to sell for.

        If there is a matching want-to-buy item, ownership of the for-sale item
        should be transferred to the buyer (i.e., the owner of the for-sale
        item should be set to the buyer, and the price of the for-sale item
        should be set to the price actually paid by the buyer for the item).
        The sold item should be returned as the result of offer_to_sell, and
        taken off the market.

        If there is no matching want-to-buy item, None should be returned, and
        the want-to-sell item should be remembered for future possible matches
        later, as new want-to-buy items are submitted to the market.
        """
        raise NotImplementedError

    def offer_to_buy(self, item):
        """
        Behavior: the "best" current purchase match is found between the given
        item, and any items currently listed for sale in the market. By "best
        buy match", we mean:

          (1) the for-sale item must (for sure) be a kind of item the buyer is
              willing to buy.

          (2) the cheapest for-sale matching item is found. If more than one
              matching for-sale item with the same lowest sell price is found,
              any such matching for-sale item can be returned. That lowest
              for-sale price is the price the buyer will pay, even if it is
              lower than the price the buyer was willing to pay.

        If there is a matching for-sale item, ownership of that item should be
        transferred to the buyer (i.e., the owner of the for-sale item should
        be set to the buyer, and the price of the for-sale item should be set
        to the price actually paid by the buyer for the item). The sold item
        should be returned (and taken off the market), and the buyer is
        understood to no longer be seeking to buy another of the item (unless
        they again later register their desire with another offer_to_buy
        submission).

        If there is no matching for-sale item, None should be returned, and the
        offer_to_buy item should be remembered for future possible matches
        later, as new items for sale are submitted to the market.
        """
        raise NotImplementedError


##################################################
##  Problem 3
##################################################

allwords = set(open('words2.txt').read().splitlines())

def word_squares(top):
    """ Return (top, right, bottom, left) words """

    left_word = []
    right_word = []
    right_len_words = set()
    for i in allwords:
        if len(i) == len(top):
            right_len_words.add(i)
    for word in right_len_words:
        if word[0] == top[0]:
            left_word.append(word)

        if word[0] == top[-1]:
            right_word.append(word)

    for word in right_len_words:
        for left in left_word:
            for right in right_word:
                if word[0] == left[-1] and word[-1] == right[-1]:
                    if left != top and left != right and left != word:
                        if right != top and right != word:
                            if top != word:
                                yield (top, right, word, left)


class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.items_count = len(collection)
        self.items = [self.collection[i:i + self.items_per_page]
                      for i in range(0, self.items_count, self.items_per_page)]

    def item_count(self):
        return self.items_count

    def page_count(self):
        return len(self.items)

    def page_item_count(self, page_index):
        try:
            return len(self.items[page_index])
        except:
            return -1

    def page_index(self, item_index):
        if item_index < 0:
            return -1
        try:
            for i, j in enumerate(self.items):
                if self.collection[item_index] in j:
                    return i
            return -1
        except:
            return -1


collection = range(1, 25)
helper = PaginationHelper(collection, 10)

print(helper)
print(helper.collection)
print(helper.items_per_page)
print(helper.items_count)
print(helper.items)

print(helper.page_count(), 3)
print(helper.page_index(23), 2)
print(helper.item_count(), 24)

def smallest_doll_size(largest_doll):
    if largest_doll():
        return smallest_doll_size(largest_doll())
    return largest_doll.size


"""
test.describe("Example test cases")

test.assert_equals(smallest_doll_size(test_doll1), test_doll1Solution)
test.assert_equals(smallest_doll_size(test_doll2), test_doll2Solution)

"""
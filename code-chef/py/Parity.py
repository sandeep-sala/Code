
def is_cocolate_divided(n):
    return 'Yes' if n%2 == 0 else 'No'


if __name__ == "__main__":
    for __ in range(  int(input()) ):
        n = int(input())
        print(is_cocolate_divided(n))
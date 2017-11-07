## https://www.hackerrank.com/challenges/designer-pdf-viewer/problem


def getTotalArea(heights, chars):
    list_indexes = list(map(lambda c : ord(c) - ord('a'), chars))
    max_height = max(list(map(lambda i : int(heights[i]), list_indexes)))
    return max_height * len(chars)


def main():
    heights = list(map(int, input().strip().split(' ')))
    chars = list(input().strip())
    print(getTotalArea(heights, chars))


main()

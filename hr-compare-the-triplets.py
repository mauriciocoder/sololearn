## https://www.hackerrank.com/challenges/compare-the-triplets/problem


def compare(a_scores, b_scores):
    a_scores = list(map(int, a_scores))
    b_scores = list(map(int, b_scores))
    a_result = 0
    b_result = 0
    for i in range(len(a_scores)):
        ## print('comparing a = {} comparing b = {}'.format(a_scores[i], b_scores[i]))
        if a_scores[i] > b_scores[i]:
            a_result += 1
        elif a_scores[i] < b_scores[i]:
            b_result += 1
    return [a_result, b_result]


def main():
    a_scores = input().strip().split(' ')
    b_scores = input().strip().split(' ')
    result = compare(a_scores, b_scores)
    print(result[0], result[1])


main()

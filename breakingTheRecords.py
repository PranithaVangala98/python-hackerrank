def breakingTheRecord(scores):
    n = len(scores)
    max = 0
    min = 0
    maximum = scores[0]
    minimum = scores[0]
    for i in range(1,n):
        if scores[i] > maximum:
            maximum = scores[i]
            max += 1
        elif scores[i] < minimum:
            minimum = scores[i]
            min += 1
    output = [max,min]
    return output

scores = [12,24,10,24,32]
print(breakingTheRecord(scores))

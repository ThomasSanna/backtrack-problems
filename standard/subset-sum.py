def subsetSum(listSet, sumGoal, log=[]):
    results = []

    if sumGoal in listSet:
        results.append(log)

    if len(listSet) <= 1:
        return results

    for i in range(len(listSet)):
        for j in range(i + 1, len(listSet)):
            num1 = listSet[i]
            num2 = listSet[j]
            newListSet = listSet[:i] + listSet[i + 1 : j] + listSet[j + 1 :]
            newListSet = [num1 + num2] + newListSet
            results.extend(subsetSum(newListSet, sumGoal, log + [num1, num2]))

    return results


print(subsetSum([1, 2, 1], 3))
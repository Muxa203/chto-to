def split(lst):
    lst.sort()
    start = 0
    end = len(lst) - 1
    if lst[end] == 0:
        return end
    if lst[start] == 1:
        return -1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == 1:
            end = mid - 1
        elif lst[mid] == 0 and lst[mid + 1] == 1:
            return mid + 1
        else:
            start = mid + 1
    return -1

roster = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
product = split(roster)
print("Место разделения: Индекс равен", product)

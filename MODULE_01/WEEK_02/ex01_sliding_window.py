def sliding_window(num_list, k):
    if len(num_list) < 1:
        print("The length of the list must be greater or equal than 1")
        return []

    if k < 1:
        print("k must be equal or greater than 1")
        return []

    if k == 1:
        return num_list

    output = []
    start = 0
    end = start + k
    while True:
        output.append(max(num_list[start:end]))
        start += 1
        end = start + k
        if start == len(num_list) - k + 1:
            break

    return output

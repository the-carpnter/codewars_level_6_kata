def longest_sequence(arr, elem):
    try:
        x = ''.join(str(i) if i==elem else ' ' for i in arr).split()
        return max(len(i) for i in x)//len(str(elem))
    except:
        return 0

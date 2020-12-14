def longest_palindrome(s):
    s = ''.join(map(str.lower, filter(str.isalnum, s)))
    sum = 0
    has_odd = False
    k = {i:s.count(i) for i in s}
    for cnt in k.values():
        if cnt == 1:
            has_odd = True
        if cnt >= 2:
            if cnt % 2 == 0:
                sum += cnt
            else:
                sum += cnt // 2 * 2
                has_odd = True
    return sum+1 if has_odd else sum

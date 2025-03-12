def add(s):
    # Case 1: Empty string
    if not s:
        return 0
    nums = s.replace('\n', ',')
    nums = nums.split(',')

    suma = 0
    for num in nums:
        if num == '':
            return -1
        elif int(num) < 0:
            return -1
        else:
            suma = suma + int(num)

    return suma
    # nums = [int(num) for num in nums]

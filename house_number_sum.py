def house_numbers_sum(inp):
    return 0 if inp[0]==0 else inp[0] + house_numbers_sum(inp[1:])

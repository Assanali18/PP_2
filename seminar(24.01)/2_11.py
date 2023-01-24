col_1 = int(input())
li_1 = int(input())
col_2 = int(input())
li_2 = int(input())
if (col_1 + 1 == col_2 or col_1 - 1 == col_2) and (li_1 + 2 == li_2 or li_1 - 2 == li_2) or ((li_1 + 1 == li_2 or li_1 - 1 == li_2) and 
(col_1 + 2 == col_2 or col_1 - 2 == col_2)):
    print ('YES')
else:
    print('NO')

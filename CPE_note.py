#大數運算
eval("string type")
# print(eval('111+111')) => 222
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ASCII轉碼
ord("string type")
#print(ord('A')) => 65
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
組合
from itertools import combinations
combinations(list or string type,int type)
#print(list(combinations([1,2,3,4,5],3))) => [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
排列
from itertools import permutations
permutations(list or string type,int type)
#print(list(permutations([1,2,3,4,5],3))) =>[(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 2), (1, 3, 4), (1, 3, 5), (1, 4, 2), (1, 4, 3), (1, 4, 5), (1, 5, 2), (1, 5, 3), (1, 5, 4), (2, 1, 3), (2, 1, 4), (2, 1, 5), (2, 3, 1), (2, 3, 4), (2, 3, 5), (2, 4, 1), (2, 4, 3), (2, 4, 5), (2, 5, 1), (2, 5, 3), (2, 5, 4), (3, 1, 2), (3, 1, 4), (3, 1, 5), (3, 2, 1), (3, 2, 4), (3, 2, 5), (3, 4, 1), (3, 4, 2), (3, 4, 5), (3, 5, 1), (3, 5, 2), (3, 5, 4), (4, 1, 2), (4, 1, 3), (4, 1, 5), (4, 2, 1), (4, 2, 3), (4, 2, 5), (4, 3, 1), (4, 3, 2), (4, 3, 5), (4, 5, 1), (4, 5, 2), (4, 5, 3), (5, 1, 2), (5, 1, 3), (5, 1, 4), (5, 2, 1), (5, 2, 3), (5, 2, 4), (5, 3, 1), (5, 3, 2), (5, 3, 4), (5, 4, 1), (5, 4, 2), (5, 4, 3)]
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#2進位轉換
int(str or 進制函數 type,int type) ## int type 可為所想轉換的進制
#print(bin(6)) => 0b110
#print(int(bin(6),2)) => 6
#print(int('110',2))
#8進位轉換
#print(oct(20)) => 0o24
#print(int(oct(20),8)) => 20
#16進位轉換
#print(hex(20)) => 0x14
#print(int(hex(20),16)) => 20


'''趨勢線上測驗 -- 第二題 '''
# def solution(A):
#     if not A or len(A) <= 2:
#         return 0
    
#     total_income = 0
#     has_product = True
#     if A[0] > A[1]:
#         total_income += A[0]
#         has_product = False

#     for i in range(1, len(A)):    
#         print(total_income)
#         if not has_product:
#             buy_price = A[i]
#             has_product = True
#         else:
#             if A[i] > A[i-1] and A[i] > A[i+1]:
#                 total_income += A[i] - buy_price
#                 print('t:', total_income)
#                 has_product = False
#     return total_income
  
# print(solution([4,1,2,3]))

def solution(A):
    total_income = 0
    if A[0] > A[1]:
        total_income += A[0]

    for i in range(1, len(A)):
        if A[i] > A[i - 1]:  # 只在价格上升时计算收益
            total_income += A[i] - A[i - 1]
            total_income %= 10**9  # 取模保留最后9位
    return total_income

print(solution([1000000000, 1, 2, 1000000000, 1, 1000000000]))

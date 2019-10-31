

target_value = [0,1,8,27,64,125,216,343,512,729]

result = []

for num in range(100,1000):
    temp_sum = 0
    temp_num = num
    for index in range(3):
        temp_value = temp_num % 10
        temp_num //= 10
        temp_sum += target_value[temp_value]
    
    if temp_sum == num:
        result.append(num)

print("the daffodil number:",result)
        
    
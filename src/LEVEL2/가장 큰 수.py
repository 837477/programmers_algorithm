def solution(numbers):
    numbers = [str(i) for i in numbers]
    temp = []
    for num in numbers:
        temp_list = [num, num * 10]
        temp.append(temp_list)
    temp.sort(key=lambda x:x[1],reverse=True)
    
    result = [i[0] for i in temp]
    result = '0' if int(''.join(result)) == 0 else ''.join(result)
    return result

if __name__ == "__main__":
    print(solution([6, 10, 2]))
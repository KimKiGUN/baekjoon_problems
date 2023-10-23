def solution(nums):
    pocket = []
    answer = 0
    for item in nums:
        if item not in pocket:
            pocket.append(item)
            answer += 1
            if answer >= len(nums)/2:
                break
        else:
            continue
    
    return answer
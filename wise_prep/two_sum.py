def two_sum(nums: list[int], target: int) -> list[int]:
    hash_map = {}
    
    for i, num in enumerate(nums):
        compliment = target - num
        
        if compliment in hash_map:
            return [hash_map[compliment], i]
        
        hash_map[num] = i
        
    return []

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
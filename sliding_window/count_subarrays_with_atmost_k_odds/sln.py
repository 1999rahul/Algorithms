def is_odd(n):
    return n % 2 != 0

# Count the subarrays with atmost K odd numbers
# The idea is to restict the window to only contain at most k odd number, 
# if its goes more than k, shrink the window size to keep the odd numbers in the range
def subarrays_with_atmost_k_odds(arr, k):
    current_odd_count, odd_subarrays_count, left = 0, 0, 0

    for right, element in enumerate(arr):
        if is_odd(element): 
            current_odd_count += 1
        
        # Keep the count of odd numbers within range for current window
        while current_odd_count > k:
            if is_odd(arr[left]):
                current_odd_count -= 1
            left += 1

        # Count the subarrays
        odd_subarrays_count += (right - left + 1)
    
    return odd_subarrays_count

arr = [2, 2, 5, 6, 9, 2, 11]
k = 2

# Count of subarrays with atmost K odd numbers
print(subarrays_with_atmost_k_odds(arr, k))

# Trick Question
# Count of subarrays with exact K odd numbers = Count of subarrays with atmost K odd numbers - Count of subarrays with atmost K-1 odd numbers
print(subarrays_with_atmost_k_odds(arr, k)- subarrays_with_atmost_k_odds(arr, k-1))

# SUBMIT LINKS
# https://www.geeksforgeeks.org/problems/count-subarray-with-k-odds/1
# https://leetcode.com/problems/count-number-of-nice-subarrays/
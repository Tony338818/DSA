"""
Three types of problems in backtracking:
1. Decision Problem - Search for a feasible solution
2. Optimization Problem - Search for the best solution
3. Enumeration Problem - Find all feasible solutions.
"""

"""
def backtrack(path, choices):

    if goal_reached:
        save_answer(path)
        return

    for choice in choices:

        # 1. choose
        path.append(choice)

        # 2. explore
        backtrack(path, new_choices)

        # 3. undo
        path.pop()  
"""


def backtrack(i, path):

    if i == len(nums):
        print(path)
        return

    # TAKE
    path.append(nums[i])
    backtrack(i + 1, path)

    # BACKTRACK
    path.pop()

    # SKIP
    backtrack(i + 1, path)


nums = [1, 2, 3]
backtrack(0, [])   
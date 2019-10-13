import numpy as np
import math as math

initial_state = np.array([[0, 1, 3], [8, 2, 6], [7, 4, 5]])

# Movements are associated with the list containing 0 indicating empty space
# one movement is within the row between next columns - Cost 1
# another movement is from the another row right next to it between columns - Cost 1.4

current_state = np.copy(initial_state)
puzzle_size = int(math.sqrt(current_state.size))


def findEmptyLocation(state):
    i = 0
    for rowValue in state:
        if 0 in rowValue:
            j = 0
            for columnValue in rowValue:
                if 0 == columnValue:
                    return i, j
                else:
                    pass
                j += 1
        else:
            pass
        i += 1


def get_adjacent_indices_withCost(i, j, m):
    adjacent_indices = {}
    if i > 0:
        adjacent_indices[(i - 1, j)] = 1
        # adjacent_indices.append(((i - 1, j), 1))
        if j > 0:
            adjacent_indices[(i - 1, j - 1)] = 1.4
            # adjacent_indices.append(((i - 1, j - 1), 1.4))
        if j + 1 < m:
            adjacent_indices[(i - 1, j + 1)] = 1.4
            # adjacent_indices.append(((i - 1, j + 1), 1.4))
    if i + 1 < m:
        adjacent_indices[(i + 1, j)] = 1
        # adjacent_indices.append(((i + 1, j), 1))
        if j > 0:
            adjacent_indices[(i + 1, j - 1)] = 1.4
            # adjacent_indices.append(((i + 1, j - 1), 1.4))
        if j + 1 < m:
            adjacent_indices[(i + 1, j + 1)] = 1.4
            # adjacent_indices.append(((i + 1, j + 1), 1.4))
    if j > 0:
        adjacent_indices[(i, j - 1)] = 1
        # adjacent_indices.append(((i, j - 1), 1))
    if j + 1 < m:
        adjacent_indices[(i, j + 1)] = 1
        # adjacent_indices.append(((i, j + 1), 1))
    return adjacent_indices


def state_comparision(goal_state, current_state):
    count = 0
    possible_positions = []
    # for x, y in zip(goal_state, current_state):
    #     # print(x, y)
    #     for p, q in zip(x, y):
    #         # print(p, q)
    #         if p == q:
    #             # state = list(current_state)
    #             # print(state.index(q))
    #             count += 1
    goal_state = list(goal_state)
    current_state = list(current_state)
    for i in range(len(goal_state)):
        for j in range(len(goal_state)):
            if goal_state[i][j] == current_state[i][j]:
                possible_positions.append((i, j))
                count += 1
    return possible_positions,count


print("Initial State:")
print(initial_state)
goal_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
moves = 0
correct_positions_list = []
final_correct_position_list = []
refined_indices_list_with_cost = {}
total_cost = 0
past_current_states = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
while not np.array_equal(goal_state, current_state):
    min_cost = 0
    emptyLocation = findEmptyLocation(current_state)
    print("Empty Location -> "+str(emptyLocation))
    # position = determinePosition(emptyLocation, puzzle_size)
    adjacent_indices_with_cost = get_adjacent_indices_withCost(emptyLocation[0], emptyLocation[1], puzzle_size)
    # print(adjacent_indices_with_cost)
    if final_correct_position_list.__len__() == 0:
        refined_indices_list_with_cost = adjacent_indices_with_cost
    else:
        for i in adjacent_indices_with_cost:
            if i in final_correct_position_list:
                pass
            else:
                refined_indices_list_with_cost[i] = adjacent_indices_with_cost[i]
    max_correct_positions = 0
    efficient_state = None
    prev_state_cost = 100
    for i in refined_indices_list_with_cost:
        cost = refined_indices_list_with_cost[i]
        temp = current_state[i[0], i[1]]
        current_state[i[0], i[1]] = current_state[emptyLocation[0], emptyLocation[1]]
        current_state[emptyLocation[0], emptyLocation[1]] = temp
        if np.array_equal(past_current_states, current_state):
            break
        # check = a(item in past_current_states for item in current_state)
        # if check is True:
        #     break
        # compare the current_state and goal_state matrices
        position_information = state_comparision(goal_state, current_state)
        correct_positions = position_information[1]
        correct_positions_list = position_information[0]
        # print("correct positions: "+str(correct_positions))
        # print(correct_positions_list)
        if correct_positions >= max_correct_positions:
            if cost <= prev_state_cost:
                max_correct_positions = correct_positions
                final_correct_position_list = correct_positions_list
                prev_state_cost = cost
                min_cost = cost
                efficient_state = np.copy(current_state)
                temp_state = np.copy(efficient_state)
        current_state = np.copy(initial_state)
        # print(current_state[i[0], i[1]])
    print("Efficient State: ")
    print(efficient_state)
    moves += 1
    refined_indices_list_with_cost = {}
    past_current_states = np.copy(initial_state)
    initial_state = np.copy(temp_state)
    current_state = np.copy(efficient_state)
    total_cost += min_cost
print("Cost of Traversal is: "+str(total_cost))
print("Goal State Reached in "+str(moves)+" moves")


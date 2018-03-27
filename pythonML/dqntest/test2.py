# https://zhuanlan.zhihu.com/p/26401217
# here is a Q_learning method for a 2*2 maze, where state 1 is the start point,
# state 2 is on the right side of state 1
# state 3 is bellow state 1 and is a trap
# state 4 is on the right side of state 3 and is a treasure
import numpy as np
import random
import matplotlib.pyplot as plt
# the discount factor
gamma = 0
# the rows are the states, 0/1/2/3 rows of reward matrix and q_matrix respectively refer to real state 1/2/3/4
# the columns are the actions, refer to (U, D, L, R, N) where N means keeping still
reward = np.array([[0,-10, 0, -1, -1],
                  [0, 10, -1, 0, -1],
                  [-1, 0, 0, 10, -1],
                  [-1, 0, -10, 0, 10]])
# 1. the setup of q table, all 0
q_matrix = np.zeros((4,5))
# about the transition_matrix, it means to transit from one state to another state, -1 represents invalid transitions.
# however, it remains questionable about the last column, should it be [0,1,2,3] ?
transition_matrix = np.array([[-1, 2, -1, 1, 0],
                              [-1, 3, 0, -1, 1],
                              [0, -1, -1, 3, 2],
                              [1, -1, 2, -1, 3]])
# for valid_actions, it encoded up as 0, down as 1, left as 2, right as 3, no action as 4
valid_actions = np.array([[1, 3, 4],
                          [1, 2, 4],
                          [0, 3, 4],
                          [0, 2, 4]])
for i in range (1000): # 1000 episodes, why using 1000?
    # 2. to choose the the start state
    start_state = 0
    current_state = start_state
    n = 0
    while current_state != 3:
        # 3. to choose the action based on current state
        action = random.choice(valid_actions[current_state])
        # 4. to move to the next state
        next_state = transition_matrix[current_state][action]
        # 5. to choose the next action based on the max rewards
        future_rewards=[]
        for next_action in valid_actions[next_state]:
            future_rewards.append(q_matrix[next_state,next_action])
        # 6. to update the q_table with Bellman Equation
        q_state = reward[current_state][action] + gamma * max(future_rewards)
        q_matrix[current_state][action] = q_state
        print (q_matrix)
        # 7. recycle
        current_state = next_state
        n = n + 1
        print ('the number:', n)
        if current_state == 3:
            print ("find the treasure!")
print ('final q_matrix :')
print (q_matrix)
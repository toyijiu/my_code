import numpy as np
import pandas as pd
import time

N_STATE = 6
ACTIONS = ['left','right']
GREEDY = 0.9 #greedy
ALPHA = 0.1 #learning rate
GAMMA = 0.9 #reward rating
MAX_EPISODES = 13
FRESH_TIME = 0.2

def  build_q_table(n_states,actions):
    table = pd.DataFrame(
        np.zeros((n_states,len(actions))),
        columns = actions,
    )
    return table


def choice_action(cur_state,q_table):
    actions = q_table.iloc[cur_state,:]
    #greedy choice
    if(np.random.uniform() > GREEDY or actions.all() == 0):
        action = np.random.choice(ACTIONS)
    else:
        action = actions.argmax()

    return action

def get_env_feedback(cur_state,action,q_table):
    if action == 'right':
        #reach the target
        if cur_state == N_STATE-2:
            next_state = 'terminal'
            reward = 1
        else:
            next_state = cur_state+1
            reward = 0
    else:
        reward = 0
        if cur_state == 0:
            next_state = cur_state
        else:
            next_state = cur_state - 1
    
    return next_state,reward


def update_env(cur_state,episode,step_times):
    env_list = ['-']*(N_STATE-1) + ['T']
    if cur_state == 'terminal':
        result = 'episode %s, total steps %s' %(episode+1,step_times)
        print("\r{}".format(result),end='')
        time.sleep(1)
        print("\r                                                    ",end='')
    else:
        env_list[cur_state] = 'o'
        result = ''.join(env_list)
        print("\r{}".format(result),end='')
        time.sleep(FRESH_TIME)


def rl():
    q_table = build_q_table(N_STATE,ACTIONS)
    for episode in range(MAX_EPISODES):
        print(q_table)
        cur_state = 0
        step_times = 0
        is_terminal = False
        update_env(cur_state,episode,step_times)

        while not is_terminal:
            action = choice_action(cur_state,q_table)
            next_state,reward = get_env_feedback(cur_state,action,q_table)

            #predict value
            q_predict = q_table.loc[cur_state,action]
            if next_state == 'terminal':
                is_terminal = True
                q_target = reward
            else:
                q_target = reward + GAMMA*q_table.iloc[next_state,:].max()
            
            q_table.loc[cur_state,action] += ALPHA*(q_target-q_predict)
            cur_state = next_state
            step_times += 1
            update_env(cur_state,episode,step_times)
    return q_table


if __name__ == '__main__':
    q_table = rl()
    print(q_table)


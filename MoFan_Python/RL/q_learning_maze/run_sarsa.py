from maze_env import Maze
from RL_brain import SarsaTable

def update():
    #learn 100 episode
    for episode in range(100):
        observation = env.reset()

        action = RL.choose_action(str(observation))
        while True:
            #update env
            env.render()

            #get the env's feedback
            observation_,reward,done = env.step(action)

            #make action
            action_ = RL.choose_action(str(observation_))

            #learn with the list (state,action,reward,state_)
            RL.learn(str(observation),action,reward,str(observation_),action_)

            observation = observation_
            action = action_

            #the end status
            if done:
                break
    
     #game over, close the game window
    print('Game Over~')
    env.destroy()


if __name__ == '__main__':
    env = Maze()
    RL = SarsaTable(actions = list(range(env.n_actions)))

    env.after(100,update)
    env.mainloop()
from maze_env import Maze
from RL_brain import QLearningTable

def update():
    #learn 100 episode
    for episode in range(100):
        observation = env.reset()

        while True:
            #update env
            env.render()

            #make action
            action = RL.choose_action(str(observation))

            #get the env's feedback
            observation_,reward,done = env.step(action)

            #learn with the list (state,action,reward,state_)
            RL.learn(str(observation),action,reward,str(observation_))

            observation = observation_

            #the end status
            if done:
                break
    
     #game over, close the game window
    print('Game Over~')
    env.destroy()


if __name__ == '__main__':
    env = Maze()
    RL = QLearningTable(actions = list(range(env.n_actions)))

    env.after(100,update)
    env.mainloop()
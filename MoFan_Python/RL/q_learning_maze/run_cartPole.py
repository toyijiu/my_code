import gym
from DQN_brain import DeepQNetwork

env = gym.make('CartPole-v0')

env = env.unwrapped

print(env.action_space)
print(env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)

RL = DeepQNetwork(n_actions = env.action_space.n,
                                            n_features = env.observation_space.shape[0],
                                            learning_rate=0.01,e_greedy=0.9,
                                            replace_target_iter=100,memory_size=2000,
                                            e_greedy_increment=0.0008)

total_steps = 0

for i_episode in range(100):
    observation = env.reset()
    ep_r = 0

    while True:
        env.render()
        action = RL.choose_action(observation)
        observation_,reward,done,info = env.step(action)

        x,x_dot,theta,theta_dot = observation_
        r1 = (env.x_threshold-abs(x))/env.x_threshold - 0.8
        r2 = (env.theta_threshold_radians-abs(theta))/env.theta_threshold_radians-0.5
        reward = r1+r2

        #store memory
        RL.store_transition(observation,action,reward,observation_)

        if total_steps > 1000:
            RL.learn()
        
        ep_r += reward
        if done:
            print('episode:%d,ep_r:%d,epsilon:%d' %(i_episode,round(ep_r,2),round(RL.epsilon,2)))
            break

        observation = observation_
        total_steps += 1

RL.plot_cost()
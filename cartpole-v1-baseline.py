import gym
import time
from math import pow, fabs


def sgn(x):
    return (-1 if x<0 else 1)

def action1(observation):
    # x = sgn a (1000 a)² + sgn p (100 p)² + sgn v (100 v)²
    cart_position, cart_velocity, pole_angle, pole_velocity = observation
    a = pow(1000 * fabs(pole_angle), 2) * sgn(pole_angle)
    b = pow(100 * fabs(cart_position), 2) * sgn(cart_position)
    c = pow(100 * fabs(pole_velocity), 2) * sgn(pole_velocity)
    return 0 if (a + b + c) < 0 else 1


env = gym.make('CartPole-v1')

for i_episode in range(20):
    observation = env.reset()
    print(observation)
    for t in range(500):
        env.render()
        observation, reward, done, info = env.step(action1(observation))
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
    time.sleep(1)

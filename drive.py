# Drive car stright

import gym
import numpy as np
import cv2

env = gym.make("CarRacing-v2", render_mode="human")  # 'rgb_array' for image-only
obs = env.reset()[0]

for _ in range(1000):
    env.render()
    # Simple action: [steering, gas, brake]
    action = np.array([0.0, 1.0, 0.0])  # go straight with gas
    obs, reward, done, truncated, info = env.step(action)

    if done or truncated:
        break

env.close()

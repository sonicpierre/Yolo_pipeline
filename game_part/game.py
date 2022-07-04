import gym
import time
from ale_py.roms import Breakout
from ale_py import ALEInterface

def create_env():
    ale = ALEInterface()
    ale.loadROM(Breakout)
    env = gym.make('ALE/Breakout-v5',
                    obs_type='rgb',                   # ram | rgb | grayscale
                    frameskip=4,                      # frame skip
                    mode=None,                        # game mode, see Machado et al. 2018
                    difficulty=None,                  # game difficulty, see Machado et al. 2018
                    repeat_action_probability=0.25,   # Sticky action probability
                    full_action_space=True,          # Use all actions
                    render_mode="human"                  # None | human | rgb_array
    )
    env.reset()
    return env
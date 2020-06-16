from typing import List
import random

class Environment:
    """We will define an environment that will give the agent random rewards 
        for a limited number of steps, regardless of the agent's actions.
    """
    def __init__(self):
        """
            In our case, the state is just a counter that limits the number of
            time steps that the agent is allowed to take to interact with the environment.
        """
        self.steps_left = 10
    
    def get_observation(self) -> List[float] :
        """
            The get_observation()method is supposed to return the current environment's 
            observation to the agent. It is usually implemented as some function of the
            internal state of the environment. In our example, the observation vector is always zero, 
            as the environment basically has no internal state.
        """
        return [0.0, 0.0, 0.0]
    
    def get_actions(self) -> List[int]:
        """
            The get_actions() method allows the agent to query the set of actions it can execute. 
            Normally, the set of actions that the agent can execute does not change over time, 
            but some actions can become impossible in different states (for example, not every 
            move is possible in any position of the tic-tac-toe game). In our simplistic example, 
            there are only two actions that the agent can carry out, which are encoded with the integers 0 and 1.
        """
        return [0, 1]

    def is_done(self) -> bool:
        return self.steps_left == 0

    def action(self, action: int) -> float:
        """
            It does two things – handles an agent's action and returns the reward for this action. 
            In our example, the reward is random and its action is discarded. Additionally, we update
            the count of steps and refuse to continue the episodes that are over.
        """
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -= 1
        return random.random()



class Agent:
    def __init__(self):
        """
            In the constructor, we initialize the counter that will keep the total reward accumulated
            by the agent during the episode.
        """
        self.total_reward = 0.0

    def step(self, env : Environment):
        """
            The step function accepts the environment instance as an argument and allows the agent to perform the following actions:
            • Observe the environment
            • Make a decision about the action to take based on the observations
            • Submit the action to the environment
            • Get the reward for the current step
        """
        current_obs = env.get_observation()
        actions = env.get_actions()
        reward = env.action(random.choice(actions))
        self.total_reward += reward



if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print("Total reward got: %0.4f" % agent.total_reward)


from pommerman import characters
from pommerman.constants import Action
from pommerman.agents import BaseAgent


class MyAgent(BaseAgent):
    """ Our version of the base agent. """

    def __init__(self, character=characters.Bomber):
        super().__init__(character)
        self.queue = []

    def act(self, obs, action_space):
        # Main event that is being called on every turn.
        if len(self.queue) == 0:
            self.queue.append(Action.Right)
            self.queue.append(Action.Down)
            self.queue.append(Action.Left)
            self.queue.append(Action.Up)
        return self.queue.pop()

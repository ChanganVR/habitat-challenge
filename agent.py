import argparse
import habitat
import random
import numpy
import os


class RandomAgent(habitat.Agent):
    def __init__(self, task_config: habitat.Config):
        self._POSSIBLE_ACTIONS = task_config.TASK.POSSIBLE_ACTIONS

    def reset(self):
        pass

    def act(self, observations):
        return {"action": numpy.random.choice(self._POSSIBLE_ACTIONS)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--evaluation", type=str, required=True, choices=["local", "remote"])
    args = parser.parse_args()

    config_paths = os.environ["CHALLENGE_CONFIG_FILE"]
    config = habitat.get_config(config_paths)
    agent = RandomAgent(task_config=config)

    if args.evaluation == "local":
        challenge = habitat.Challenge(eval_remote=False)
    else:
        challenge = habitat.Challenge(eval_remote=True)

    challenge.submit(agent)


if __name__ == "__main__":
    main()


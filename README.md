# Deep Reinforcement Learning Nanodegree - Project 1 
# Navigation 

This project contains my solution for the first project of the DRLND : https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893

In this project, we train a Banana collector that gets a +1 reward for collecting yellow bananas and -1 for the blue bananas. 

**This project implement a Value Based method called Deep Q-Networks**
     
<img src="trained_agent.gif" 
     alt="Trained Agent" />
<p align="center"> My Banana Collector at work ;)  </p>

## File organisation 
* **Report.md** : Describe the used algorithm and the possible future works. 
* **navigation.ipynd** : Train code and running the agent. 
* **agent.py** : defines the agent and the learning functions 
* **model.py** : defines the neural network that aim to predict the Q Action-Value function. 
* **dqn_checkpoint.pth** : Saved model 

## Environement details 

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction.

Given this information, the agent has to learn how to best select actions. Four discrete actions are available, corresponding to:
* Move forward.
* Move backward.
* Turn left.
* Turn right.

The task is episodic (Well-defined starting and ending point). In order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes.

## Installation and usage

* Follow the instructions in the [original Udacity repository](https://github.com/udacity/deep-reinforcement-learning#dependencies) to install the different dependencies. 

* Download the Banana Unity Environment suitable for your OS 

* Clone this repo 

* Train the agent by executing the jupyter notebook : navigation.ipynb

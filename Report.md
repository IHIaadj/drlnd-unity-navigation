# Report 
## Used Framework 
In this project, we are using PyTorch framework. [PyTorch](https://pytorch.org/) is an optimized tensor library for deep learning using GPUs and CPUs.
It offers several layers and filters to implement all deep learning models. 

## Learning Algorithm 
In this first shot solution, we are using [Vanilla Deep Q Learning](https://arxiv.org/pdf/1312.5602.pdf). As input to the neural network, the vector of state is used. Thus, no need for convolution layers we just use a fully connected neural network. 
A fully connected neural network with 3 layers is implemented : 
* Input : 37 (Size of the state) ---> Output : 128
* Input : 128 ---> Output : 64
* Input : 64  ---> Output :  4 (Action size)

DQN algorithm's parameters : 
* Maximum steps per episode: 4000
* Starting epsilion: 1.0
* Ending epsilion: 0.01
* Epsilion decay rate: 0.999


## Results 
![](result.png) 
```
Episode 100	Average Score: 1.63

Episode 200	Average Score: 4.92

Episode 300	Average Score: 8.82

Episode 400	Average Score: 11.77

Episode 447	Average Score: 13.03

Environment solved in 347 episodes!	Average Score: 13.03
```

## Ideas for Future Work 
* Implement a Double Deep Q Network 
* Prioritized Experience Replay
* Dueling Deep Q Networks
* Complete the optional part to directly use the pixels using a convolutional network. 

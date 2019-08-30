import torch 
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):

    """This class defines the model used to create the agent 
       The model consists on 3 fully connected layer.
       The network maps the state to the action
    """

    def __init__(self, state_size, action_size, seed):
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, action_size)

    def forward(self, state):
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

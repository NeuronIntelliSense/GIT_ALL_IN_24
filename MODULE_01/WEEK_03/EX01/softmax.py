import torch
import torch.nn as nn
import math


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        if len(x) == 0:
            print("The list is empty.")
        elif len(x) == 1:
            return torch.Tensor([1])
        else:
            total_exp = 0
            list_exp = []
            for i in x:
                total_exp += math.exp(i)
                list_exp.append(math.exp(i))

            output = []
            for i in list_exp:
                output.append(i/total_exp)

            output = torch.Tensor(output)
            return output

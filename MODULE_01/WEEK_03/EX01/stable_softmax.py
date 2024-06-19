import torch
import torch.nn as nn
import math


class Softmax_stable(nn.Module):
    def __init__(self):
        super(Softmax_stable, self).__init__()

    def forward(self, x):
        if len(x) == 0:
            print("The list is empty.")
        elif len(x) == 1:
            return torch.Tensor([1])
        else:
            max_element = max(x)
            list_exp = []
            total_exp = 0
            for i in x:
                list_exp.append(math.exp(i - max_element))
                total_exp += math.exp(i - max_element)

            output = []
            for i in list_exp:
                output.append(i/total_exp)

            output = torch.Tensor(output)
            return output

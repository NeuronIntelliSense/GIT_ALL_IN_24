import torch
from softmax import Softmax
from stable_softmax import Softmax_stable

if __name__ == "__main__":
    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    print(softmax(data))
    stable_softmax = Softmax_stable()
    print(stable_softmax(data))
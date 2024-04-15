import torch
if torch.cuda.is_available():
    print("CUDA is avaiable")
else:
    print("CUDA isn't avaiable")
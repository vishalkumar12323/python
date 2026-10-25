import pandas
import numpy
import torch

print("---- Environment Check ----")
print(f"pandas version: {pandas.__version__}")
print(f"numpy version: {numpy.__version__}")
print(f"pytorch version: {torch.__version__}")
print(f"CUDA Available for AI/ML: {torch.cuda.is_available()}")
print("Environment successfully provisioned!")

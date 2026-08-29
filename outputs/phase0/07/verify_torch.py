import torch
import numpy, pandas, sklearn, matplotlib
import transformers, datasets

print(f"PyTorch {torch.__version__}, CUDA available: {torch.cuda.is_available()}")
x = torch.randn(3, 3) @ torch.randn(3, 3)
print(f"torch matmul ok: {tuple(x.shape)}")
print(f"numpy {numpy.__version__} | pandas {pandas.__version__} | sklearn {sklearn.__version__}")
print(f"transformers {transformers.__version__} | datasets {datasets.__version__}")
print("ALL CHECKS PASSED")

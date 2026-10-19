import torch
import cv2

print("PyTorch:", torch.__version__)
print("GPU可用:", torch.cuda.is_available())
print("OpenCV:", cv2.__version__)

x = torch.rand(3, 3).cuda()
print("\nGPU上的随机矩阵：")
print(x)

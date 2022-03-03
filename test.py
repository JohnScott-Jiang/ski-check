from operator import mod
from statistics import mode
import torch


import torch
import torchvision
from torch.autograd import Variable
from torchvision import transforms, models
import cv2

model = models.resnet152(num_classes=3)
model.load_state_dict(torch.load("output/params_50.pth"))
model.eval()
model.cuda()
img = cv2.imread('DS/0/03452.jpg')
img_tensor = transforms.ToTensor()(img)
img_tensor = img_tensor.unsqueeze(0)
prediction = model(Variable(img_tensor.cuda()))
pred = torch.max(prediction, 1)[1]
print(pred.item())
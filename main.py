import os.path

from torch.utils.data import Dataset
from PIL import Image
import cv2
#hihihi

imgp="train/COCO_train2014_000000000009.jpg"
img=Image.open(imgp)
img.show()
dir="/media/linxiao/Storage/udownload/"
labeldir="train"
os.path.join(dir,labeldir)

class Mydattaa(Dataset):

    def __init__(self, dir,lableDir):
        self.dir=dir

    def __getitem__(self, item):
        self.dir = dir


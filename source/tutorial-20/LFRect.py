from PIL import Image
from PIL.Image import open

class LFRect:
	def __init__(self,x,y,w,h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
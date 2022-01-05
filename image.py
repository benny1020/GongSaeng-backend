import os

print(len(os.listdir('./url')))

class image_mange():
    def __init__(self):
        self.count = len(os.listdir('./image/url'))

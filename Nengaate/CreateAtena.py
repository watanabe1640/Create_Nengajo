import pandas as pd
from PIL import Image,ImageDraw,ImageFont
font = ImageFont.truetype('ヒラギノ明朝 ProN.ttc', 24)
class Atena:
    postcode=None
    address1=None
    address2=None
    sei_name=None
    mei_name=None
    plane_img = Image.open("./img/muji.jpg")
    drawnImg = ImageDraw.Draw(plane_img)
    vertical_space = 30
    

    def __init__(
        self,
        postcode,
        address1,
        sei_name,
        mei_name,
        address2=None
    ):
        self.postcode=postcode
        self.address1=address1
        self.address2=address2
        self.sei_name=sei_name
        self.mei_name=mei_name

    def DrawPostcode(self):
        postcode_list = list(self.postcode)
        for i in range(0,3):
            self.drawnImg.text((215+32*i,60),postcode_list[i],"black",font=font)
        for i in range(3,7):
            self.drawnImg.text((316+32*(i-3),60),postcode_list[i],"black",font=font)

    def DrawName(self):
        sei_list = list(self.sei_name)
        mei_list = list(self.mei_name)
        for i in range(len(sei_list)):
            self.drawnImg.text((200,160+i*24),sei_list[i],"black",font=font)
        for i in range(len(sei_list)):
            self.drawnImg.text((200,(160+len(sei_list)*24)+20+24*i),mei_list[i],"black",font=font)
    def SaveImage(self):
        self.plane_img.save(f"./created_dir{self.mei_name}{self.sei_name}.jpg")
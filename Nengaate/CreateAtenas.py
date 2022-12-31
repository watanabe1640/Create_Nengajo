import pandas as pd
import CreateAtena
from PIL import Image,ImageDraw,ImageFont
font = ImageFont.truetype('ヒラギノ明朝 ProN.ttc', 24)
atena_df = pd.read_csv("address.csv")
atena_df.columns = ["index", "sei","mei", "address1","address2","postcode"]

def main(self):
  for i in len(atena_df.index):
    atena_ins = CreateAtena.Atena(
      sei_name=atena_df.sei[i],
      mei_name=atena_df.mei[i],
      postcode=atena_df.postcode[i],
      address1=atena_df.address1[i],
      address2=atena_df.address2[i]
    )
    atena_ins.DrawName()
    atena_ins.DrawPostcode()
    atena_ins.SaveImage()
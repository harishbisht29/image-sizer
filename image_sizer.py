from PIL import Image
from resizeimage import resizeimage
import os
import sys

from os import listdir
from os.path import isfile, join

class Image_Sizer:

    image_dims = {}

    def get_image_dims(self, template_folder):
        template_names = [f for f in listdir(template_folder) if isfile(join(template_folder, f))]
        
        for t in template_names:
            tf= os.path.join(template_folder, t)
            self.image_dims[os.path.splitext(t)[0]] = Image.open(tf).size

    def __init__(self, template_loc):
        self.get_image_dims(template_loc)


    def resize_image(self,input,tname):
        input_image = Image.open(input)
        
        twidth= self.image_dims[tname][0]
        theight= self.image_dims[tname][1]
        tratio= twidth/theight
        iwidth= input_image.size[0]
        iheight= input_image.size[1]
        if iwidth >= twidth and iheight >= theight:
            converted_image = resizeimage.resize_cover(input_image,[twidth,theight])
        else:
            converted_image = resizeimage.resize_cover(input_image,[iwidth,iwidth/tratio])
        return converted_image


if __name__ == "__main__":
	ifile_name= sys.argv[1]
	sizer= Image_Sizer('./templates')
	# print(sizer.image_dims)
	# cimage= sizer.resize_image(ifile_name,'blog_cover')
	# cimage.save('venv_image_output.jpg')
	print(sizer.image_dims)
	for name in sizer.image_dims:
		cimage= sizer.resize_image(ifile_name,name)
		cimage.save("{}_{}{}".format(os.path.splitext(ifile_name)[0],name,os.path.splitext(ifile_name)[1]))


  

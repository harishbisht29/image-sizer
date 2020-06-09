from PIL import Image
from resizeimage import resizeimage
import os
from os import listdir
from os.path import isfile, join

class Image_Sizer:

    image_dims = {}

    def get_image_dims(self, template_folder):
        template_names = [f for f in listdir(template_folder) if isfile(join(template_folder, f))]
        
        for t in template_names:
            tf= os.path.join(template_folder, t)
            self.image_dims[os.path.splitext(t)[0]] = Image.open(tf).size
        print(self.image_dims)
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
    sizer= Image_Sizer('./templates')
    # print(sizer.image_dims)
    cimage= sizer.resize_image('codethemall_logo.png','signs')
    cimage.save('codethemall_logo.png')
  

# template_name= 'blog_featured'
# template_ratio = image_templates[template_name][0]/image_templates[template_name][1]
# print("Template Ration",template_ratio)

# input_image = Image.open('./test_image.jpg')
# width = input_image.size[0]
# print(width)
# height = width/template_ratio
# print(height)
# converted_image = resizeimage.resize_cover(input_image,[width,height])
# converted_image.save('test-image-cover.jpeg', input_image.format)
# test_image = Image.open('./test_image.jpg')
# cover = resizeimage.resize_thumbnail(test_image, image_templates['blog_featured'])
# # cover.show()
# print(blog_featured.size)
# print(test_image.size)
# print(cover.size)

# cover.save('test-image-cover.jpeg', test_image.format)

# import PIL
# from PIL import Image

# mywidth = 300

# img = Image.open('someimage.jpg')
# wpercent = (mywidth/float(img.size[0]))
# hsize = int((float(img.size[1])*float(wpercent)))
# img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
# img.save('resized.jpg')

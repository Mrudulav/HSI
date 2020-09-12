#!/usr/bin/env python
# coding: utf-8

# In[1]:


from spectral import *


# In[ ]:


pip install opencv-python


# In[2]:


img = open_image('REFLECTANCE_2017-06-21_002.hdr')


# In[3]:


img


# In[4]:


import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
import cv2
import os


# In[34]:


# view = imshow(img,(5,5,5))
# view = imshow(img[150:400,100:430,])
# view = imshow(img,(0,203,0))
# view = imshow(img,(0,100,0))
# view = imshow(img,(0,0,203))
# view = imshow(img,(203,0,0))

# view = imshow(img,(203,0,0))


# view = imshow(img,(100,0,0))

# l1 = []
# l2 = []
# l3 = []
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             view = imshow(img,(i,j,k))
#             print(i,j,k)
# for i in range(512):
    
#     try:
#         view = imshow(img,(2,2,i))
#     except:
#         print(i)

            


# In[21]:


for i in range(0,203):

    gt = open_image('REFLECTANCE_2017-06-21_002.hdr').read_band(i)

    view = imshow(img, classes=gt)
    view.set_display_mode('overlay')
    view.class_alpha = 0.5
    from matplotlib import pyplot as plt
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5, 10.5)
#     fig.savefig('test.jpg', dpi=200)
    plt.savefig("images/"+str(i)+".jpg", dpi = 200)


# In[38]:


dir(view)


# In[8]:


pip install fpdf


# In[ ]:


from fpdf import FPDF
pdf = FPDF()
import glob
images = glob.glob("images/*.jpg")
# imagelist is the list with all image filenames
for image in images:
    pdf.add_page()
    pdf.image(image)
pdf.output("file.pdf", "F")


# In[23]:





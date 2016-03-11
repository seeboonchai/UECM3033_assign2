import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.linalg as sp

#loading image
img=mpimg.imread('camera.tiff')
img1=mpimg.imread('camera.tiff')
[r,g,b] = [img1[:,:,i] for i in range(3)]




U_red,sigma_red,V_red = sp.svd(r,False,True,False,True)
U_green,sigma_green,V_green = sp.svd(g,False,True,False,True)
U_blue,sigma_blue,V_blue = sp.svd(b,False,True,False,True)

#Sigma is convert from vector to  a diagonal matrix
sigma_red = np.diag(sigma_red)
sigma_green = np.diag(sigma_green)
sigma_blue = np.diag(sigma_blue)

# Compress the Lower resolution picture
sigma_RED = np.zeros_like(sigma_red)
sigma_GREEN = np.zeros_like(sigma_green)
sigma_BLUE = np.zeros_like(sigma_blue)

# make sure the first 30 none zero element are  Sigma
sigma_RED[0:30] = sigma_red[0:30]
sigma_GREEN[0:30] = sigma_green[0:30]
sigma_BLUE[0:30] = sigma_blue[0:30]

RED   = U_red.dot(sigma_RED).dot(V_red)
GREEN = U_green.dot(sigma_GREEN).dot(V_green)
BLUE  = U_blue.dot(sigma_BLUE).dot(V_blue)

img[:,:,0] = RED
img[:,:,1] = GREEN
img[:,:,2] = BLUE

figure = plt.figure(1)
ax1 = figure.add_subplot(2,2,1)
ax2 = figure.add_subplot(2,2,2)
ax3 = figure.add_subplot(2,2,3)
ax4 = figure.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(RED, cmap = 'Reds')
ax3.imshow(GREEN, cmap = 'Greens')
ax4.imshow(BLUE, cmap = 'Blues')
plt.suptitle('Lower Resolution, size=30')
plt.show()

# Compress - better resolution picture
sigma_RED = np.zeros_like(sigma_red)
sigma_GREEN = np.zeros_like(sigma_green)
sigma_BLUE = np.zeros_like(sigma_blue)

# keeping the first 200 none zero elements as Sigma
sigma_RED[0:200] = sigma_red[0:200]
sigma_GREEN[0:200] = sigma_green[0:200]
sigma_BLUE[0:200] = sigma_blue[0:200]

RED   = U_red.dot(sigma_RED).dot(V_red)
GREEN = U_green.dot(sigma_GREEN).dot(V_green)
BLUE  = U_blue.dot(sigma_BLUE).dot(V_blue)

img1[:,:,0] = RED
img1[:,:,1] = GREEN
img1[:,:,2] = BLUE

figure = plt.figure(2)
ax1 = figure.add_subplot(2,2,1)
ax2 = figure.add_subplot(2,2,2)
ax3 = figure.add_subplot(2,2,3)
ax4 = figure.add_subplot(2,2,4)
ax1.imshow(img1)
ax2.imshow(RED, cmap = 'Reds')
ax3.imshow(GREEN, cmap = 'Greens')
ax4.imshow(BLUE, cmap = 'Blues')
plt.suptitle('Higher Resolution, size=200')
plt.show()


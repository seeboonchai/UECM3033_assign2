import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#this is image file loading
img=mpimg.imread('camera.tiff')
[r,g,b] = [img[:,:,i] for i in range(3)]


fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()


#singular value decomposition
U_red, sigma_red, V_red = np.linalg.svd(r,full_matrices = True)
U_green, sigma_g, V_green = np.linalg.svd(g,full_matrices = True)
U_blue, sigma_b, V_blue = np.linalg.svd(b,full_matrices = True)
n_sigma = np.count_nonzero(sigma_red)
print("non zero element for sigma of r, g, b : ", n_sigma)
num_data, dim = r.shape

# Compress-Lower Resolution picture
#red image
sigma_red_30=np.zeros_like(sigma_red)
sigma_red_30[:30] = sigma_red[:30]
r_30 = np.matrix(U_red) * np.diag(sigma_red_30) * np.matrix(V_red[:num_data, :])

#green image
sigma_green_30=np.zeros_like(sigma_g)
sigma_green_30[:30] = sigma_g[:30]
g_30 = np.matrix(U_green) * np.diag(sigma_green_30) * np.matrix(V_green[:num_data, :])

#blue image
sigma_blue_30=np.zeros_like(sigma_b)
sigma_blue_30[:30] = sigma_b[:30]
b_30 = np.matrix(U_blue) * np.diag(sigma_blue_30) * np.matrix(V_blue[:num_data, :])

#compress  the imageinto color image
low_img = img
low_img[:,:,0] = r_30
low_img[:,:,1] = g_30
low_img[:,:,2] = b_30

#display red, green, blue image.
fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(r_30, cmap = 'Reds')
ax2.imshow(g_30, cmap = 'Greens')
ax3.imshow(b_30, cmap = 'Blues')
ax4.imshow(low_img)
fig = plt.gcf()
fig.set_size_inches(15,15)
plt.suptitle('Lower Resolution, size=30')
plt.show()

# Compress-Higher Resolution picture
#red image
sigma_red_200=np.zeros_like(sigma_red)
sigma_red_200[:200] = sigma_red[:200]
red_200 = np.matrix(U_red) * np.diag(sigma_red_200) * np.matrix(V_red[:num_data, :])

#green image
sigma_green_200=np.zeros_like(sigma_g)
sigma_green_200[:200] = sigma_g[:200]
green_200 = np.matrix(U_green) * np.diag(sigma_green_200) * np.matrix(V_green[:num_data, :])

#blue image
sigma_blue_200=np.zeros_like(sigma_b)
sigma_blue_200[:200] = sigma_b[:200]
blue_200 = np.matrix(U_blue) * np.diag(sigma_blue_200) * np.matrix(V_blue[:num_data, :])

#compress  the image into color image
hi_img = img
hi_img[:,:,0] = red_200
hi_img[:,:,1] = green_200
hi_img[:,:,2] = blue_200

#display red, green, blue image.
fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(red_200, cmap = 'Reds')
ax2.imshow(green_200, cmap = 'Greens')
ax3.imshow(blue_200, cmap = 'Blues')
ax4.imshow(hi_img)
fig = plt.gcf()
fig.set_size_inches(15,15)
plt.suptitle('Higher Resolution, size=200')
plt.show()


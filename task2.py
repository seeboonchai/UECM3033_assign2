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
U_red, Sig_red, V_red = np.linalg.svd(r,full_matrices = True)
U_green, Sig_green, V_green = np.linalg.svd(g,full_matrices = True)
U_blue, Sig_blue, V_blue = np.linalg.svd(b,full_matrices = True)
n_sig = np.count_nonzero(Sig_red)
print("The number of the non zero element for ∑  will be  : ", n_sig)
n_data, dim = r.shape

# Compression for Lower Resolution picture
#red image
Sig_RED_30=Sig_red
Sig_RED_30[30::] = 0
RED_30 = np.matrix(U_red) * np.diag(Sig_RED_30) * np.matrix(V_red[:n_data, :])

#green image
Sig_GREEN_30=Sig_green
Sig_GREEN_30[30::] = 0
green_30 = np.matrix(U_green) * np.diag(Sig_GREEN_30) * np.matrix(V_green[:n_data, :])

#blue image
Sig_BLUE_30=Sig_blue
Sig_BLUE_30[30::] = 0
blue_30 = np.matrix(U_blue) * np.diag(Sig_BLUE_30) * np.matrix(V_blue[:n_data, :])

#display red, green, blue image.
fig = plt.figure(1)
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)
ax1.imshow(RED_30, cmap = 'Reds')
ax2.imshow(green_30, cmap = 'Greens')
ax3.imshow(blue_30, cmap = 'Blues')
fig = plt.gcf()
fig.set_size_inches(15,15)
plt.suptitle('Lower Resolution picture, size=30')
plt.show()

# Compression for Higher Resolution picture
#red image
U_red, Sig_red, V_red = np.linalg.svd(r,full_matrices = True)
Sig_red_200=Sig_red
Sig_red_200[200::] = 0
red_200 = np.matrix(U_red) * np.diag(Sig_red_200) * np.matrix(V_red[:n_data, :])

#green image
U_green, Sig_green, V_green = np.linalg.svd(g,full_matrices = True)
Sig_green_200=Sig_green
Sig_green_200[200::] = 0
green_200 = np.matrix(U_green) * np.diag(Sig_green_200) * np.matrix(V_green[:n_data, :])

#blue image
U_blue, Sig_blue, V_blue = np.linalg.svd(b,full_matrices = True)
Sig_blue_200=Sig_blue
Sig_blue_200[200::] = 0
blue_200 = np.matrix(U_blue) * np.diag(Sig_blue_200) * np.matrix(V_blue[:n_data, :])

#display red, green, blue image.
fig = plt.figure(1)
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)
ax1.imshow(red_200, cmap = 'Reds')
ax2.imshow(green_200, cmap = 'Greens')
ax3.imshow(blue_200, cmap = 'Blues')
fig = plt.gcf()
fig.set_size_inches(15,15)
plt.suptitle('Higher Resolution picture, size=200')
plt.show()

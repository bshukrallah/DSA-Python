from skimage import io
import matplotlib.pyplot as plt
import numpy as np

photo = io.imread("python//images//bird_pexels.jpg")

print(photo)
print(type(photo))
print(photo.shape) # can show resolution

plt.imshow(photo)
plt.show()

plt.imshow(photo[::-1]) #flip upside down (vertical flip)
plt.show()

plt.imshow(photo[:,::-1]) #flip horizontally
plt.show()

plt.imshow(photo[0:300,100:450]) #select certain pixels to show (x,y)
plt.show()

plt.imshow(photo[::2,::2]) #resize, cut in half
plt.show()

photo_sin = np.sin(photo)
print(photo_sin)

photo_mean = np.mean(photo)
print(photo_mean)

photo_mask = np.where(photo > 100, 255, 0)
plt.imshow(photo_mask)
plt.show()
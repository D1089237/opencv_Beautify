import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# 读取图像
image = cv2.imread('IMG_5805.JPG')

# 应用高斯模糊以平滑图像
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# 锐化图像
kernel = np.array([[-1, -1, -1],
                  [-1,  9, -1],
                  [-1, -1, -1]])
sharpened_image = cv2.filter2D(blurred_image, -1, kernel)

# 保存美化后的图像
cv2.imwrite('output.jpg', sharpened_image)

# 显示原始和美化后的图像
cv2_imshow(image)
cv2_imshow(sharpened_image)

# 等待用户按下任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()

# Multi-scaleSR_For_MRI_Blur
使用一种更深更宽的多尺度神经网络来进行核磁共振图像的去除伪影操作

Multi-scale Network with the deeper and wider residual block for MRI motion artifact correction
基本介绍

这个代码的目的是使用一种多尺度的神经网络来对含有伪影的核磁共振图像进行矫正，伪影在核磁共振图像中很常见，多是由于患者的不自主运动（如肌肉骨骼痉挛，或是心律不齐引起的心房颤动）引起。

下图就是一张含有伪影的MRI图像，这副图像的伪影比较明显。大部分实际的伪影是不太明显的（有些只有专业的医生才能分辨）（上面的图像比较明显，下面的不明显）

![明显伪影图像](https://github.com/buptzhang0414/Multi-scaleSR_For_MRI_Blur/blob/master/blurImage.jpg)

![不明显伪影图像](https://github.com/buptzhang0414/Multi-scaleSR_For_MRI_Blur/blob/master/blurImage_little.jpg)

本算法使用一种多尺度的网络结构

![网络结构](https://github.com/buptzhang0414/Multi-scaleSR_For_MRI_Blur/blob/master/network.png)



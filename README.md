# Multi-scaleSR_For_MRI_Blur
使用一种更深更宽的多尺度神经网络来进行核磁共振图像的去除伪影操作

Multi-scale Network with the deeper and wider residual block for MRI motion artifact correction
基本介绍

这个代码的目的是使用一种多尺度的神经网络来对含有伪影的核磁共振图像进行矫正，伪影在核磁共振图像中很常见，多是由于患者的不自主运动（如肌肉骨骼痉挛，或是心律不齐引起的心房颤动）引起。

下图就是一张含有伪影的MRI图像，这副图像的伪影比较明显。大部分实际的伪影是不太明显的（有些只有专业的医生才能分辨）（上面的图像比较明显，下面的不明显）

<img src="https://github.com/buptzhang0414/Multi-scaleSR_For_MRI_Blur/blob/master/blurImage.jpg" width="256pt" height="256pt">

<img src="https://github.com/buptzhang0414/Multi-scaleSR_For_MRI_Blur/blob/master/blurImage_little.jpg" width="256pt" height="256pt">

本算法使用一种多尺度的网络结构

<img src="https://github.com/buptzhang0414/Multi-scaleSR_For_MRI_Blur/blob/master/network.png" width="582pt" height="324pt">

通过提取同一张图像多个不同尺度的特征来更好的表征图像，这种网络不同尺度的网络可以共享参数，使得算法可以很快收敛。

同时我们创造性的提出了一种不同于以往的更宽更深的残差块（DW-ResBlock）（下图c），这种结构使得图像的特征提取的更为充分，同时可以减少网络的层数，使得训练的时间减少，网络的效果基本不变。

<img src="https://github.com/buptzhang0414/Multi-scaleSR_For_MRI_Blur/blob/master/dwresblock.png" width="474pt" height="512pt">

data数据集：由于数据集不是公开数据集，所以暂时还不能公布

转到./Multi-scaleSR，执行

```
python run_model.py --phase=train --batch=10 --lr=1e-4 --epoch=4000 --height=512 --width=512
```

进行训练

测试用代码

```
python run_model.py --input_path=./test_train --output_path=./test_train_res --height=512 --width=512 --gpu=-1
```

下图是部分结果

<img src="https://github.com/buptzhang0414/Multi-scaleSR_For_MRI_Blur/blob/master/result.png" width="545pt" height="340pt">


# Get GVI, SVF, BVF by Image Segmentation 

## Overview

給定一個來源圖檔，將圖檔進行image segmentation，輸出合成圖、得出GVI, SVF, BVF三種scores並輸出至.csv檔。

## Prerequisite
1. `git clone https://github.com/DENGRENHAO/GVI_by_Segmentation.git`
2. `cd .\GVI_by_Segmentation\`
3. run setup.sh
4. Download pretrained model checkpoints(wait for a few minutes):
`curl https://download.openmmlab.com/mmsegmentation/v0.5/pspnet/pspnet_r50-d8_512x1024_40k_cityscapes/pspnet_r50-d8_512x1024_40k_cityscapes_20200605_003338-2966598c.pth -o pspnet_r50-d8_512x1024_40k_cityscapes_20200605_003338-2966598c.pth`

## Usage

查看可用的選項：

```
python main.py --help
```

### 範例

```
python main.py -i C:\thomas\test\gvi_by_segmentation\test_img.jpg
```

- 來源檔案`test_img.jpg`位於 `C:\thomas\test\gvi_by_segmentation\`中，最後會輸出檔案`segmented_test_img.jpg`與‵`scores_of_test_img.csv`到本資料夾中

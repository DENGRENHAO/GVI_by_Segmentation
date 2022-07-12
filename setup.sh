echo "Start setup"
pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.10/index.html
pip install pytorch=1.10.0 torchvision
git clone https://github.com/open-mmlab/mmsegmentation.git
cd mmsegmentation
pip install -e .
mkdir checkpoints
wget https://download.openmmlab.com/mmsegmentation/v0.5/pspnet/pspnet_r50-d8_512x1024_40k_cityscapes/pspnet_r50-d8_512x1024_40k_cityscapes_20200605_003338-2966598c.pth -P checkpoints
cd ..
pip install -r requirements.txt
echo "End setup"
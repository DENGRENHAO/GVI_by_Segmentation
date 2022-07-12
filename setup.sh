echo "Start setup"
pip install mmcv-full==1.4.2
pip install pytorch==1.10.0 torchvision
git clone https://github.com/open-mmlab/mmsegmentation.git
cd mmsegmentation
pip install -e .
mkdir checkpoints
cd checkpoints
echo "Downloading checkpoints......wait for a few minutes"
curl https://download.openmmlab.com/mmsegmentation/v0.5/pspnet/pspnet_r50-d8_512x1024_40k_cityscapes/pspnet_r50-d8_512x1024_40k_cityscapes_20200605_003338-2966598c.pth
cd ../../
pip install -r requirements.txt
echo "End setup"
echo "Start setup"
pip install mmcv-full==1.4.2
pip install pytorch==1.10.0 torchvision
git clone https://github.com/open-mmlab/mmsegmentation.git
cd mmsegmentation
pip install -e .
cd ..
pip install -r requirements.txt
echo "End setup"
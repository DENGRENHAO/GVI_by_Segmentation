from mmseg.apis import inference_segmentor, init_segmentor
from mmseg.core.evaluation import get_palette
# import matplotlib.pyplot as plt
import mmcv
import pandas as pd
import os

def show_plot(model,
              img,
              result,
              palette=None,
              opacity=0.5,
              out_file=None):
    if hasattr(model, 'module'):
      model = model.module
    img_name = os.path.basename(img)
    img = model.show_result(
      img, result, palette=palette, show=False, opacity=opacity)
    # plt.figure(figsize=(15, 10))
    # plt.imshow(mmcv.bgr2rgb(img))
    # plt.title("segmented_"+img_name)
    # plt.tight_layout()
    # plt.show(block=True)
    if out_file:
        mmcv.imwrite(img, "segmented_"+img_name)
        print(f"Completed output segmented_{img_name}")
    return mmcv.bgr2rgb(img)

def get_scores_and_plot(img):
    config_file = 'mmsegmentation/configs/pspnet/pspnet_r50-d8_512x1024_40k_cityscapes.py'
    checkpoint_file = 'pspnet_r50-d8_512x1024_40k_cityscapes_20200605_003338-2966598c.pth'
    config = mmcv.Config.fromfile(config_file)
    config["norm_cfg"]["type"] = "BN"
    config["model"]["backbone"]["norm_cfg"]["type"] = "BN"
    config["model"]["decode_head"]["norm_cfg"]["type"] = "BN"
    config["model"]["auxiliary_head"]["norm_cfg"]["type"] = "BN"
    # build the model from a config file and a checkpoint file
    model = init_segmentor(config, checkpoint_file, device='cpu')
    # test a single image
    result = inference_segmentor(model, img)
    # show the results
    rgb_img = show_plot(model, img, result, get_palette('cityscapes'),opacity=1,out_file=False)
    compound_img = show_plot(model, img, result, get_palette('cityscapes'),opacity=0.5,out_file=True)
    d = {}
    for i in range(rgb_img.shape[0]):
      for j in range(rgb_img.shape[1]):
        color = tuple(rgb_img[i][j])
        if color in d:
            d[color] += 1
        else:
            d[color] = 1
    total = 0
    tree = 0
    grass = 0
    building = 0
    sky = 0
    for key, value in d.items():
      total += value
      if key==(107, 142, 35):
        tree += value
      elif key==(152, 251, 152):
        grass += value
      elif key==(70, 70, 70):
        building += value
      elif key==(70, 130, 180):
        sky += value
    gvi = (tree+grass)/total
    svf = sky/total
    bvf = building/total
    print(f"GVI: {format(gvi*100, '.3f')}%")
    print(f"SVF: {format(svf*100, '.3f')}%")
    print(f"BVF: {format(bvf*100, '.3f')}%")
    data = {'GVI': gvi, 'SVF': svf, 'BVF': bvf}
    df = pd.DataFrame({"key": data.keys(), "value": data.values()})
    img_name = os.path.basename(img)
    img_name = img_name.split(".")
    df.to_csv('scores_of_'+img_name[0]+'.csv', index = False)
    print(f"Completed output scores_of_{img_name[0]}.csv")
import sys
import os.path
import glob
import cv2
import numpy as np
import torch
import src.model.architecture as arch

def img_run():
    model_path = 'run/src/model/RRDB_ESRGAN_x4.pth'
    device = torch.device('cpu')
    with open('run/src/folder.txt','r') as f:
        new_name = f.read()
    test_img_folder = '/Users/kkim2250/Desktop/Project_SRGAN/run/src/static/images/{}/image.png'.format(new_name)

    model = arch.RRDB_Net(3, 3, 64, 23, gc=32, upscale=4, norm_type=None, act_type='leakyrelu', \
                            mode='CNA', res_scale=1, upsample_mode='upconv')
    model.load_state_dict(torch.load(model_path), strict=True)
    model.eval()
    for k, v in model.named_parameters():
        v.requires_grad = False
    model = model.to(device)
    for path in glob.glob(test_img_folder):
        base = os.path.splitext(os.path.basename(path))[0]
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        img = img * 1.0 / 255
        img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
        img_LR = img.unsqueeze(0)
        img_LR = img_LR.to(device)
        output = model(img_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()
        output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
        output = (output * 255.0).round()
        cv2.imwrite('/Users/kkim2250/Desktop/Project_SRGAN/run/src/static/images/{}/image1.png'.format(new_name), output)
        return new_name

import sys
import os.path
import glob
import cv2
import numpy as np
import torch
import src.model.architecture as arch
# import architecture as arch

def img_run():
    model_path = 'run/src/model/RRDB_ESRGAN_x4.pth'
    # model_path = 'RRDB_ESRGAN_x4.pth'
    device = torch.device('cpu')

    test_img_folder = '/Users/kkim2250/Desktop/Project_SRGAN/run/src/static/image.png'

    model = arch.RRDB_Net(3, 3, 64, 23, gc=32, upscale=4, norm_type=None, act_type='leakyrelu', \
                            mode='CNA', res_scale=1, upsample_mode='upconv')
    model.load_state_dict(torch.load(model_path), strict=True)
    model.eval()
    for k, v in model.named_parameters():
        v.requires_grad = False
    model = model.to(device)
    print('Model path {:s}. \nTesting...'.format(model_path))
    for path in glob.glob(test_img_folder):
        print(path)
        base = os.path.splitext(os.path.basename(path))[0]
        print(glob.glob(test_img_folder))
        print(base)
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        print(img)
        img = img * 1.0 / 255
        print('Done1')
        img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
        print('Done2')
        img_LR = img.unsqueeze(0)
        print('Done3')
        img_LR = img_LR.to(device)
        print('Done4')
        output = model(img_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()
        print('Done5')
        output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
        print('Done6')
        output = (output * 255.0).round()
        print('Done7')
        cv2.imwrite('/Users/kkim2250/Desktop/Project_SRGAN/run/src/static/image1.png', output)
        print('Done8')
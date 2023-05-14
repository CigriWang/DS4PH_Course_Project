# Image Denoising based on deep learning methods
 
Bring noisy old photo back to life using UNet, SUNet, and SWINIR

Natural photo (DIV2K) dataset: https://www.kaggle.com/datasets/joe1995/div2k-dataset

Old photo dataset: https://hpcbristol.net/photographers

## :pushpin: How to use the web app?

You can select from natural image dataset or old photo dataset, and then you can pick one of the pictures out of three to display the denoised result.

Or you can upload your own picture to bring it back to life.

## :rocket: How to run the file?

```
t_data = '' # Input data
l_data = '' #Input Label
test_image = '' #Image to be predicted while training
test_label = '' #Label of the prediction Image
test_folderP = '' #Test folder Image
test_folderL = '' #Test folder Label for calculating the Dice score
 ```
Models are written in the SUNet.py SWINIR.py and Models.py

The best model weights will be saved in ./model/UNet_XX_XX/best.pth
 
Run test set using eval.py (PATCH_IT.py is used for divide the image input patch for SWINIR model)

The test output will be saved to ./model/gen_images/

## :round_pushpin: Results

Among three models, SUNet performs better than the other two models. More detail please refer to the report.

## :book: References

1) **UNet** - U-Net: Convolutional Networks for Biomedical Image Segmentation
https://arxiv.org/abs/1505.04597

2) **SUNet** - Swin-Transformer UNet 
https://ieeexplore.ieee.org/document/9937486

3) **SwinIR** - Swin-Transformer Image Restoration
https://arxiv.org/abs/2108.10257

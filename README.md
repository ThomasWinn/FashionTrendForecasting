# FashionTrendForecasting

The goal of this project is to create a full pipeline which calculates the popularity of fashion trends based on social media posts and see how long that trend will last to gauge if we should invest in this trend or not.

## Notes

Use pipreqs to get requirements.txt



## Methods

- From the paper (https://arxiv.org/abs/1703.06870)
    - Pixel to Pixel Alignment is implemented which is not in Fast RCNN outputted from each ROI (bounding box)
    - ROIAlign implemented to increase accuracy of mask outputs
    - (old)Use FCN (Fully Convolution Network (CNN)) to predict mask from ROI (Bounding box) because Convolution layers retain spatial orientation
        - Wouldn't use Fully connected layers because spatial orientation of pixels in respect to eachother are lost
    - (new) Use FPN (Feature Pyramid Network) instead of Fully Convolutional Network
    
- Summary Fast RCNN 
    - Determine ROI = Bounding box for each object class using RPN (Region Proposal Network)
    - For each ROI, determine class label. Done with ROI Pooling
        - Problem with data loss in ROI Pooling because we are downsampling or maxpooling our ROI getting rid of key features when max pooling
        - Problem with strides when ROI Pooling as data is misaligned and data is lost
            - Only misaligned and data lost if stride is rounded up or down due to decimal stride i.e 18x18 -> 7x7 = stride 2.57 = 3
        - **Solution = use ROI Align so can use stride 2.57 using interpolation**
        - ROI Align = preserves spatial orientation of features with no loss of data within different ROI's

- Summary Mask RCNN
    - Mask RCNN Impelmentation
        - Determine bounding box for each object of interest (ROI). We use Region Proposal Network (RPN) to do this
        - For each ROI
            - Determine Class Label
            - Implement ROI Align to preserve spatial orientation of features with no loss of data within different ROI's 
                - This implementation fixes the problems with ROI Pooling where within downsampling we would lose data
        - Use Fully Convolutional Network (FCN) to predict mask for each ROI 
            - We use FCN for this because it retains spatial orientation unlike using fully connected layers
        - Output 
            - Bounding Box 
            - Class Label
            - Image Segmentation Mask
    - Used for Instance Segmentation where it is done by using Bounding Box + Semantic Segmenation
    - Mask RCNN = Fast RCNN + FCN/FPN
    

## Datasets
- [DeepFashion](https://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html)
- [DeepFashion2](https://github.com/switchablenorms/DeepFashion2)

## References
* [Heuritech](https://www.heuritech.com/)
* [(2023) Integrated Approach for Clothing Detection and Comparison using Structural Shape Detection and Texture Analysis](https://pdf.sciencedirectassets.com/280203/1-s2.0-S1877050923X0009X/1-s2.0-S1877050923014047/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIGXQjUlqStgTGkQqHUjucNlK3C6zNILOrEB%2F5Qyiwy%2FQAiB3FHbEkqOj13fPoAGOOstnkbwLBHM5R46LyEbrc3R93yq8BQiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAUaDDA1OTAwMzU0Njg2NSIM6HwlLOqMzW7mTy28KpAFCMAoAMr3hqXFoQ%2F%2F7XsJ15pDMwU3g%2FHpSl8pmwx3YNXpFagW3X2MoqE4cCnpSygtVJRiEPFigYzqscPqfqfbuEH%2BYYOwnEKuBZfEcowT%2BC%2F923aKwBQsZ5kLwHnoI27ZDMlS7NNdfEkmCLgUHuS%2BIunU5VXgYaQlu3Ygd7hvwPpjJcBokftX4VxRcK8fQRAvf80BVNL%2FaESB0XWdWYtzUyHHRiNs3GgALurU%2BnXRT6wObUkbHWFsPnihSiQz%2FT5yooJd%2F1A%2B2fUDVWzey1mue5EiPzBN8T76je98WjoWbSwdlewls8HnGsb79A%2FA%2B75zjK4BoXiDuXrnHbTe21EnThaeSjv5iy3hObXzulA8s4pCf5tpP75ighaQvJsrgj8%2Bey%2BOrSHXLcyg7QDShKHPfSACCRBUFWDSUFMOdWhx9dCDvZwyp%2FtqdHo9EGsmHssFiscJc59FcdQfN9Nu2Jeb06s6DQoBgbMNGR8Mb0lBPaEgnNeHj97LrvxOWxz7Op%2BcqRN1HjJp9mcRnpF4NJQ9OVX2swfWUes4dQ2xpm6%2FYQtgZxeUl3gcBLy92Bx0CJP1H96t195RBd2QyzRLRR2KpB%2FaccNnVuyvZOOXBBUiuxqmA6rDG37YiiRSPCsob%2BqtpLzzFt7etK1U6yBrDhVkc1hPixrvzEQBT4%2BdCd2DJj6kAOi5bQg3SDIo6eMw891BGfc5zWbf%2BAO%2B1V9zP5YIus1KOZ8ZawoPtDPFRESlMjfUiQ7vu4AScrGBFOdVRBN7PWjJ45u2xN2axiG%2BegmMPDKM9%2BpLqMpWLS6T2lGieFZlB6lhNiK8cpWVjGgHhdXAgohCZ8GR0IEpMBpy9K4kvTvWkJz0oVC7FCHvNZeD6o8wxIiprAY6sgGGItXYho9pqLZjDv1PQysLDDWjjw6pypR7VOu%2B%2F7q7vl6AFUuZC1zoARZoYL6A%2BIu18hJIZRk%2FKbaJ3dHIcYQiDwM0y2LMOcra1IgFvYgRqCz%2BVZZccvZHw3ke0YCVHNd7rde2TCPAcUI8HmXEHTV5ixRQZ5F2fP0nhzqi1BLg3CtRFhcaXmuGUf6akjtzvXYNNvvFxK0fLb6087XqlbWVZZR%2B%2FZpwPo7SdoOJa5%2BQd%2BUL&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231226T041718Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYY4UCIB6P%2F20231226%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=fb838bf4a0a5db99d88a775164b09f093a507a59a706f0951c672265ccb5e97a&hash=10cc8e4709b4b31525143c4e3fdb3a3fca180eb319fdd4dcda83ce91df1d625d&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S1877050923014047&tid=spdf-e5481efb-91da-4e92-9cfd-d7830160ad6e&sid=0bbc941e631e8948c55977e79eb82bb7e46dgxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=0f135a5104515c525658&rr=83b683693847c633&cc=us)
* [(2018) Mask RCNN](https://arxiv.org/abs/1703.06870)

## Other Cool Projects
* [(2023 - Yolov5) Using Object Detection Technology to Identify Defects in Clothing for Blind People](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10181740/)
# Image Super Resolution Project (ESRGAN)

## Project Overview

This project focuses on implementing Enhanced Super Resolution Generative Adversarial Networks (ESRGAN). The project aimed to explore and apply techniques from image processing, machine learning, and GANs to enhance image resolution. The journey involved a step-by-step approach to understanding and implementing various components that culminate in the final super-resolution model.


## Topics Explored

### Image Processing with OpenCV

The project began with a deep dive into fundamental image processing using OpenCV, covering:

- Basic operations like resizing, rescaling, and color space conversion
- Techniques for image smoothing, such as erosion, dilation, and different blurring methods

Key image processing functions were also explored, including:

- Building Gaussian pyramids
- Applying Canny edge detection
- Using the SIFT algorithm for feature detection
- Working with contours and convex hulls

**First Assignment**:  
This assignment involved importing images, initiating live video feeds with OpenCV, altering color schemes, and applying various image transformation techniques like blurring and smoothing. A creative task included creating a pencil sketch effect for both static images and live video. All related work is organized in the `Assignment 1` folder.

### Introduction to Machine Learning

Next, the focus shifted to foundational machine learning concepts:

- **Google’s Machine Learning Course**: Covered key terms and concepts like training and validation datasets, feature engineering, logistic regression, neural networks, and embeddings.
- **Udacity’s TensorFlow Course**: Provided deeper insights into Convolutional Neural Networks (CNNs) and the power of transfer learning.


### Basics of Generative Adversarial Networks (GANs)

The project then explored the intriguing world of GANs:

- GANs are a type of machine learning model designed to generate data that closely mimics real-world examples.
- A GAN typically consists of two competing models: a generator that creates synthetic data and a discriminator that attempts to distinguish between the real and generated data.
- Various loss functions associated with GANs and the common challenges encountered during training were also examined.

**Anime Sketch Coloring GAN Assignment**:  
This assignment involved creating a GAN capable of coloring anime sketches based on input data. Although challenging, the results were fascinating and rewarding. The implementation is available in the `Assignment 3` folder.

### Super-Resolution with SRGAN and ESRGAN

The final section of the project centered on the main objective: image super-resolution using SRGAN and ESRGAN. Key concepts included:

- Understanding and implementing perceptual loss
- Adapting the discriminator network for super-resolution tasks

**Final Implementation**:  
The project culminated in enhancing low-resolution images to high-resolution counterparts using the ESRGAN framework. This implementation brought together all the skills and knowledge acquired throughout the project, including:

- Image processing with OpenCV
- Model development with TensorFlow
- Utilizing transfer learning for VGG loss computation
- Applying GANs to achieve the desired super-resolution

The final Jupyter notebook, summarizing the outcomes of the training sessions, can be found in the `FinalESRGAN` folder.

## Summary

This project served as a comprehensive exploration of image processing, machine learning, and GANs, leading to the successful implementation of an image super-resolution model. Each stage of the project built upon the last, with all relevant assignments and final implementations carefully documented in their respective directories.

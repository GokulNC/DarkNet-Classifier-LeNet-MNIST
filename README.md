# DarkNet Classifier LeNet MNIST

LeNet Training & Inference for MNIST dataset on DarkNet.

## Requirements

- [DarkNet](https://github.com/pjreddie/darknet/tree/61c9d02ec461e30d55762ec7669d6a1d3c356fb2) built
- `pip install opencv-python`
- `pip install numpy`

## Download & Convert MNIST data

```
python download_and_convert_mnist.py
```

## Set it up for DarkNet
1. Copy the contents of `cfg` folder in this repo to `darknet/cfg`
2. Move `mnist_images` folder to `darknet/data/` folder
3. Then,
```
cd darknet/data/mnist_images
find `pwd`/train -name \*.png > train.list
find `pwd`/test -name \*.png > test.list
cd ../..
```

## Train
```
./darknet classifier train cfg/mnist.data cfg/mnist_lenet.cfg
```

## Validate
```
./darknet classifier valid cfg/mnist.data cfg/mnist_lenet.cfg backup/mnist_lenet.backup
```

## Predict
```
./darknet classifier predict cfg/mnist.data cfg/mnist_lenet.cfg backup/mnist_lenet.weights data/mnist_images/test/<image_name>.png
```

## Credits
https://pjreddie.com/darknet/train-cifar/  
https://github.com/ashitani/darknet_mnist

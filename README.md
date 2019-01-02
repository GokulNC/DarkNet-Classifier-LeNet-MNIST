# darknet_mnist

Training LeNet for MNIST dataset on darknet.

# Requirements

- darknet
- opencv
- numpy

# Download & Convert MNIST data

```
python download_and_convert_mnist.py
```

# Set it up for DarkNet
1. Copy the contents of `cfg` folder in this repo to `darknet/cfg`
2. Move `mnist_images` folder to `darknet/data/` folder
3. `cd darknet/data/mnist_images`
4. `find `pwd`/train -name \*.png > train.list`
5. `find `pwd`/test -name \*.png > test.list`
6. `cd ../..`


# Train

```
./darknet classifier train cfg/mnist.data cfg/mnist_lenet.cfg
```

# Validate

```
./darknet classifier valid cfg/mnist.data cfg/mnist_lenet.cfg backup/mnist_lenet.backup
```

# Predict

```
/darknet classifier predict cfg/mnist.data cfg/mnist_lenet.cfg ./mnist_lenet.weights data/mnist_images/test/<image_name>.png
```

## Credits
https://pjreddie.com/darknet/train-cifar/  
https://github.com/ashitani/darknet_mnist

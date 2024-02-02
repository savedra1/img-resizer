# A simple image resizing CLI - PyPi package deployemnt CI example 

### About
This project is used for an example of how to deploy a Python package to PyPi using GitHub Actions. The example package is a simple CLI tool I built many moons ago that allows you to easily resize any image file from the command line. Feel free to use this if you think it would be useful but you're probably better off with [ImageMagick](https://github.com/ImageMagick/ImageMagick).

### Installation 
```
pip install resize-img
```

### Comands
- `resize-img $IMG_PATH` Saves a new, resized image of the specified image path to the CWD, using the default size of 512x512px.
- `resize-img $IMG_PATH small` Saves specified image as 512x512px in CWD   
- `resize-img $IMG_PATH medium` Saves specified image as 1000x1000px in CWD
- `resize-img $IMG_PATH big` Saves specified image as 2000x2000px in CWD
- `resize-img $IMG_PATH custom <int> <int>` Saves specified image as <int>px<int>px in CWD

## Staging package deployment 
---- TBC
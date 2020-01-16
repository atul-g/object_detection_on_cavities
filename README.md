# Detecting tooth decay and cavities using Tensorflow Object Detection API

![image_prediction](https://raw.githubusercontent.com/atul-g/object_detection_on_cavities/master/my_custom_detector/prediction1.png)

In this project I use tensorflow's ![Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) to detect tooth decay and possibly early stage cavities. I made my own dataset of images, which was collected from Google Images.

Note:I made a [similiar project](https://github.com/atul-g/cavity_detection) on this before where I used CNN to **classify** images into categories- having decay/cavities, not having any decay/cavities. The results weren't convincing enough so I decided to move to Object Detection. The results turned out to be much better.

# Project Tree:
* The `models` directory is cloned from tensorflow's [models](https://github.com/tensorflow/models) repo.
* The `labelimg-master` is cloned from this [repository](https://github.com/tzutalin/labelImg). I used it to annotate my images.
* The main working directory is the `my_custom_directory`:
* `images` contains our dataset of images with it's corresponding xml files which was created with the help of labelimg.
* `ssd_mobilenet_v1_coco_2018_01_28` is the model which I used to train on my dataset. Other models can be found [here](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md).
* The `training` directory contains the config files for the model and also the label-map which is needed by the model for training and also detection. The model stores it's checkpoints in this directory.
* `trained_inference_graph` contains the graph exported from the trained model using the `export_inference_graph.py` script which was copied from the object_detection directory.
* `model_main.py` is the script which is used to start the training of the model.
* `generate_tfrecord.py` and `xml_to_csv.py` were scripts used from this [repo](https://github.com/datitran/raccoon_dataset). A  really simple and convenient way to convert the xml files created to CSV and then generating Tensorflow records which will be used to train the model. The generated CSV files and the TFrecords are in the `data` directory.

# Training:
1. Clone the models repo from tensorflow. Follow their installation instructions to setup the environment needed for the project.
2. Collect the dataset. I had around 350 images in total
3. Annotate the images with the help of labelimg. Run `python3 labelimg.py` to start the application.
4. Use `xml_to_csv.py` and `generate_tfrecords.py` to get the final train.records and test.records files.
5. Select your model and clone it. Get the corresponding config file from `/models/research/object_detection/samples` directory. 
6. Edit the config file.
7. Create the .ptxt file which will be the label-map. Mine is [object-detection.pbtxt](https://github.com/atul-g/object_detection_on_cavities/blob/master/my_custom_detector/training/object-detection.pbtxt).
8. Run the model_main.py. I used 40000 steps to train the model.
9. Use export_inference_graph.py to generate the graph needed for further prediction. (Use the best checkpoint file for this)
10. For further predictions just paste images in the `test_image_dir`.
11. The code to make predictions from trained models were derived from the `object_detections_tutorial.ipynb`. I made a few changes to it as the code seemed to render some errors.

Since I trained it in colab, you can find the [`cavity_detection.ipynb`](https://github.com/atul-g/object_detection_on_cavities/blob/master/my_custom_detector/cavity_detection.ipynb) notebook which does all of the above.

### References:
* [Object Detection using Tensorflow API](https://www.youtube.com/watch?v=COlbP62-B-U&list=PLQVvvaa0QuDcNK5GeCQnxYnSSaar2tpku&index=1)
* [Tensorflow Object Detection Docs](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/)

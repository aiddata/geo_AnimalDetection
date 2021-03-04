
import tensorflow_hub as hub
import os
import sys
import numpy
import tensorflow as tf

ROOD_DIR = os.path.abspath("../")
sys.path.append(ROOD_DIR)

#model_handler = "https://tfhub.dev/google/faster_rcnn/openimages_v4/inception_resnet_v2/1"
#detector = hub.load(model_handler).signatures['default']
img = r"/home/mirandalv/Documents/github/birds_detection/processing_data/clipped/9_clip.tif"

def load_tif(path):

    try:
        img = tf.io.read_file(path)
        # img = rasterio.open(path)
    except:
        print(path)
        raise

    # test = tf.image.decode_image(img, channels=3)


load_tif(img)
import os
import shutil
from shutil import copyfile
# change the respective paths to get the dataset splits
TRAIN_PATH = '/content/drive/MyDrive/Multimodal_Machine_Translation/Image_Splits/image_splits/train_images.txt' # Add the path to the training splits file
IMAGE_PATH = '/content/drive/MyDrive/Multimodal_Machine_Translation/flickr30k_images/'  # Add the path of Flickr 30K Images
VAL_PATH = '/content/drive/MyDrive/Multimodal_Machine_Translation/Image_Splits/image_splits/val_images.txt' #Add the path of the validation splits
TEST_2016_PATH = '/content/drive/MyDrive/Multimodal_Machine_Translation/Image_Splits/image_splits/test_2016_images.txt' # Add the path of the test_2016 split
TEST_2017_PATH = '/content/drive/MyDrive/Multimodal_Machine_Translation/Image_Splits/image_splits/test_2017_images.txt' # Add the path of the test_2017 split

#create folders for train, validation, test_2016, and 2017 splits
train_split = '/content/drive/MyDrive/Multimodal_Machine_Translation/Train/'
val_split = '/content/drive/MyDrive/Multimodal_Machine_Translation/Validation/'
test_2016 = '/content/drive/MyDrive/Multimodal_Machine_Translation/Test_016/'
test_2017 = '/content/drive/MyDrive/Multimodal_Machine_Translation/Test_017/'

# Create directories if not previously present
if not os.path.exists(train_split):
    os.mkdir(train_split)

if not os.path.exists(val_split):
    os.mkdir(val_split)

if not os.path.exists(test_2016):
    os.mkdir(test_2016)

if not os.path.exists(test_2017):
    os.mkdir(test_2017)

# Open the text file fpr train, validation, test_2016, and test 2017
f = open(TRAIN_PATH, 'r')
train_files = f.read().split()
train_files = list(train_files)

f = open(VAL_PATH, 'r')
val_files = f.read().split()
val_files = list(val_files)

f = open(TEST_2016_PATH, 'r')
test_2016 = f.read().split()
test_2016 = list(test_2016)

f = open(TEST_2017_PATH, 'r')
test_2017 = f.read().split()
test_2017 = list(test_2017)

# Path to the images folder
Image_folder = [i for i in os.listdir(IMAGE_PATH) if os.path.isfile(os.path.join(IMAGE_PATH,i))]
train_folder = [i for i in Image_folder for j in train_files if j in i]
val_folder = [i for i in Image_folder for j in val_files if j in i]
test_folder_2016 = [i for i in Image_folder for j in test_2016 if j in i]
test_folder_2017 = [i for i in Image_folder for j in test_2017 if j in i]

# Comparing the lists before moving the splits
train_folder = set(train_folder)
intersection = train_folder.intersection(train_files)
train_folder = list(intersection)

print(len(train_folder))

val_folder = set(val_folder)
intersection = val_folder.intersection(val_files)
val_folder = list(intersection)

print(len(val_folder))

test_folder_2016 = set(test_folder_2016)
intersection = test_folder_2016.intersection(test_2016)
test_folder_2016 = list(intersection)

print(len(test_folder_2016))

test_folder_2017 = set(test_folder_2017)
intersection = test_folder_2017.intersection(test_2017)
test_folder_2017 = list(intersection)

print(len(test_folder_2017))

for i in val_folder:
    source = os.path.join(IMAGE_PATH, i)
    destination = os.path.join(val_split, i)
    copyfile(source, destination)

print(f'The images have been copied to the validation folder: {len(val_folder)} images')

for i in train_folder:
    source = os.path.join(IMAGE_PATH, i)
    destination = os.path.join(train_split, i)
    shutil.copyfile(source, destination)

print(f'The images have been copied to the train folder: {len(train_folder)} images')

for i in test_2016:
    source = os.path.join(IMAGE_PATH, i)
    destination = os.path.join(test_2016, i)
    shutil.copyfile(source, destination)

print(f'The images have been copied to the test_2016 folder: {len(test_2016)} images')

for i in test_folder_2017:
    source = os.path.join(IMAGE_PATH, i)
    destination = os.path.join(test_2017, i)
    shutil.copyfile(source, destination)

print('The images have been copied to the test_2017 folder')
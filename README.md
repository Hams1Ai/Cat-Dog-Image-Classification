# Cat-Dog Image Classification 🐱🐶

## Project Description
This project is an image classification model that identifies whether an input image is a **Cat** or a **Dog**.

The model was created and trained using **Google Teachable Machine** and exported as a **TensorFlow/Keras model**. Python is used to load the trained model and classify a new image.

## Classes
The model contains two classes:

- Dog
- Cat

## Steps

1. Collected images of cats and dogs.
2. Uploaded the images to Google Teachable Machine.
3. Created two classes: Dog and Cat.
4. Trained the image classification model.
5. Tested the model using new images.
6. Exported the trained model using TensorFlow → Keras.
7. Loaded the Keras model using Python.
8. Preprocessed the test image to 224 × 224 pixels.
9. Used the trained model to predict the image class.
10. Displayed the predicted class and confidence score.

## Files

- `main.py` - Python code used to load and test the model.
- `keras_model.h5` - Trained Keras image classification model.
- `labels.txt` - Contains the class names.
- `dog.jpg` - Test image.

## Libraries Used

- TensorFlow
- Keras
- NumPy
- Pillow

## Test Result

The model was tested using a dog image.

**Predicted Class:** Dog  
**Confidence Score:** 50.00%

## Tools

- Google Teachable Machine
- Google Colab
- Python
- GitHub

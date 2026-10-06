
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

# Load the model
model = tf.keras.models.load_model("keras_model.h5", compile=False)

# Load labels
class_names = open("labels.txt", "r").readlines()

# Load test image
image = Image.open("dog.jpg").convert("RGB")

# Resize image
image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

# Convert image to numpy array
image_array = np.asarray(image)

# Normalize image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Prepare input
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
data[0] = normalized_image_array

# Make prediction
prediction = model.predict(data)
index = np.argmax(prediction)

class_name = class_names[index].strip()
confidence_score = prediction[0][index]

# Display result
print("Class:", class_name)
print("Confidence:", f"{confidence_score * 100:.2f}%")

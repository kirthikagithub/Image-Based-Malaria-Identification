# Image-Based-Malaria-Identification
The Malaria Identification App is designed to provide a user-friendly interface for predicting the likelihood of malaria infection in uploaded images.
GUI with PyQt5:

The graphical interface is built using the PyQt5 library, offering an intuitive and interactive experience for users.
Upload Image Button:

The "Upload Image" button allows users to select an image file (in JPG or PNG format) from their local system for analysis.
Image Prediction:

Upon uploading an image, the program displays the selected image in the GUI and predicts whether it contains malaria parasites or is uninfected. The prediction is based on a pre-trained TensorFlow model.
Real-time Accuracy Feedback:

The program tracks the number of correct predictions and the total number of predictions, updating the accuracy percentage in real-time. This information is displayed in the GUI to provide users with an indication of the model's performance.
Accuracy Message Box:

A message box appears, showcasing the overall accuracy of the model's predictions after each image analysis.
Model Loading:

The script loads a pre-trained TensorFlow model ("model.h5") for image classification. This model is used to predict whether an input image is infected with malaria parasites or not.
Accuracy Calculation:

The program calculates the accuracy by comparing the predicted result with the actual label of the uploaded image (whether it's infected or uninfected). The overall accuracy is displayed to the user.
Continuous Learning:

The program encourages continuous learning by providing users with immediate feedback on the accuracy of predictions. This feature enhances user understanding and trust in the model.
Dynamic User Interface:

The GUI dynamically updates with the image and prediction information, ensuring a visually appealing and informative presentation.
Informative Labels:

The GUI includes informative labels such as the predicted result, whether the prediction is correct, and the real-time accuracy percentage.

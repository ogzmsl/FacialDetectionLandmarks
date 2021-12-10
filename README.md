<div id="top"></div>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ogzmsl/HandDetection/blob/main/ouz-logo.png">
    <img src="/ouz-logo.png" alt="" width="" height="">
  </a>

  <h3 align="center">Python Facial Recognition</h3>

  <p align="center">
    Python with OpenCV - MediaPip Framework Facial Detection
    <br />
    <a href="https://www.width.ai/post/facial-detection-and-recognition-with-dlib"><strong>Explore the docs »</strong></a>
    <br />
    <br /> 
    <a href="https://oguzmuslu.com">Contact Me</a> 
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

[![product-screenshot]](https://pythonrepo.com/repo/cvzone-cvzone)

It is a Computer vision package that makes it easy to operate image processing and AI functions. It mainly uses OpenCV and Google Mediapipe libraries.

Usage areas
* Military Industry (submarine sonic wave scans), underwater imaging.
* Security, criminal laboratories.
* Medicine.
* Clarification of structures such as tumors, vessels, Tomography, Ultrasound.
* Robotics, traffic, astronomy, radar, newspaper and photography industry applications
* Vb..

Here we just do hand identification with a computer camera based on the basics.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

Libraries and programming language I use.

* [Python](https://www.python.org/)
* [OpenCV](https://opencv.org/)
* [Mediapip](https://mediapipe.dev/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

The materials you need to do this.

### Installation

· Install PIP packages

   ```sh
   ! pip install opencv
   ```
   ```sh
   ! pip install mediapip
   ```
   
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

### Girl Face Detection in Images

![girl-detector]

```
import cv2
import mediapipe as mp

#Image Path
image = cv2.imread("Brown-hair-girl-portrait-face_1280x800.jpg")
height, width, _ = image.shape
print("Height, width", height, width)

```

### My Face Detection in PC Camera

![my-faceDetection]

```
import cv2
import mediapipe as mp

#Camera Capture
cap = cv2.VideoCapture(0)

while True:
    #Video Path
    ret, image = cap.read()
    if ret is not True:
        break

```

<!-- CONTACT -->
## Contact

Twitter - [@filokipatisi](https://twitter.com/filokipatisi) <br>
E-Mail -  [GMAIL](mailto:oguzzmuslu@gmail.com) <br>
Linkedin - [oguzzmuslu](https://www.linkedin.com/in/oguzzmuslu/)


<p align="right">(<a href="#top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[my-faceDetection]: https://raw.githubusercontent.com/ogzmsl/FacialDetectionLandmarks/main/my-face.jpeg
[product-screenshot]: https://raw.githubusercontent.com/ogzmsl/FacialDetectionLandmarks/main/facial-detector.jpg
[girl-detector]: https://raw.githubusercontent.com/ogzmsl/FacialDetectionLandmarks/main/girl-detector.jpeg

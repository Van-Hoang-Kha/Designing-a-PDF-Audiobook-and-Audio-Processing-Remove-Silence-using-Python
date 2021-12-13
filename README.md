# Designing a PDF Audiobook and Audio Processing, Remove Silence using Python
In this code, a simple implementation of PDF Audiobook is shown. PDF text is read to the user as audio using this code.

### Introduction
Reading stories or essays or any text can be arduous, however an audio reading of the text is convenient and doesnt require as much concentration as reading requires. In this project, I implemented a simple PDF to audio converter. This code scans page(s) of PDF and reads it using audio, to the user. While this project is good for simple text reading, it does not perform good if a scientific paper with equations is given to it because equations are not supported to be read in pytesseract OCR library which we used to convert image to text.

### Project Flow
Here is the project flow diagram:

![image](https://user-images.githubusercontent.com/72704844/145893378-fea0afaa-1ea8-44d4-a9d5-74e955992188.png)

### Project flow

* First, we take the PDF file and convert each page into image using PyMuPDF software.
* Then, we take the image(s) and scan the text in the image using Pytesseract OCR software.
* Then, we use Google Text to Speech (gTTS) library to convert text to audio file.
* Lastly, we get the Pygame mixer to play the audio file loud.
### Prerequisite software
### The software libraries required to run this code can be installed using:
``` pip install Pillow ```           # -------- image reader library.

``` pip install PyMuPDF ```          # -------- library to convert PDF page to image.

``` pip install pytesseract ```      # -------- Image to text converting Optical Character Recognition library.

``` pip install pygame ```           # -------- pygame to play audio.

``` pip install gTTS ```            # -------- Google Text To Speech.

``` pip install pysimplegui ```      # -------- This library makes GUI development far simpler than tkinter.

``` pip install tesseract ```       

``` pip install tesseract-ocr ```

### Conclusion
It was seen that the code performs really well in reading straightforward PDF text files, however, if equations are involved in the text, then the reader cannot properly read the equations. Hence, the code is good for simple text but not for scientific papers as it will fumble reading the equations. However, text will be read just fine.

Please give a star to the repo to let me know if the work helped you.
Audio Processing Techniques like Play an Audio, Plot the Audio Signals, Merge and Split Audio, Change the Frame Rate, Sample Width and Channel, Silence Remove in Audio, Slow down and Speed up audio

### This Repository includes how to

* Play an audio
* Plot the Audio Signals
* Merge and Split Audio Contents
* Slow down and Speed up the Audio - Speed Changer
* Change the Frame Rate, Channels and Sample Width
* Silence Remove
### Installation
```pip install webrtcvad==2.0.10 wave pydub simpleaudio numpy matplotlib```

To install Tesseract OCR for Windows:

* Run the installer: https://tesseract-ocr.github.io/tessdoc/Downloads.html
* Configure your installation (choose installation path and language data to include)
* Add Tesseract OCR to your environment variables

To install and use Pytesseract on Windows:
* Simply run ```pip install pytesseract```
* You will also need to install Pillow with pip install Pillow to use Pytesseract. Import it in your Python document like so from PIL import Image.
* You will need to add the following line in your code in order to be able to call pytesseract on your machine: **pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'**

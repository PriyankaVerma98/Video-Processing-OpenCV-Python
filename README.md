## Introduction

**Objective:**

This project was developed as part of a smart electricity billing application based on research work by Elrefaei et al., [1]. It has the potential to save time, prevent human errors during electricity bill generation. 

Four units namely- Volt, Ampere, Kilowatt, Kilowatt-Hour, were extracted in real time from digital electricity meter videos using OpenCV and Python. Please see the report in this repository for a detailed documentation.

**Method:** 

- First videos were pre-processed to extract the digital display area using color filtering and contour detection. 

- After extracting screen, template matching was tried to extract key metrics. 

- The results were improvised by using feature matching. 
    - Various algorithms like SIFT and ORB were tried for feature extraction. 
    - Brute force and Flann based techniques were tried for feature matching. 
    - Then ratio test was used to extract good points. 
 
- Identified units were displayed on screen 

***** 

## Feature Extraction and Matching 
Following images show the result of ORB with Flann technique.

![Volt](https://user-images.githubusercontent.com/39693183/63647974-5d644000-c746-11e9-8c9b-466bd1e038f8.png)


![KiloWatt hour](https://user-images.githubusercontent.com/39693183/63647975-5fc69a00-c746-11e9-921e-93ff605a3cd2.png)


![Amperes](https://user-images.githubusercontent.com/39693183/63647976-62c18a80-c746-11e9-82bc-79d141bc6a5d.png)


![KiloWatt](https://user-images.githubusercontent.com/39693183/63647979-69500200-c746-11e9-9bc9-c375c56985b0.png)

****


## Results

[Link to the video with result](https://drive.google.com/open?id=1FaaPnWijvFikdoWgZjdGRic1jOd0Oh58)


![Screen Shot 2019-08-24 at 11 36 05 PM](https://user-images.githubusercontent.com/39693183/63641233-80e8a580-c6c8-11e9-92e4-3580cedd3f7b.png)


****


## Scope

Earlier process to take the meter readings and generate bills involved a company official to make home visit, note down the reading then a bill is generated at the office and couriered to the home.

****

The project had been developed as a partial fulfillment of the *Practice School 1* course at BITS Pilani. The project has been developed under the guidance of Senior Scientist at [BISAG, Gandhinagar](https://bisag.gujarat.gov.in). The software was accepted by [Gujarat Power R&D Department](https://www.gprd.in) for further development. I received the **Innovation Challenge Award** and cash prize by **Dept. of Science and Technology, Govt. of Gujarat** for high impact results. 

Reference [1] : Elrefaei, L. A., Bajaber, A., Natheir, S., AbuSanab, N., & Bazi, M. (2015, November). Automatic electricity meter reading based on image processing. In 2015 IEEE Jordan Conference on Applied Electrical Engineering and Computing Technologies (AEECT) (pp. 1-5). IEEE. [Link](https://github.com/PriyankaVerma98/Video-Processing-OpenCV-Python/blob/master/ResearchPaper.pdf)

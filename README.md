# Hate Detector

Group project for [Hack the North 2019](https://hackthenorth.com). 

Team members: 
- [Wais Shahbaz](https://github.com/wshahbaz)
- [Jack Lu](https://github.com/Jacklu0831)
- [Sunanda Gamage](https://github.com/sgamage2)
- [Eric Luo](https://github.com/2017soft)

## Inspiration

There exists many scenarios and situations where people are abusing each other in many shapes and forms, but one of the most prevalent forms is in verbal abuse. Hate Speech is referred to the concept of using vulgar language and discriminatory terms to invoke pain in another's mood, gain power and more. There exists a need for an automated solution to this problem, and that will be our web application.

## What it does

Our web app receives a text input, classified each sentence of the body of text with a natural language processing model in categories of "hate speech", "offensive language", and "neutral". The results are displayed in a table format under the text box. Each sentence has a color code associated with it to graphically display its degree of hate/offensiveness.

## How we built it

Using Django web framework and coding in python, we developed a web GUI that allows a user to input any size of text, and once the data is processed, our GUI displays the results of each phrase in a friendly, colour coded table with numerical ranks and an overall "Hate" rank. To quantify the degree of hate in each separate body of text (sentences), we used the pre-trained NLP model sourced from "Automated Hate Speech Detection and the Problem of Offensive Language" research paper in 2017.

## What's next for Verbal Abuse Detector

The verbal abuse detector could be extended to finding similar problems in videos and audios with a speech to text model.

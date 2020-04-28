# web_crawling_and_personality_traits_detection

This project has mainly two sections

1. crawling images form websites(here in this repository considered only one website but it can be extended further to multiple websites)
2. predicting personality traits of images of the person we got from crawlong websites based on Big_O formula and implimentation of it in Convolutional neural networks

in this project it was implimented on pycharm IDE

Libraris and models used include----->>

1. for crawling websites (popularly know as scraping)
  1.scarpy
  2.requests

2. for prediction of personality traits (BIG O factor prediction)
  1.Tensorflow
  2.keras
  3.Reset34Model(with trained parameters taken form limited training data set available so it may impact on accuracy of the model predicitons)
  3.numpy
  4.open CV
  
3. for creating database(.db) file
  1.sqlite3
  
  final output is a database file containing [name,image_link,image(BLOP),'Openness', 'Conscientiousness', 'Extroversion', 'Agreeableness', 'Neuroticism']


Note :
The Reset34Model was inspired from the personality_traits prediciton model developed by ankit2saxena [github=(https://github.com/ankit2saxena/deep_learning)]
because of less avaliability of training data images and videos the prediction of the personality traits may get disturbed but however it works considerably)
and the model parameters can be improved furtger with proper training dataset adding to the model.

______________________________________THANK YOU________________________________________

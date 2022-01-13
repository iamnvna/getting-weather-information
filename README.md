### Project Three - 100DaysofCode
# Getting Weather Information
This is a simple program that collects an input, *city name*, from a user and returns a json file that is formatted as a tree. This program makes use of the **Open Weather Map API Key**. The user input is passed through the API and the responds printed out.

## Background
This project is part of my #100DaysOfCode learning streak. I intend to write a simple python program each day. Each project would:
* be heavily commented for learning purposes;
* include a README file similar to this one;
* include an algorithm to solve it without code;
* include a summary of what I learnt.

## Algorithm
1. Start.
2. Import required library(s). *requests* and *pprint* in this program.
3. Create a variable to hold the API Key obtained.
4. Create a variable to collect the city name from the user.
5. Create a variable to hold the *base url* of the API call, appended with the API Key variable, and the user input. Read the documentation [here](https://openweathermap.org/) to gain more insight into this step.
6. Pass the *base url* (now complete) through the *requests* library to connect to the API.
7. Print the output through the *pprint* library.
9. Stop.

## What I've learnt
* This is the first program that put my knowledge on APi to the test. I've had a good sense of how to use API's practically.
* I also learnt about the pprint (PrettyPrinter) library today. In this program, it helped format the json file into readable text, though still in json. 
* I am getting used to the *requests* library and it's scope after using it twice now. 
* Edit: The APi Key used in this program is public and visible, after pushing the final local repository, I got an email from GitGaurdian alerting me of sensitive data pushed to my public GitHub. I'll keep this alive, but I'll find ways to keep sensitive data out of the public domain for future projects. 

For more understanding, watch the full tutorial **[here](https://youtu.be/SqvVm3QiQVk?t=1494)** from freeCodeCamp.org

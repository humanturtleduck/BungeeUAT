# BungeeUAT

![image](https://github.com/user-attachments/assets/d827d65b-f7be-4f89-85d9-87aaea24a02c)

Train a neural network with your drop data to use the Universal Approximation Theorem(UAT) and get up to centimeter accuracy for BOTH partially elastic and fully elastic cords. You are able to generate dummy data(uses fully elastic equation from wiki) to test out the approximator(see images below.) You can tune multiple variables to get more accurate data such as noise, number of neurons/hidden layers, number of testing epochs. The most important factor is the amount of data you collect, which itself helps fine tune. DM @itscalledsoccer_ on discord if the UI is confusing, if you have issues, if there are bugs/suggestions. I will NOT give out optimal tuning parameters, you should find them yourself. Please don't sell/trade access to this github repo/releases. The graphs should suffice for tuning purposes. Please backup your data before feeding it. Unfortunately, this only works for windows 10/11. PLEASE DOWNLOAD THE LATEST RELEASE, THE CODE IN THE GITHUB CODE IS OUTDATED. You can do bro a favor by submitting a pull request, I'll just accept them bc im lazy to update the repo.

![image](https://github.com/user-attachments/assets/adfbeb18-0651-4048-b45c-33807ee1750a)
![image](https://github.com/user-attachments/assets/3bce4505-db5c-4fee-937b-d561613cac43)

As you can see, the nn didn't completely fit the data, this is normal and you can overcome this by tuning the parameters. ONCE THIS IS SMOOTH AND THE MEAN ABSOLUTE ERROR IS LOW, YOU ARE GOOD.

## How to use

![image](https://github.com/user-attachments/assets/1e27e0c2-9116-4f6b-ab47-f8d0965c51a8)


This is the UI that I(poorly) made. I will explain the use of each button and textbox.

- Number of training epochs is the how many cycles the network learns for
- Number of random data points is for generating dummy data, you need to press generate data to make it. It will override any data you inputted
- You can input your data using the button input data
- you can press output data to see the estimates
- Duplicates, shape, scale, and sigma are parameters for noise (gaussian and gamma). Figure out how they work ig

## How to set up layers

You can experiment with the number of hidden layers and number of neurons in each layer. The input layer will always hava 2 neurons, output layer will always have 1 neuron. I will give a few examples of possible configurations, but its not limiting.


![image](https://github.com/user-attachments/assets/64d16b89-418a-43d7-a96b-6492297bc775)

This would be:
![image](https://github.com/user-attachments/assets/75d3c8a8-a2d3-40d2-b997-086351947e48)
This is because the first hidden layer has 5 neurons, the second has 3.

the cover would be 16 16 16 8, with all 4 numbers being on a separate line. I truly hate markdown.

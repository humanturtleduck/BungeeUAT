# BungeeUAT

![image](https://github.com/user-attachments/assets/d827d65b-f7be-4f89-85d9-87aaea24a02c)

Train a neural network with your drop data to use the Universal Approximation Theorem(UAT) and get up to centimeter accuracy for BOTH partially elastic and fully elastic cords. You are able to generate dummy data(uses fully elastic equation from wiki) to test out the approximator(see images below.) You can tune multiple variables to get more accurate data such as noise, number of neurons/hidden layers, number of testing epochs. The most important factor is the amount of data you collect, which itself helps fine tune. DM @itscalledsoccer_ on discord if the UI is confusing, if you have issues, if there are bugs/suggestions. I will NOT give out optimal tuning parameters, you should find them yourself. Please don't sell/trade access to this github repo/releases. The graphs should suffice for tuning purposes. Please backup your data before feeding it. Unfortunately, this only works for windows 10/11. PLEASE DOWNLOAD THE LATEST RELEASE, THE CODE IN THE GITHUB CODE IS OUTDATED. You can do bro a favor by submitting a pull request, I'll just accept them bc im lazy to update the repo.

![image](https://github.com/user-attachments/assets/adfbeb18-0651-4048-b45c-33807ee1750a)
![image](https://github.com/user-attachments/assets/3bce4505-db5c-4fee-937b-d561613cac43)

As you can see, the nn didn't completely fit the data, this is normal and you can overcome this by tuning the parameters.

![image](https://github.com/user-attachments/assets/7171c630-11d3-4c4f-ac00-68a7bf582af8)

This is the UI that I(poorly) made. the first textbox(top left) has the number of epochs. The second one(top right) has the number of dummy data points. You should press generate data before training off of this set. The training button also 

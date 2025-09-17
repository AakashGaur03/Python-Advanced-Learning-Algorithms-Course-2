# Commonly by far there are three Activation Functions 

# Refer to Image 1
# g(z) = 

# 1) Sigmoid = 1/(1+(e^-z))

# 2) ReLU Rectified Lienar Unit = max(0,z)

# 3) Linear Activation Function / No Activation Function = z

# 4) Softmax Activation (We will cover this later)


# Refer to Image 2
# How to choose Activation Function

#  There are high chance we get to know activation funciton acc to the output y

# In Binary Classification Problem, almost every case sigmoid funciton

# Regression Problem 
# How stock price will change in upcomiing time so it can be either positive or negative 
# so Linear Activation Function

# if y can take only non negative value 
# Like predicting price of house 
# Then we use ReLU Rectified Linear Unit



# Refer to Image 3
# In hidden layers most common choice is ReLU

# why so because ReLU is faster than sigmoid as it just need max of 0 and z and sigmoid needs computation that is
# exponentiation then a inverse and ...

# In sigmoid it goes flat on both sides
# in ReLU it goes flat on one side only that is 0

# Refer to Image 4
# Summary of above


## NOTE there are others activaiton functions too such as tan h or LeakyReLU that we will learn on the go


# Why do we need Activation Function
# In cases when we apply linear activation Function that is no activation funciton even our model
# is going through multiple hidden layers it just gives same output as of linear regression model
# refer to Image 5 and 6
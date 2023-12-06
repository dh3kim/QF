import random
import numpy as np

def sigmoid(z):
    return 1/(1 + np.exp(-z))

def Training(X, y, learning_rate, num_iter):
    NCols, NRows = X.shape
    # weights of hidden layer (Wh) and output (Wo)
    W_hidden = np.random.normal(0, 1, NRows)
    W_out = np.random.normal(0, 1, 1)
    print('')
    print('TRAINING:')
    for iter in range(num_iter):
        # hypothesis and loss function
        hypothesis = sigmoid( W_out * sigmoid(np.matmul(X,W_hidden)))
        loss = np.sum(-y * np.log(hypothesis) - (1 - y) * np.log(1 - hypothesis))
        # update: derivative of the loss function
        dWh = (1/NCols) * W_out * np.matmul(X.T, (hypothesis - y))
        dWo = (1/NCols) * np.dot(W_hidden, np.matmul(X.T, (hypothesis - y)))
        W_hidden -= learning_rate * dWh
        W_out -= learning_rate * dWo
        if iter % 200 == 0:
            print(iter, loss)
    return W_hidden, W_out

def Prediction(X, W_hidden, W_out):
    hypothesis = sigmoid( W_out * np.matmul(X,W_hidden))
    NObs = len(hypothesis)
    y_pred = [None] * NObs
    for i in range(len(hypothesis)):
        if hypothesis[i] > 0.5:
            y_pred[i] = 1
        else:
            y_pred[i] = 0
    return y_pred

def Accuracy(y_pred, y):
    return np.sum(y == y_pred) / len(y)

def main():
    # data
    NObs = 500
    x1 = [None]*NObs ; x2 = [None]*NObs ; y = [None]*NObs
    sum_y = 0
    for i in range(NObs):
        x1[i] = random.random()*10
        x2[i] = random.random()*50
        y_temp = 100 + 5 * x1[i] + (-3) * x2[i] 
        y[i] = y_temp + random.gauss(0,1)
        sum_y += y[i]
       
    for i in range(NObs):
        if y[i] < sum_y/NObs:
            y[i] = 0
        else:
            y[i] = 1
 
    y = np.array(y)
    X = np.array(list(zip(x1,x2)))
    # include bias of ones
    ones = np.ones((NObs,1))
    X = np.hstack((ones,X)) 
    
    # TRAINING
    Wh, Wo = Training(X, y, 0.001, 3000)
    y_hat = Prediction(X, Wh, Wo)
    print('\nAccuracy', Accuracy(y_hat, y))
    
if __name__ == "__main__":
    main()






# Basic 1-layer ANN
import random
import numpy as np

def sigmoid(z):
    return 1/(1 + np.exp(-z))

def Training(X, y, learning_rate, num_iter):
    # initialization of W
    # NRows = NFeatures + 1
    NCols, NRows = X.shape
    W = np.random.normal(0, 1, NRows)
    print('')
    print('TRAINING:')
    print('STEP, LOSS')
    for iter in range(num_iter):
        # hypothesis
        hypothesis = sigmoid(np.matmul(X,W))
        # loss function
        loss = np.sum(-y * np.log(hypothesis) - (1 - y) * np.log(1 - hypothesis))
        # update 
        # derivative of the loss function
        dW = (1/NCols) * np.matmul(X.T, (hypothesis - y))
        W -= learning_rate * dW
        if iter % 200 == 0:
            print(iter, loss)
    return W

def Prediction(X, W):
    hypothesis = sigmoid(np.matmul(X,W))
    NObs = len(hypothesis)
    y_pred = [None] * NObs
    for i in range(len(hypothesis)):
        if hypothesis[i] > 0.5:
            y_pred[i] = 1
        else:
            y_pred[i] = 0
    return y_pred

def Accuracy(y_pred, y):
    print('')
    #print('y, predicted y')
    #for i in range(len(y)):
    #    print(y[i], y_pred[i])
    return np.sum(y == y_pred) / len(y)

def main():
    # (PART 1): data generated using random number generators
    NObs = 100
    x1 = [None]*NObs
    x2 = [None]*NObs
    y = [None]*NObs
    random.seed(510)
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
    
    #print('DATA:')
    #for i in range(7):
    #    print(round(x1[i],2), round(x2[i],2), y[i])
        
    y = np.array(y)
    X = np.array(list(zip(x1,x2)))
    # include bias of ones
    ones = np.ones((NObs,1))
    X = np.hstack((ones,X)) 
    
    # (PART 2) TRAINING
    W = Training(X, y, 0.0001, 5000)
    y_hat = Prediction(X, W)
    print('Accuracy', Accuracy(y_hat, y))
    
if __name__ == "__main__":
    main()


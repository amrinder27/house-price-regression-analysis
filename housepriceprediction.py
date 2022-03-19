import numpy as np
import numpy.random as rnd

# Read the data
# Download "data.csv" from the course website
data = np.genfromtxt('data.csv', delimiter=',', skip_header=1)

# Display the *shape* of the data matrix
print(data.shape)

# Please leave these print statements, to help your TAs grade quickly.
print('\n\nQuestion 1')
print('----------')

print('\nQuestion 1(a):') # Please leave print statements like these

#print('\nFirst column and the first 10 rows of the data')
print(data[0:10,0])

print('\nQuestion 1(b):')

#print('\nSecond column and the first 10 rows of the data')
print(data[0:10,1])


# Include your response in your writeup

print('\nQuestion 1(d):')

data = data[:, 1: ]

#print('\nShape of data')
print(data.shape)

test = data[data[:, 0] > 2013.417]
# Include your response in your writeup

print('\nQuestion 1(f):')


train_valid = data[data[:, 0] <= 2013.417]

#print('\nShape of test')
print(test.shape)

#print('\nShape of train_valid')
print(train_valid.shape)

print('\nQuestion 1(g):')

# Below array was generated by calling
# randarray = rnd.randint(0, 5, train_valid.shape[0])
# Do NOT uncomment the above line of code. Instead, we are including
# the values you should use below.
randarray = np.array([2, 0, 1, 3, 0, 0, 0, 3, 2, 3, 1, 1, 2, 0, 4, 4, 0, 2, 1, 2, 2, 2,
                      4, 1, 3, 2, 0, 1, 2, 0, 3, 0, 3, 1, 3, 0, 4, 1, 4, 4, 0, 0, 1, 2,
                      4, 0, 0, 1, 1, 1, 2, 3, 4, 4, 3, 3, 0, 0, 0, 0, 2, 2, 3, 0, 0, 1,
                      4, 1, 4, 2, 2, 4, 4, 2, 0, 4, 0, 3, 2, 0, 4, 3, 1, 1, 0, 0, 0, 0,
                      1, 1, 4, 0, 3, 4, 2, 0, 0, 4, 4, 4, 4, 3, 3, 0, 0, 2, 2, 1, 3, 2,
                      4, 1, 2, 2, 3, 4, 1, 4, 3, 1, 1, 3, 0, 4, 4, 4, 0, 3, 3, 0, 4, 0,
                      0, 4, 3, 4, 1, 2, 2, 4, 4, 1, 2, 1, 1, 0, 4, 4, 4, 2, 0, 4, 2, 0,
                      4, 4, 1, 4, 0, 4, 0, 0, 1, 4, 3, 2, 4, 3, 1, 4, 1, 3, 4, 1, 0, 0,
                      4, 4, 2, 0, 4, 4, 4, 2, 3, 3, 4, 1, 0, 1, 2, 3, 1, 0, 1, 3, 4, 0,
                      0, 1, 2, 2, 2, 2, 4, 3, 1, 1, 4, 4, 1, 4, 2, 4, 0, 2, 4, 1, 3, 0,
                      4, 2, 3, 0, 4, 2, 3, 2, 2, 0, 2, 0, 2, 3, 2, 3, 4, 2, 4, 2, 2, 4,
                      3, 4, 0, 4, 4, 0, 1, 4, 2, 4, 2, 4, 0, 3, 4, 2, 1, 1, 3, 0, 1, 0,
                      3, 1, 3, 2, 4, 3, 1, 3, 0, 3, 0, 4, 2, 1, 2, 3, 2, 2, 4, 1, 4, 2,
                      1, 3, 1, 2, 2, 3, 1, 4, 2, 2, 4, 4, 1, 3, 2, 4, 1, 2, 4, 4, 0, 3,
                      1, 2, 1, 3, 3, 3, 2, 1, 3, 0, 2, 4, 2, 0, 3, 1, 0, 4, 2, 4, 1, 0,
                      4, 2, 2, 0, 1, 4, 3, 4, 0, 3, 2, 0, 2, 0])


train = train_valid[randarray[0:] != 0]
valid = train_valid[randarray[0:] == 0]


#print('\nShape of train')
print(train.shape)

#print('\nShape of valid')
print(valid.shape)


print('\nQuestion 1(h):')

train_x = train[0: ,1:6]
train_t = train[0: ,6]
valid_x = valid[0: ,1:6]
valid_t = valid[0: ,6]
test_x = test[0: ,1:6]
test_t = test[0: ,6]


#print('\nFirst 2 rows of train_x')
print(train_x[:2])

#print('\nFirst 2 rows of train_t')
print(train_t[:2]) 

#print('\nFirst 2 rows of valid_x')
print(valid_x[:2])

#print('\nFirst 2 rows of valid_t')
print(valid_t[:2])

#print('\nFirst 2 rows of test_x')
print(test_x[:2])

#print('\nFirst 2 rows of test_t')
print(test_t[:2])


print('\nQuestion 1(i):')

#print('\nMean of each column in data')
print(np.mean(data, axis=0))

#print('\nStandard deviation of each column in data')
print(np.std(data, axis=0))


x_mean = np.mean(train_x, axis=0)
x_std = np.std(train_x, axis=0)

#print('\nMean of each column in train_x')
print(x_mean)

#print('\nStandard deviation of each column in train_x')
print(x_std)



# Include your response in your writeup

# Include your response in your writeup

print('\nQuestion 1(l):')

tmp_a = np.array([[1.4, 2.5, 3.0], [9.1, 3.4, 2.3]])
tmp_b = np.sum(tmp_a, axis=0)
print(tmp_a)
print(tmp_b)
print(tmp_a - tmp_b)

# Include your response in your writeup

print('\nQuestion 1(m):')
norm_train_x = (train_x - x_mean) / x_std

#print('\nFirst 2 rows of norm_train_x')
print(norm_train_x[:2])

#print('\nMean and STD of the columns of norm_train_x')
print(np.mean(norm_train_x, axis=0))
#print(np.std(norm_train_x, axis=0))


print('\nQuestion 1(n):')
import time
nonvec_before = time.time()
for i in range(1000):
    norm_train_x_loop = np.zeros_like(train_x)
    for i in range(train_x.shape[0]):
        for j in range(train_x.shape[1]):
            norm_train_x_loop = (train_x[i, j] - x_mean[j]) / x_std[j]

nonvec_after = time.time()
print("Non-vectorized time: ", nonvec_after - nonvec_before)


vec_before = time.time()

for i in range(1000):
    norm_train_x = (train_x - x_mean) / x_std
vec_after = time.time()
print("Vectorized time: ", vec_after - vec_before)


# Include your response in your writeup




















# Please leave these print statements, to help your TAs grade quickly.
print('\n\nQuestion 2')
print('----------')
print('\nQuestion 2(a):')

v = valid_x[0] # should be np.array([ 19.5    , 306.5947 ,   9.     ,  24.98034, 121.53951])

#Calculate euclidean distances(not sqaure rooted)
distances = np.sum(np.power(train_x[:] - v, 2), axis=1)
dist_sorted_index = np.argsort(distances)
n = dist_sorted_index[0]

#print('\nFirst 10 rows of distances')
print(distances[0: 10])

#print('\ntrain_x[n]')
print(train_x[n])

#print('\ntrain_t[n]')
print(train_t[n])


print('\nQuestion 2(b):')
#Compute 3NN for training data set with vector 
three_nn = np.mean(train_t[dist_sorted_index[0:3]])
print(three_nn)


print('\nQuestion 2(c):')

def unnorm_knn(v, k, features=train_x, labels=train_t):
    """
    Returns the k Nearest Neighbour prediction of housing prices for an input
    vector v.

    Parameters:
        v - The input vector to make predictions for
        k - The hyperparameter "k" in kNN
        features - The input features of the training data; a numpy array of shape [N, D]
                   (By default, `train_x` is used)
        labels - The target labels of the training data; a numpy array of shape [N]
                 (By default, `train_t` is used)
    """
    #Calculate euclidean distances
    distances = np.sum(np.power(v - features[:], 2), axis=1)
    #Sort distance indexes
    dist_sorted_index = np.argsort(distances)
    #Return KNN
    return np.mean(labels[dist_sorted_index[0:k]])
    

print(unnorm_knn(v=valid_x[1], k=5))



print('\nQuestion 2(d):')
def compute_mse(predict, data_x=valid_x, data_t=valid_t):
    """
    Returns the Mean Squared Error of a model across a dataset

    Parameters:
        predict - A Python *function* that takes an input vector and produces a
                  prediction for that vector.
        data_x - The input features of the data set to make predictions for
                 (By default, `valid_x` is used)
        data_t - The target labels of the dataset to make predictions for 
                 (By default, `train_t` is used)
    """
    errors = []
    for i in range(data_t.shape[0]):
        #Compute difference between actual and predicted label
        error = (predict(data_x[i]) - data_t[i])**2
        errors.append(error) 
    return np.mean(errors)

def baseline(v):
    """
    Returns the average housing price given an input vector v.
    """
    return np.mean(train_t)

# compute and print the training and validation MSE
print(compute_mse(baseline, data_x=train_x, data_t=train_t))
print(compute_mse(baseline, data_x=valid_x, data_t=valid_t))

print('\nQuestion 2(e):')

train_mse = []
valid_mse = []
for k in range(1, 31):
    # create a temporary function `predict_fn` that computes the knn
    # prediction for the current value of the loop variable `k`
    def predict_fn(new_v):
        return unnorm_knn(new_v, k)

    # compute the training and validation MSE for this kNN model
    mse = compute_mse(predict_fn, data_x=train_x, data_t=train_t)
    train_mse.append(mse)
    mse = compute_mse(predict_fn, data_x=valid_x, data_t=valid_t)
    valid_mse.append(mse)


from matplotlib import pyplot as plt
plt.plot(range(1, 31), train_mse)
plt.plot(range(1, 31), valid_mse)
plt.xlabel("k")
plt.ylabel("MSE")
plt.title("Unnormalized kNN")
plt.legend(["Training", "Validation"])
plt.show()

#print('\ntrain_mse')
print(train_mse)

#print('\nvalid_mse')
print(valid_mse)
# Include your response in your writeup

print('\nQuestion 2(f):')

def norm_knn(v, k, features=norm_train_x, means=x_mean, stds=x_std, labels=train_t):
    """
    Returns the k Nearest Neighbour prediction of housing prices for an input
    vector v.

    Parameters:
        v - The input vector to make predictions for
        k - The hyperparameter "k" in kNN
        features - The normalized input features of the training data
                   (By default, `norm_train_x` is used)
        means - The means over the training data (By default, `x_mean` is used)
        stds - The standard deviations of the training data (By default, `x_std` is used)
        labels - The target labels of the training data; a numpy array of shape [N]
                 (By default, `train_t` is used)
    """
    #normalize vector v in terms of features data
    v_norm = (v - means) / stds
    #Calculate distances
    distances = np.sum(np.power(features[:] - v_norm, 2), axis=1)
    #Sort distance indexes
    dist_sorted_index = np.argsort(distances)
    #return knn
    return np.mean(labels[dist_sorted_index[0:k]])
    
    

train_mse = []
valid_mse = []
for k in range(1, 31):
    # create a temporary function `predict_fn` that computes the knn
    # prediction for the current value of the loop variable `k`
    def predict_fn(new_v):
        return norm_knn(new_v, k)

    # compute the training and validation MSE for this kNN model
    mse = compute_mse(predict_fn, data_x=train_x, data_t=train_t)
    train_mse.append(mse)
    mse = compute_mse(predict_fn, data_x=valid_x, data_t=valid_t)
    valid_mse.append(mse)
    
#print('\ntrain_mse_norm')
print(train_mse)

#print('\nvalid_mse_norm')
print(valid_mse)

#Plot MSE for normalized KNN
from matplotlib import pyplot as plt
plt.plot(range(1, 31), train_mse)
plt.plot(range(1, 31), valid_mse)
plt.xlabel("k")
plt.ylabel("MSE")
plt.title("Normalized kNN")
plt.legend(["Training", "Validation"])
plt.show()

# Include your response in your writeup

# Include your response in your writeup

# Include your response in your writeup

# Include your response in your writeup

















# Please leave these print statements, to help your TAs grade quickly.

print('\n\nQuestion 3')
print('----------')

train_d = train_x[:, 0] # house age

# Plot this feature against the target (house price)
plt.scatter(train_d, train_t)
plt.xlabel("House Age")
plt.ylabel("House Price")
plt.title("House Age vs. Price")
plt.show()

print('\nQuestion 3(a):')

#Create design matrix for linear polynomal regression
ones = np.ones(train_d.shape[0])
X = np.stack((ones, train_d), axis=-1)

#Compute weights for linear polynomal regression
linear_coef = np.matmul(np.linalg.inv(np.matmul(X.T,X)), np.matmul(X.T,train_t[:]))
print(linear_coef)

def pred_linear(v, coef=linear_coef):
    """
    Returns the linear regression predictions of house prices, given
    a vector consisting of the ages of several houses that we would
    like to make predictions for.

    Parameters:
        v - A vector of house ages
        coef - The linear regression coefficient
    """
    return (coef[1]*v) + coef[0]

def plot_prediction(predict, title):
    """
    Display a plot that superimposes the model predictions on a scatter
    plot of the training data (train_d, train_t)

    Parameters:
        predict - A Python *function* that takes an input vector and produces a
                  prediction for that vector.
        title - A title to display on the figure.
    """
    # start with a scatter plot
    plt.scatter(train_d, train_t)

    # create several "house age" values to make predictions for
    min_age = np.min(train_d)
    max_age = np.max(train_d)
    v = np.arange(min_age, max_age, 0.1)
    
    # make predictions for those values
    y = predict(v)

    # plot the result
    plt.plot(v, y)
    plt.title(title)
    plt.xlabel("House Age")
    plt.ylabel("House Price")
    plt.show()

#Create plot for linear polynomial regression
plot_prediction(pred_linear, title="Linear Regression (no feature expansion)")

print('\nQuestion 3(c):')

def compute_mse_vectorized(predict, data_x=valid_x, data_t=valid_t):
    """
    Returns the Mean Squared Error of a model across a dataset

    Parameters:
        predict - A Python *function* that takes a vector of house ages, 
                  and produces a vector of house price predictions
        data_x - The input features of the data set to make predictions for
                 (By default, `valid_x` is used)
        data_t - The target labels of the dataset to make predictions for 
                 (By default, `valid_t` is used)
    """
    v = data_x[:, 0] # house age
    mse = np.square(predict(v) - data_t[:]).mean()
    return mse


print('\nQuestion 3(d):')
#Create design matrix for quadratic polynomial regression
ones = np.ones(train_d.shape[0])
train_d_sqr = np.square(train_d)
X = np.stack((ones, train_d, train_d_sqr), axis=-1)

#Compute weights for quadratic polynomial regression
quad_coef = np.matmul(np.linalg.inv(np.matmul(X.T,X)), np.matmul(X.T,train_t[:]))

print(quad_coef)


def pred_quad(v, coef=quad_coef):
    """
    Returns the degree 2 polynomial regression predictions of
    house prices, given a vector consisting of the ages of several houses
    that we would like to make predictions for.

    Parameters:
        v - A vector of house ages
        coef - The linear regression coefficient
    """
    
    v_sqr = np.square(v)
    return (coef[2]*v_sqr) + (coef[1]*v) + coef[0]

#Create plot for quadratic polynomial regression
plot_prediction(pred_quad, title="Polynomial Regression (M=2)")

print('\nQuestion 3(f):')

#Compute training set MSE for quadratic polynomial regression
mse_train = compute_mse_vectorized(pred_quad, data_x=train_x, data_t=train_t)
#print('\nTraining MSE')
print(mse_train)

#Compute validation set MSE for quadratic polynomial regression
mse_valid = compute_mse_vectorized(pred_quad)
#print('\nValidation MSE')
print(mse_valid)



print('\nQuestion 3(g):')


def vector_multinomial(v, M):
    """
    Return design matrix for polynomial regression with M dimension
    
    Parameters
    ----------
    v : input vector(N)
    M : dimension size

    Returns
    -------
    X : design matrix(N,M+1)

    """
    X = np.ones((v.shape[0],1))
    
    for i in range(0,M):
        pwr = np.power(v, i + 1)
        pwr.shape = (v.shape[0],1)
        X = np.concatenate((X, pwr), axis=1)
        
    return X


train_mse_r = []
valid_mse_r = []


for M in range(0, 11):

    #Compute design matrix X
    X = vector_multinomial(train_d, M)
    #Compute weights for polynomial regression function
    coef = np.matmul(np.linalg.inv(np.matmul(X.T,X)), np.matmul(X.T,train_t[:]))
    
    #Compute prediction given inputs v and coefficents c
    def predict(v, c= coef):
        v = vector_multinomial(v, M)
        
        pred = np.dot(v, c.T)
        return pred
    
    #Compute validation set MSE
    mse_valid = compute_mse_vectorized(predict)
    #Compute training set MSE
    mse_train = compute_mse_vectorized(predict, data_x=train_x, data_t=train_t)
    
    train_mse_r.append(mse_train) 
    valid_mse_r.append(mse_valid)
    

#print('\ntrain_msr_r')
print(train_mse_r)
#print('\nvalid_msr_r')
print(valid_mse_r)


# Include your response in your writeup

plt.plot(range(0, 11), train_mse_r)
plt.plot(range(0, 11), valid_mse_r)
plt.xlabel("Polynomial Degree")
plt.ylabel("MSE")
plt.title("Polynomial Regression")
plt.legend(["Training", "Validation"])
plt.show()

# Include your response in your writeup

for M in range(3, 11):
    
    #Compute design matrix X
    X = vector_multinomial(train_d, M)
    #Compute weights for polynomial regression function
    coef = np.matmul(np.linalg.inv(np.matmul(X.T,X)), np.matmul(X.T,train_t[:]))
    
    #Compute prediction given inputs v and coefficents c
    def predict(v, c= coef):
        v = vector_multinomial(v, M)
        
        pred = np.dot(v, c.T)
        return pred
    
    #Create plot of polynomial regression with M
    plot_prediction(predict, title="Polynomial Regression (M=%d)" % M)
        

# Include your response in your writeup

# Include your response in your writeup

# Include your response in your writeup

# Include your response in your writeup

# Include your response in your writeup

# Include your response in your writeup

# Include your response in your writeup
















# Please leave these print statements, to help your TAs grade quickly.

print('\n\nQuestion 4')
print('----------')
print('\nQuestion 4(e):')

def grad(weight, X, t):
    '''
    Return gradient of each weight evaluated at the current value

    Parameters:
        `weight` - a current "guess" of what our weights should be,
                   a numpy array of shape (D)
        `X` - matrix of shape (N,D) of input features
        `t` - target y values of shape (N)

    '''
    #Number of data points in data set
    n = X.shape[0]
    
    #Compute vector of prediction Y
    predict_y = np.matmul(X, weight.T)
    
    #Compute error vector Y-t
    error = predict_y - t
    
    #Return gradient vector
    return np.matmul(error, X) / n



# Please leave this print statement for grading:
print(grad(np.array([1]), np.array([[1], [1]]), np.array([2, 2])))


# Include your response in your writeup


print('\nQuestion 4(f):')

#Define inputs
w = np.array([1.0, 0.0])
X = np.array([[1,2], [1,2]])
t = np.array([2, 2])

#Gradient vector using grad function for input values w, X, t
print(grad(w, X, t))

#Gradient vector approximation using finite difference rule
grad_approx = []
h = 0.001
N = X.shape[0]
for i in range(0,w.shape[0]):
    #Compute f(x)
    pred = np.matmul(X, w.T)
    error = np.square(pred - t)
    f = np.sum(error) / (2*N)
    
    #Compute f(x+h)
    w_copy = np.copy(w)
    x = w[i] + h
    w_copy[i] = x
    pred = np.matmul(X, w_copy.T)
    error = np.square(pred - t)
    f_h = np.sum(error) / (2*N)
    
    #Compute [f(x+h)-f(x)] / h for weight w_i
    approx = (f_h - f)/h
    grad_approx.append(approx)
    

#Print gradient vector approximation using finite difference rule
print(grad_approx)
    

print('\nQuestion 4(g):')

def solve_via_gradient_descent(M, alpha=0.0025, niter=10000):
    '''
    Given `M` - maximum degree of the polynomial regression model
          `alpha` - the learning rate
          `niter` - the number of iterations of gradient descent to run
    Solves for linear regression weights.
    Return weights after `niter` iterations.
    '''
    #Initialize all the weights to zeros
    w = np.zeros([M + 1])

    train_d = train_x[:, 0] # house age
    
    #Construct the design matrix
    X = vector_multinomial(train_d, M)
    
    #Compute and update weights using grad function for niter iterations
    for i in range(niter):
        
        gradient = grad(w, X, train_t[:])
        w = w - alpha*gradient
    return w

print(solve_via_gradient_descent(M=1, alpha=0.0025, niter=10000))

# Include your response in your writeup

print('\nQuestion 4(i):')
print(solve_via_gradient_descent(M=1, alpha=0.01, niter=50))



print('\n\nQuestion 5')
print('----------')

# Include your response in your writeup

print('\nQuestion 5(b):')

#Number of data point 
n = train_valid.shape[0]

#Number of data points per fold for 5-fold CV
fold_size = round(n/5)

#List of average MSE for each k in range 1-30
cv_avgs = []

for k in range(1,31):
    total = 0
    for L in range(0,5):
        #print(L*fold_size,(L+1)*fold_size)
        #Validation Set for fold
        v = train_valid[L*fold_size:(L+1)*fold_size,:]
        #print(v.shape)
        
        #Training set for fold
        t = np.concatenate((train_valid[0:L*fold_size,:], train_valid[(L+1)*fold_size:,:]), axis=0)
        #print(t.shape)
        
        #Seperate training and validation sets by features and labels
        t_x = t[0: ,1:6]
        t_t = t[0: ,6]
        v_x = v[0: ,1:6]
        v_t = v[0: ,6]
        #print(train_x.shape, train_t.shape, valid_x.shape, valid_t.shape)
        
        #Compute unnormalized KNN prediction
        def predict_fn(new_v):
            return unnorm_knn(new_v, k, features=t_x, labels=t_t)
    
        #Compute and add validation set MSE to total
        total += compute_mse(predict_fn, data_x=v_x, data_t=v_t)
        
    #Compute average MSE for validation set for given k in KNN
    cv_avgs.append(total/5)
    

#print(cv_avgs)
    

#Create plot for 
from matplotlib import pyplot as plt
plt.plot(range(1, 31), cv_avgs)
plt.xlabel("K")
plt.ylabel("Average Validation MSE")
plt.title(" 5-fold cross validation on the unnormalized kNN model")
plt.legend(["Validation"])
plt.axis([None, None, 0, 100])
plt.show()

# Include your response in your writeup

# Include your response in your writeup

print('\nQuestion 5(e):')
#Compute and print test set MSE for optimal model
def predict_unnorm(new_v):
        return unnorm_knn(new_v, 6)
        
    
print(compute_mse(predict_unnorm, data_x=test_x, data_t=test_t))



# Include your response in your writeup



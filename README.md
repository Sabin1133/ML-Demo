##### Copyright 2023 Padurariu Sabin

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━┏━━━┓┏━━━┓┏━━━┓┏━━━┓━━━┏━┓┏━┓┏━━━┓━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━┃┏━┓┃┃┏━━┛┃┏━┓┃┗┓┏┓┃━━━┃┃┗┛┃┃┃┏━━┛━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━┃┗━┛┃┃┗━━┓┃┃━┃┃━┃┃┃┃━━━┃┏┓┏┓┃┃┗━━┓━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━┃┏┓┏┛┃┏━━┛┃┗━┛┃━┃┃┃┃━━━┃┃┃┃┃┃┃┏━━┛━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━┃┃┃┗┓┃┗━━┓┃┏━┓┃┏┛┗┛┃━━━┃┃┃┃┃┃┃┗━━┓━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━┗┛┗━┛┗━━━┛┗┛━┗┛┗━━━┛━━━┗┛┗┛┗┛┗━━━┛━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# **Numerical Methods Homework 1**

## **Task 1 - Markov is coming**


This collection of functions can be used to determine, using an euristic
algorithm, the path from a random spot in a labyrinth to one of the given 
exits using markov chains and iterative numerical analysis methods.

### Functions
```
function [Labyrinth] = parse_labyrinth(file_path)
```
* used to parse a txt file for get a labyrinth
```
function [Adj] = get_adjacency_matrix(Labyrinth)
```
* used to create the adjacency matrix for the given Labyrinth
```
function [Link] = get_link_matrix(Labyrinth)
```
* used to create the link matrix for the given Labyrinth, 
containing probabilities
```
function [G, c] = get_Jacobi_parameters(Link)
```
* used to extract the required matrices for the iterative method
```
function [x, err, steps] = perform_iterative(G, c, x0, tol, max_steps)
```
* used to perform Jacobi and compute the x vector with a certain precision
```
function [path] = heuristic_greedy(start_position, x, Adj)
```
* used to compute the path to the exit from the random spot
```
function [decoded_path] = decode_path(path, lines, cols)
```
* used to decode the path based on the labyrinth dimensions


<br>

## **Task 2 - Linear Regression**

This collection of functions provides some of the basic methods and
functionality . It requires an initial dataset in order to train the model and 
can predict the price of a future 
apartment based on the previously provided data.

The package includes:
* csv file parsing function
* txt file parsing function, 
* two functions to compute the error/cost
* two functions to train the model

### Functions
```
function [Y, InitialMatrix] = parse_data_set_file(file_path)
```
* used to parse a txt file to extract the results and training examples
```
function [Y, InitialMatrix] = parse_csv_file(file_path)
```
* used to parse a csv file to extract the results and training examples
```
function [FeatureMatrix] = prepare_for_regression(InitialMatrix)
```
* used to create the matrix by converting all strings to their 
corresponding values
    * yes - 1
    * no - 0
    * semi-furnished - 1, 0
    * unfurnished - 0, 1
    * furnished - 0, 0
```
function [Theta] = gradient_descent(FeatureMatrix, Y, n, m, alpha, iter)
```
* used to train the predictors/weights based on the provided dataset using the
gradient descent formula
```
function [Theta] = normal_equation(FeatureMatrix, Y, tol, iter)
```
* used to train the predictors/weights based on the provided dataset using the
conjugate gradient formula
```
function [Error] = linear_regression_cost_function(Theta, Y, FeatureMatrix)
```
* used to compute the error/cost of the current weights
```
function [Error] = lasso_regression_cost_function(Theta, Y, FeatureMatrix, lambda)
```
* used to compute the error/cost of the current weights using lasso formula
```
function [Error] = ridge_regression_cost_function(Theta, Y, FeatureMatrix, lambda)
```
* used to compute the error/cost of the current weights using ridge formula


<br>

## **Task 3 - MNIST 101**

This collection of functions provides the required tools to train a very basic 
"AI" model to recognise hand-written digits, the popular MNIST. It also
includes a function wich was provided by someone in order to compute some
additional required parameters.

## Functions
```
function [X, y] = load_dataset(file_path)
```
* loads the training examples and results into memory
```
function [X_train, y_train, X_test, y_test] = split_dataset(X, y, percent)
```
* used to randomly split a given collection of training examples into actual 
training samples and test samples
```
function [matrix] = initialize_weight(L_prev, L_next)
```
* used to create a matrix of initial weights for a certain neuron layer
```
function [theta1, theta2] = extract_matrices(weights, input_layer_size, hidden_layer_size, output_layer_size)
```
* used to create the transition matrices using the given weights
```
function [grad, J] = cost_function(params, X, y, lambda, input_layer_size, hidden_layer_size, output_layer_size)
```
* used to compute the error/cost of the current weights and perform 
backpropagation to obtain the gradient
```
function [a2, a3] = forward_propagation(a1, theta1, theta2)
```
* used to perform forward propagation of the given neurons and return the
activation of the hidden layer neurons and the activation of final neurons 
```
function [classes] = predict_classes(X, weights, input_layer_size, hidden_layer_size, output_layer_size)
```
* used to compute the digit written in the inital photo for every sample
provided using the trained weights


<br>

function [Theta] = gradient_descent(FeatureMatrix, Y, n, m, alpha, iter)
  % FeatureMatrix -> the matrix with all training examples
  % Y -> the vector with all actual values
  % n -> the number of predictors
  % m -> the number of trainings
  % alpha -> the learning rate
  % iter -> the number of iterations

  % Theta -> the vector of weights
  
  
  % initializing Theta to all zeros
  Theta = zeros(n, 1);
  
  % performing the Descent Gradient Method using the given formula
  for k = 1 : iter
    J = (FeatureMatrix' * ((FeatureMatrix * Theta) - Y)) / m;
    Theta = Theta - (alpha * J);
  endfor
  
  % appending the 0-th predictor
  Theta = [0; Theta];
  
endfunction

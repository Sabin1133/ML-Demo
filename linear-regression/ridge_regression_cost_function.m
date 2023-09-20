function [Error] = ridge_regression_cost_function(Theta, Y, FeatureMatrix, lambda)
  % Theta -> the vector of weights
  % Y -> the vector with all actual values
  % FeatureMatrix -> the matrix with all training examples
  % lambda -> regularization parameter that controls the amount of 
  %           shrinkage applied to the regression coefficients

  % Error -> the error of the regularized cost function

  
  % get dimensions
  [m n] = size(FeatureMatrix);
  
  % separate the 0-th predictor
  free_var(1:m, 1) = Theta(1);
  Theta = Theta(2:length(Theta));
  
  % calculating the cost using the given formula
  first_norm_sqr = norm(FeatureMatrix * Theta + free_var - Y) ^ 2;
  second_norm_sqr = norm(Theta) ^ 2;
  
  Error = (first_norm_sqr / (2 * m)) + (lambda * second_norm_sqr);
  
endfunction

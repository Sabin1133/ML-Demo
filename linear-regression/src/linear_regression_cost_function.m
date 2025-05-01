function [Error] = linear_regression_cost_function(Theta, Y, FeatureMatrix)
  % Theta -> the vector of weights
  % Y -> the vector with all actual values
  % FeatureMatrix -> the matrix with all training examples

  % Error -> the error of the regularized cost function

  
  % get dimensions
  [m n] = size(FeatureMatrix);
  
  % separate the 0-th predictor
  free_var(1:m, 1) = Theta(1);
  Theta = Theta(2:length(Theta));
  
  % calculating the cost using the given formula
  Error = (norm(FeatureMatrix * Theta + free_var - Y) ^ 2) / (2 * m);
  
endfunction

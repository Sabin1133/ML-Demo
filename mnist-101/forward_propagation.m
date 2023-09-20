function [a2, a3] = forward_propagation(a1, theta1, theta2)
  % here at every propagation we add a row of ones
  % because this function supports not only a dataset but a vector of datasets (matrix with neurons)
  % so for every dataset we add a 1 for the bias
  
  % the neurons of every layer computed do not contain the 1 for the bias, only the neurons
  
  "sigmoid";
  
  % first propagation/layer
  [n n] = size(a1);
  a2 = theta1 * [ones(1, n); a1];
  a2 = sigmoid(a2);
  
  % second propagation/layer
  [n n] = size(a2);
  a3 = theta2 * [ones(1, n); a2];
  a3 = sigmoid(a3);
  
endfunction
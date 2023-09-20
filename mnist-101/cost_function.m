function [J, grad] = cost_function(params, X, y, lambda, ...
                   input_layer_size, hidden_layer_size, ...
                   output_layer_size)

  % params -> vector containing the weights from the two matrices
  %           Theta1 and Theta2 in an unrolled form (as a column vector)
  % X -> the feature matrix containing the training examples
  % y -> a vector containing the labels (from 1 to 10) for each
  %      training example
  % lambda -> the regularization constant/parameter
  % [input|hidden|output]_layer_size -> the sizes of the three layers
  
  % J -> the cost function for the current parameters
  % grad -> a column vector with the same length as params
  % These will be used for optimization using fmincg
  
  
  "extract_matrices";
  "forward_propagation";
  
  % extract the matrices and reshape them according to the given formulae
  % first we extract s1 * (s0 + 1) weights and then reshape them
  [theta1 theta2] = extract_matrices(params, input_layer_size, hidden_layer_size, output_layer_size);
  
  % compute the neuron activation of the hidden and output layer using forward propagation
  a1 = X';
  [a2 a3] = forward_propagation(a1, theta1, theta2);
  % and modify y vector into the "neuron activated" matrix form
  y = eye(10)(:, y);
  
  % calculate the cost for m tests
  m = length(y);
  cost = sum(sum((-y .* log(a3)) - ((1 - y) .* log(1 - a3))));
  J = (cost / m) + (lambda / (2 * m)) * (sum(sum(theta1(:, 2:end) .^ 2)) + sum(sum(theta2(:, 2:end) .^ 2)));
  
  % execute backpropagation using the given formulae
  delta1 = zeros(size(theta1));
  delta2 = zeros(size(theta2));
  for i = 1:m
    % compute error in output layer
    err3 = a3(:, i) - y(:, i);
    delta2 += (err3 * [1; a2(:, i)]');
    
    %  compute error in hidden layer
    err2 = (theta2' * err3)(2:end) .* (a2(:, i) .* (1 - a2(:, i)));  
    delta1 += (err2 * [1; a1(:, i)]');
  endfor
  
  % determine the gradient using also the given formulae
  grad1 = delta1 / m;
  grad1(:, 2:end) += ((lambda / m) * theta1(:, 2:end));
  grad2 = delta2 / m;
  grad2(:, 2:end) += ((lambda / m) * theta2(:, 2:end));
  
  grad = [grad1(:); grad2(:)];

endfunction

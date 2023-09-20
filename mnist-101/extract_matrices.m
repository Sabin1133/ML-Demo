function [theta1, theta2] = extract_matrices(weights, input_layer_size, ...
                          hidden_layer_size, output_layer_size)
  
  % calculate only the first matrix size
  % because the second size is just the remaining size
  % and then reshape the matrices
  size1 = hidden_layer_size * (1 + input_layer_size);
  theta1 = reshape(weights(1:size1), hidden_layer_size, input_layer_size + 1);
  theta2 = reshape(weights((size1 + 1):end), output_layer_size, hidden_layer_size + 1);
  
endfunction
function [matrix] = initialize_weights(L_prev, L_next)
  % L_prev -> the number of units in the previous layer
  % L_next -> the number of units in the next layer

  % matrix -> the matrix with random values

  
  eps = sqrt(6) / sqrt(L_prev + L_next);
  
  matrix = (2 * eps * rand(L_next, L_prev + 1)) - eps;
  
endfunction

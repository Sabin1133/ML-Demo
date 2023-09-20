function [Theta] = normal_equation(FeatureMatrix, Y, tol, iter)
  % FeatureMatrix -> the matrix with all training examples
  % Y -> the vector with all actual values
  % tol -> the learning rate
  % iter -> the number of iterations
  % tol -> the tolerance level for convergence of the conjugate gradient method

  % Theta -> the vector of weights

  
  % initializing the system
  A = FeatureMatrix' * FeatureMatrix;
  b = FeatureMatrix' * Y;
  Theta = zeros(length(b), 1);
  
  % returning Theta (vector full of zeros) if matrix is not positive definite
  % "all" checks is all elements are nonnull
  if all(eig(A) > 0) < 1
    Theta = [0; Theta];
    return;
  endif
  
  % initial values using the given formula 
  r_0 = b; % r = b - A * Theta, but Theta_0 is all zeros
  v = r_0;
  tolsqr = tol ^ 2;
  
  % performing the Conjugate Gradient Method using the given formula
  k = 1;
  while (k <= iter) && ((r_0' * r_0) > tolsqr)
    t = (r_0' * r_0) / (v' * A * v);
    
    Theta += (t * v);
    r_1 = r_0 - (t * A * v);
    
    s = (r_1' * r_1) / (r_0' * r_0);
    v = r_1 + (s * v);
    
    r_0 = r_1;
    ++k;
  endwhile
  
  % appending the 0-th predictor
  Theta = [0; Theta];
  
endfunction

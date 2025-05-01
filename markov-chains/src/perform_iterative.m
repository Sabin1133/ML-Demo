function [x, err, steps] = perform_iterative (G, c, x0, tol, max_steps)
	% G -> iteration matrix
	% c -> iteration vector
	% x0 -> initial solution
	% tol -> accepted tolerance (norm of the difference between two solutions)
	% max_steps -> the maximum number of iterations
	
	% x -> final solution
	% err -> last calculated difference (as an euclidean norm)
	% steps -> actual number of steps performed

   
   % initial values
  err = tol + 1;
  steps = 0;
  x_k = x0;
  
  % perform Jacobi
  while (steps < max_steps && tol < err)
    x = (G * x_k) + c;
    
    err = norm(x - x_k);
    ++steps;
    
    x_k = x;
  endwhile
   
endfunction

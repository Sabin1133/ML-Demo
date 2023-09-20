function [path] = heuristic_greedy (start_position, probabilities, Adj)
	% start_position -> the starting point in the labyrinth
	% probabilities -> vector of associated probabilities: including WIN and LOSE
	% Adj -> adjacency matrix
	
	% path -> the states chosen by the algorithm

  
  [n n] = size(Adj);
  
  if (start_position < 1 || (n - 2) < start_position)
    printf("Wrong start position!\n");
    return;
  endif
  
  % initializing the stack and visited vector
  visited = zeros(1, n);
  path(1, 1) = start_position;
  idx = 1;
  
  while (0 < idx && probabilities(path(idx)) < 1)
    % top() to get the current position
    position = path(idx);
    % setting the initial neighbour to LOSE to have the smallest prob
    neigh = n;
    
    % checking all neighbours
    for i = 1:n
      if (Adj(position, i) == 1 && !visited(i) && probabilities(i) > probabilities(neigh))
        neigh = i;
      endif
    endfor
    
    % if there are no unvisited neighs remove the pos form the stack else put it on the stack 
    if (neigh == n)
      path(idx) = 0;
      --idx;
    else
      ++idx;
      visited(neigh) = 1;
      path(idx) = neigh;
    endif
  endwhile
  
  % trimming down the path if there are any zeros and transpose to obtain the column vector
  path = path(1:idx);
  path = path';

endfunction

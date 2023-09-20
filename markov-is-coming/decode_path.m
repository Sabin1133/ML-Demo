function [decoded_path] = decode_path (path, lines, cols)
	% path -> vector containing the order of the states that arrived
	% 		 to a winning position
	% lines -> numeber of lines
	% cols -> number of columns
	
	% decoded_path -> vector of pairs (line_index, column_index)
  %                 corresponding to path states
  % hint: decoded_path does not contain indices for the WIN state

  
  [n m] = size(path);
  
  % looping until n - 1 to ignore the WIN position
  for i = 1:(n - 1)
    % calculating the position based on the given labyrinth dimensions
    decoded_path(i, 1) = idivide(path(i, 1) - 1, int32(cols), 'fix') + 1;
    decoded_path(i, 2) = mod(path(i, 1) - 1, cols) + 1;
  endfor

endfunction

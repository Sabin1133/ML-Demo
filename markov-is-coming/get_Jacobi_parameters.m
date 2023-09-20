function [G, c] = get_Jacobi_parameters (Link)
	% Link -> the link matrix (edge with probabilities matrix)
	
  % G -> iteration matrix
	% c -> iteration vector

  
  [n n] = size(Link);
  
  % the matrix without the WIN and LOSE probabilities
  G = Link(1:(n - 2), 1:(n - 2));
  
  % the column of the WIN node with size number of labyrinth cells
  c = Link(1:(n - 2), n - 1);

endfunction

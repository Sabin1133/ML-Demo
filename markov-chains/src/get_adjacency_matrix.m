function [Adj] = get_adjacency_matrix (Labyrinth)
	% Labyrinth -> the matrix of all encodings
  
  % Adj -> the adjacency matrix associated to the given labyrinth

  
  [m n] = size(Labyrinth);
  
  nr_nodes = m * n;
  
  Adj = sparse(nr_nodes + 2, nr_nodes + 2);
  
  for j = 1:m
    for i = 1:n
      % the number of the corresponding labyrinth node/cell
      node = (j - 1) * n + i;
      
      % the encrypted cell data 
      codif = Labyrinth(j, i);
      
      % node list to be linked 
      dest = [];
      
      % decoding the cell data
      if (bitand(8, codif) == 0)
        dest = [dest ((nr_nodes + 1) * (j == 1) + (node - n) * (j != 1))];
      endif
      
      if (bitand(4, codif) == 0)
        dest = [dest ((nr_nodes + 1) * (j == m) + (node + n) * (j != m))];
      endif
      
      if (bitand(1, codif) == 0)
        dest = [dest ((nr_nodes + 2) * (i == 1) + (node - 1) * (i != 1))];
      endif
      
      if (bitand(2, codif) == 0)
        dest = [dest ((nr_nodes + 2) * (i == n) + (node + 1) * (i != n))];
      endif
      
      Adj(node, dest) = 1;
      
    endfor
  endfor
  
  % WIN and LOSE adjacency
  Adj(nr_nodes + 1, nr_nodes + 1) = 1;
  Adj(nr_nodes + 2, nr_nodes + 2) = 1;
  
endfunction

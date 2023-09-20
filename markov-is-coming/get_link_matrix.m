function [Link] = get_link_matrix (Labyrinth)
	% Labyrinth -> the matrix of all encodings
  
  % Link -> the link matrix associated to the given labyrinth

  
  [m n] = size(Labyrinth);
  
  nr_nodes = m * n;
  
  Link = sparse(nr_nodes + 2, nr_nodes + 2);
  
  for j = 1:m
    for i = 1:n
      % the number of the corresponding labyrinth node/cell
      node = (j - 1) * n + i;
      
      % the encrypted cell data 
      codif = Labyrinth(j, i);
      
      % computing the probability
      prob = 0;
      for k = [1 2 4 8]
        prob += (bitand(k, codif) == 0);
      endfor
      prob = 1 / prob;

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
      
      Link(node, dest) = prob;
      
    endfor
  endfor
  
  % WIN and LOSE adjacency
  Link(nr_nodes + 1, nr_nodes + 1) = 1;
  Link(nr_nodes + 2, nr_nodes + 2) = 1;
  
endfunction

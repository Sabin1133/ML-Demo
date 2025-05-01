function [Labyrinth] = parse_labyrinth(file_path)
	% file_path -> the relative path to a file that needs to
  %              be loaded_graphics_toolkits
  
  % Labyrinth -> the matrix of all encodings for the labyrinth walls

  
  fid = fopen(file_path, "r");

  % the matrix dimensions
  dim = fscanf(fid, "%i", [2 1]);
  m = dim(1,1);
  n = dim(2,1);

  % reading the labyrinth
  Labyrinth = fscanf(fid, "%d", [n m]);
  Labyrinth = Labyrinth';

  fclose(fid);

endfunction

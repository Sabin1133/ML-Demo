function [Y, InitialMatrix] = parse_data_set_file(file_path)
  % path -> a relative path to the .txt file

  % Y -> the vector with all actual values
  % InitialMatrix -> the matrix that must be transformed

  
  fid = fopen(file_path, "r");
  
  if (fid == -1)
    return;
  endif
  
  % InitialMatrix dimensions
  dim = fscanf(fid, "%f", [2 1]);
  m = dim(1);
  n = dim(2);

  aux = textscan(fid, ['%f', repmat('%s', [1 dim(2)])], 'CollectOutput', 1);
  
  Y = aux{1};
  InitialMatrix = aux{2};
  
  fclose(fid);
  
endfunction

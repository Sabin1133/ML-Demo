function [Y, InitialMatrix] = parse_csv_file(file_path)
  % path -> a relative path to the .csv file
  
  % Y -> the vector with all actual values
  % InitialMatrix -> the matrix that must be transformed

  
  fid = fopen(file_path, "r");
  
  if (fid == -1)
    return;
  endif
  
  % extra read to discard the header
  textscan(fid, "%s", 13, 'Delimiter', ',');
  
  % repmat is used to make a string of length number of columns containing only '%s'
  % so that textscan puts every entry in its column
  % 'CollectOutput' is used to group the cells by their class(type)
  % so the first cell will contain a vector of prices as floats
  % and the second cell a matrix with all the other entries as strings
  aux = textscan(fid, ['%f', repmat('%s', [1 12])], 'CollectOutput', 1, 'Delimiter', ',');
  
  Y = aux{1};
  InitialMatrix = aux{2};
  
  fclose(fid);
  
endfunction

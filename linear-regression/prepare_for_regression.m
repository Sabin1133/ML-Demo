function [FeatureMatrix] = prepare_for_regression(InitialMatrix)
  % InitialMatrix -> the matrix that must be transformed

  % FeatureMatrix -> the matrix with all training examples

  
  [m n] = size(InitialMatrix);
  
  FeatureMatrix = [];
  
  for j = 1 : m
    
    % auxiliary row
    row = [];   
    
    for i = 1 : n   
      % checking the strings to insert corresponding value
      if strcmp(InitialMatrix{j, i}, 'yes')
        row = [row 1];
      elseif strcmp(InitialMatrix{j, i}, 'no')
        row = [row 0];
      elseif strcmp(InitialMatrix{j, i}, 'semi-furnished')
        row = [row 1 0];
      elseif strcmp(InitialMatrix{j, i}, 'unfurnished')
        row = [row 0 1];
      elseif strcmp(InitialMatrix{j, i}, 'furnished')
        row = [row 0 0];
      else
        row = [row str2num(InitialMatrix{j, i})];
      endif
    endfor
    
    % appending the row to the final matrix
    FeatureMatrix = [FeatureMatrix; row];
  endfor
  
endfunction

function [X_train, y_train, X_test, y_test] = split_dataset(X, y, percent)
  % X -> the loaded dataset with all training examples
  % y -> the corresponding labels
  % percent -> fraction of training examples to be put in training dataset
  
  % X_[train|test] -> the datasets for training and test respectively
  % y_[train|test] -> the corresponding labels
  
  % Example: [X, y] has 1000 training examples with labels and percent = 0.85
  %           -> X_train will have 850 examples
  %           -> X_test will have the other 150 examples

  
  % get dimensions
  [m n] = size(X);
  nr_train = floor(percent * m);
  
  % vector containing a permutation of the first n indices
  % used to shuffle the rows
  idx = randperm(m);
  X = X(idx, :);
  y = y(idx, :);
  
  % training dataset
  X_train = X(1:nr_train, :);
  y_train = y(1:nr_train, :);
  
  % test dataset
  X_test = X((nr_train + 1):m, :);
  y_test = y((nr_train + 1):m, :);
  
endfunction

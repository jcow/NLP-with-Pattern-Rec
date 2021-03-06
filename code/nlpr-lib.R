##########################################################################################################
# Evin Ozer
# Jason Cowan
# CSCI 548-01
# Spring Semester
# 4/16/13
#
# Graduate Project - Natural Language Pattern Recognition
# ~ Common functions used for Pattern Recognition on annotated text.
##########################################################################################################
# LIBRARIES
#
library(MASS)
library(rJava)
library(FSelector)
#
# REQUIREMENTS
#
#require(graphics)
#

selectFeatures = function(X)
{
  Y = my_data[,-1]
  Y_sub = cfs(Category~.,Y)
  print(Y_sub)
  
  return(X[,Y_sub])
}

removeConstants = function(X)
{
  badIndexes = vector()
  for (i in 1:ncol(X))
  {
    if (sum(X[,i]) == (X[1,i] * nrow(X)))
      badIndexes = c(badIndexes, i)
    else if (var(X[,i] < (.0001^2)))
      badIndexes = c(badIndexes, i)
  }
  
  return(features[,-badIndexes])
}

explore = function(X,classes,w=T)
{
  constant = (ncol(X) == 250)
  
  cat(paste0("Exploring All Class Cases...\n"))
  indexes = list()
  indexes[[1]] = getIndexes(classes[[1]])
  indexes[[2]] = getIndexes(classes[[2]])
  indexes[[3]] = getIndexes(classes[[3]])
  
  c_colors = list()
  c_colors[[1]] = as.vector(classes[[1]])
  c_colors[[2]] = as.vector(classes[[2]])
  c_colors[[3]] = as.vector(classes[[3]])
  
  # For all relevant indexes, associate the following colors...
  colors = list()
  colors[[1]] = rainbow(length(unique(classes[[1]])))
  colors[[2]] = rainbow(length(unique(classes[[2]])))
  colors[[3]] = rainbow(length(unique(classes[[3]])))
  
  # Plot a heat map of the dataset.
  if (!constant) plotHeatMap(as.matrix(X),w)
  
  for (i in 1:length(indexes))
  {
    indxs = indexes[[i]]
    clrs = colors[[i]]
    c_clrs = c_colors[[i]]
    for (j in 1:length(indxs))
    {
      c_clrs[indxs[[j]]] = clrs[j]
    }
    
    c_colors[[i]] = c_clrs
  }
  
  plotPCA(X,classes,c_colors,w)
  plotMDS(X,classes,c_colors,w)
  
  if (!constant)
  {
    plotLDA(X,classes,c_colors,w)
    
    # find the accuracy of LDA
    classify(X,classes)
  }    
}

plotHeatMap = function(X,w=F){
  
  # Sets the heatmap window to be 4" by 4"
  if (w) windows(4,4)
  heatmap(X,Colv=NA,na.rm=TRUE)
}

plotData = function(x,y,classes,colors,xlabel,ylabel,lpos="topright",w=F)
{  
  par(mar=c(4.5, 4.3, 2.0, 9.8), xpd=TRUE)
  # Plot the results of the PCA with red-bordered, red-filled circles.
  plot(x,y,
       pch=16,
       col=colors,
       xlab=xlabel,
       ylab=ylabel)
  # Create a legend to display on the plot.
  legend(lpos, inset=c(-.38,0), legend=levels(classes), col=unique(colors), pch=16)
}

plotBar = function(data,names,w=F)
{
  # Sets the plot window to be 4" by 4"
  if (w) windows(4,4)
  
  # Adjusts the margins of the plot.
  par(mar=c(2.5,2.5,2.5,2.5),mgp=c(1.5,.5,0))
  
  # Plot the proportions of variance on a bar plot.
  barplot(data,names.arg=names)
}

plotPCA = function(X,classes,colors,w=T)
{
  # Perform PCA on the data and store the results.
  pca = prcomp(X,tol=0)
  
  # Extract the first (x[,1]) and second (x[,2]) principal components..
  x = pca$x[,1]
  y = pca$x[,2]
  
  # A vector of the proportion of
  # variance captured during PCA.
  proportion = vector()
  
  # Sets the plot window to be 10" by 12"
  if (w) windows(6,12)
  
  layout(matrix(c(1,2,3),nrow=3))
  
  for (i in 1:length(classes))
  {
    plotData(x,y,classes[[i]],colors[[i]],"First Principal Component","Second Principal Component", w=w)
  }
  
  # Retrieve the standard deviation of each component.
  std = as.vector(pca$sdev)
  variance = as.vector(std)
  
  # Calculate and store the variance of each component.
  variance[1] = std[1]^2
  variance[2] = std[2]^2
  variance[3] = std[3]^2
  variance[4] = std[4]^2
  
  # Calculate the total variance.
  total = variance[1] + variance[2] + variance[3] + variance[4]
  
  # Calculate and store the proportion of captured variance.
  proportion = c(variance[1]/total,
                 variance[2]/total,
                 variance[3]/total,
                 variance[4]/total)
  
  plotBar(proportion, c("PC1","PC2","PC3","PC4"),w)
}

plotMDS = function(X,classes,colors,w=T)
{
  # Generate two eigen-vectors from the distance matrix of the Iris data.
  points = cmdscale(dist(X))
  
  # Sets the plot window to be 6" by 12"
  if (w) windows(6,12)
  
  layout(matrix(c(1,2,3),nrow=3))
  
  for (i in 1:length(classes))
  {      
    # Plot the results of the PCA with red-bordered, red-filled circles.
    plotData(points[,1],points[,2],classes[[i]],colors[[i]],
             "First Principal Coordinate","Second Principal Coordinate",
             w=w)
  }
}

plotLDA = function(X, classes,colors,w=T)
{
  # Sets the plot window to be 6" by 12"
  if (w) windows(6,12)
  
  layout(matrix(c(1,2,3),nrow=3))
  
  for (i in 1:length(classes))
  {      
    # do a scatter plot if enough classes to get two linear discriminents
    if(length(unique(classes[[i]])) > 2){
      
      z = lda(X,classes[[i]])
      #get the projections
      projection_onto_first = as.matrix(X) %*% z$scaling[,1]
      projection_onto_second = as.matrix(X) %*% z$scaling[,2]
      
      # plot it
      plot(projection_onto_first, projection_onto_second, pch = 16, 
           col = colors[[i]],
           xlab = "Linear Discriminant 1",
           ylab = "Linear Discriminant 2")
      legend("topright", inset=c(-0.38,0), legend=levels(classes[[i]]), col=unique(colors[[i]]), pch=16)
    }
    # only 2 classes, one linear discriminent, do a density plot
    else{
      
      new_colors = unique(colors[[i]])
      first_color = new_colors[1]
      second_color = new_colors[2]
      
      # train the data
      z = lda(X, classes[[i]])
      
      #seperate the data
      nl_info = X[which(classes[[i]] == "informative"),]
      nl_imag = X[which(classes[[i]] == "imaginative"),]
      
      # project it
      projection_onto_first = as.matrix(X) %*% z$scaling[,1]
      nl_info_projection_onto_first = as.matrix(nl_info) %*% z$scaling[,1]
      nl_imag_projection_onto_first = as.matrix(nl_imag) %*% z$scaling[,1]
      
      myDens = density(projection_onto_first)
      myXrange = range(myDens$x)
      
      myDensInfo = density(nl_info_projection_onto_first)
      myDensImag = density(nl_imag_projection_onto_first)
      
      par(mar=c(4.5, 4.3, 2.0, 9.8), xpd=TRUE)
      plot(myDensInfo$x, myDensInfo$y, type = "l", col = first_color,
           xlim = myXrange, xlab = "Linear Discriminant 1",ylab = "Density")
      lines(myDensImag$x, myDensImag$y, col=second_color)
      legend("topright", inset=c(-0.38,0), legend=levels(classes[[i]]), col=c(first_color, second_color), pch=16)
    }
  }
}

classify = function(X, classes)
{
  for (i in 1:length(classes))
  {
    cat(paste0("X-Validation: ",length(unique(classes[[i]])),"-Class Case...\n"))
    # k-fold validation amount, how large do you want your chunks to be?
    fold_amount = 1
    
    # simple declaratives to setup
    subset_min = 1
    subset_max = fold_amount
    accuracy_totals = c()
    
    if(fold_amount == 1){
      print("Doing Leave-one-out cross validation")
    }
    else{
      print(paste(paste("Doing", fold_amount), "fold cross validation"))
    }
    
    # loop though and do fold_amount-fold cross validation
    while(subset_min < nrow(X)){
      
      # get the training indices
      leave_out = seq(subset_min, subset_max)
      train = seq(1:nrow(X))
      train = train[! train %in% leave_out]
      
      
      # Perform LDA on the training samples of the dataset.
      z = lda(X[train,],classes[[i]][train])
      
      # Generate the predicted classes for the set of non-trained, or "test," indexes.
      results = predict(z, X[-train,])$class
      
      # Infer a vector of incorrectly classified test samples.
      missed = which(results != classes[[i]][-train])
      
      # Calculate the accuracy of the classifier. = 1 - (number missed / number trained on)
      accuracy =( 1- (length(missed) / (nrow(X) - length(train)))) * 100
      
      accuracy_totals = c(accuracy_totals, accuracy)
      
      subset_min = subset_min + fold_amount
      subset_max = subset_max + fold_amount
    }
    
    print(paste("Result: ", sum(accuracy_totals)/(length(accuracy_totals)), "%", sep=""))
  }
}

normalize = function(X)
{
  for (j in 1:(ncol(X)))
  {
    mx = max(X[,j])
    mn = min(X[,j])
    
    for (i in 1:nrow(X))
    {
      X[i,j] = (X[i,j] - mn) / (mx - mn)
    }
  }
  
  return(X)
}

getIndexes = function(classes)
{
  indexes = list()
  uniqueClasses = unique(classes)
  
  for (i in 1:length(classes))
  {
    indexes[[i]] = which(classes == uniqueClasses[i])
  }
  
  return(indexes)
}

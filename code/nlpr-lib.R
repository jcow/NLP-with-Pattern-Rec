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

explore = function(X,classes,w=F)
{
  heatmap(X,Colv=NA)
  
  for (c in classes)
  {
    cat(paste0("Exploring ",length(unique(c)),"-Class Case...\n"))
    indexes = getIndexes(c)
    
    c_colors = as.vector(c)
    # For all relevant indexes, associate the following colors...
    colors = rainbow(length(unique(c)))
    
    for (i in 1:length(indexes))
    {
      c_colors[indexes[[i]]] = colors[i]
    }
    
    plotPCA(X,c,c_colors)
    plotMDS(X,c,c_colors)
    
    classify(X,c,.75)
  }  
}

plotData = function(x,y,classes,colors,xlabel,ylabel,lpos="bottomleft",w=F)
{
  # Sets the plot window to be 4" by 4"
  if (w) windows(4,4)
  
  # Adjusts the margins of the plot.
  par(mar=c(2.5,2.5,2.5,2.5),mgp=c(1.5,.5,0))
  
  # Plot the results of the PCA with red-bordered, red-filled circles.
  plot(x,y,
       pch=19,
       col=colors,
       xlab=xlabel,
       ylab=ylabel)
  # Create a legend to display on the plot.
  #legend("bottomleft", unique(classes), col=unique(colors), pch=19)
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

plotPCA = function(X,classes,colors,w=F)
{
  # Perform PCA on the data and store the results.
  pca = prcomp(X,tol=0)
  
  # Extract the first (x[,1]) and second (x[,2]) principal components..
  x = pca$x[,1]
  y = pca$x[,2]
  
  plotData(x,y,classes,colors,"First Principal Component","Second Principal Component")
  
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
  
  # Create a variable to store the proportions.
  proportion = as.vector(variance)
  
  # Calculate and store the proportion of captured variance.
  proportion[1] = variance[1]/total
  proportion[2] = variance[2]/total
  proportion[3] = variance[3]/total
  proportion[4] = variance[4]/total
  
  #plotBar(proportion[1:4],c("PC1", "PC2", "PC3", "PC4"))
}

plotMDS = function(X,classes,colors,w=F)
{
  # Generate two eigen-vectors from the distance matrix of the Iris data.
  points = cmdscale(dist(X))
  
  # Sets the plot window to be 4" by 4"
  if (w) windows(4,4)
  
  # Adjusts the margins of the plot.
  par(mar=c(2.5,2.5,2.5,2.5),mgp=c(1.5,.5,0))
  
  # Plot the results of the PCA with red-bordered, red-filled circles.
  plot(points,
       pch=19,
       col=colors,
       xlab="First Principal Coordinate",
       ylab="Second Principal Coordinate")
  # Create a legend to display on the plot.
  #legend("bottomleft", unique(classes), col=unique(colors), pch=19)
}

classify = function(X, classes, tProp)
{
    # Generate a vector to store some proportion of unique training indexes
    print("Generating sample indexes from the dataset...")
    train = sample(1:nrow(X), (nrow(X)*tProp))
    
    # Perform LDA on the training samples of the dataset.
    print("Performing LDA on the training samples...!")
    #if (is.na(tol))
    z = lda(X[train,],classes[train])
    #else
    #  z = lda(X[train,],classes[train], tol=tol)
    
    print("Generating results...")
    # Generate the predicted classes for the set of non-trained, or "test," indexes.
    results = predict(z, X[-train,])$class
    
    # Infer a vector of incorrectly classified test samples.
    missed = which(results != classes[-train])
    
    # Calculate the accuracy of the classifier.
    accuracy = 100 * (length(train) - length(missed)) / length(train)
    
    # Print the accuracy of the classification.
    print(paste("Accuracy of LDA on the dataset: ", accuracy, "%", sep=""))
    
    return(z)
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

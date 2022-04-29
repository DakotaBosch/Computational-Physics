#!/usr/bin/env python3

import numpy as np #--> Handles numpy arrays
import matplotlib
import matplotlib.pyplot as plt #--> Handles the plotting
import pandas as pd #--> All about pandas, the DataFrame, not the aninmal...
from matplotlib.colors import LogNorm #--> Enable log scale to your 2D histogram
from sklearn.utils import shuffle #--> SHuffle data
from sklearn.ensemble import RandomForestClassifier #--> Get the random forest classifier
from sklearn.metrics import roc_curve #--> All about ROC
from sklearn.metrics import confusion_matrix #--> All about confusion

#Note: Most of the parts seen here have been taken from:
#a) https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
#b) https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html
#c) https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py

#In case of comments, questions, or complaints, please contact:
#Daniel Lersch - dlersch@jlab.org

print("  ")

print("RUN TRAINING OF A RANDOM FOREST CLASSIFIER")

print("  ")


#1.) Load the data and have a look at it:
#----------------------------------------
print("Load DataFrame...")

data = 'fsu_ml_hwk_data.csv' #-->Full path to where the data is stored
data_df = pd.read_csv(data) #--> Read the data in

print("...done!")
print(" ")

print("Show a few first entries of the DataFrame...")

print(" ")
print(data_df.head(10))
print(" ")

print("...done!")
print(" ")
#----------------------------------------

#2.) Define features and target values:
#----------------------------------------
print("Prepare data for classifier training...")

X = data_df[['var1','var2','var3']].values
Y = data_df['label'].values
#----------------------------------------

#3.) Shuffle the data, in order to avoid bias:
#----------------------------------------
x_train, y_train = shuffle(X,Y,random_state=0)

print("...done!")
print(" ")
#----------------------------------------

#4.) Setup the random forest classifier:
#----------------------------------------
print("Setup random forest classifier...")

my_rf = RandomForestClassifier(
         n_estimators=10, #--> Number of trees in your forest
         warm_start=True,
         max_depth=5, #--> Maximum depth of tree
         random_state=0
)

print("...done!")
print(" ")
#----------------------------------------

#5.) Now train the random forest:
#----------------------------------------
print("Train the random forest classifier...")

my_rf.fit(x_train,y_train)

print("...done!")
print(" ")
#----------------------------------------

#6.) Get predictions and add them to the data frame:
#----------------------------------------
print("Add classifier predictions to the DataFrame...")
data_df['prediction'] = my_rf.predict(X)

probabilities = my_rf.predict_proba(X)
data_df['probability2'] = probabilities[:,1]

print(" ")
print(data_df.head(10))
print(" ")

print("...done!")
print(" ")
#----------------------------------------

n_bins = 100
print("Create a few monitroing plots...")

#7.) Plot the random forest output for species 2 only:
#----------------------------------------
plt.rcParams.update({'font.size': 18})
plt.subplots_adjust(bottom=0.15,top=0.9)

plt.hist(data_df[data_df['label'] == 1]['probability2'],bins=n_bins,log=True,facecolor='r',alpha=0.5)
plt.xlabel('Random Forest Output for Species2')
plt.ylabel('Entries [a.u.]')
#plt.show()
plt.savefig('RF_output.png')
plt.close()
#----------------------------------------

#8.) Plot variable 2 vs. variable 1 before and after classification of species2:
#----------------------------------------

fig,ax = plt.subplots(1,2,sharex=True,sharey=True)
plt.subplots_adjust(bottom=0.15,top=0.9)
#Before classification:
#Note: we look at events that JUST contain species2, i.e. labeled with 1:
ax[0].hist2d(data_df[data_df['label'] == 1]['var2'],data_df[data_df['label'] == 1]['var1'],bins=n_bins,norm=LogNorm())

#After classification:
#Note: we look at events containining ALL species, but labeled with 1:
ax[1].hist2d(data_df[data_df['prediction'] == 1]['var2'],data_df[data_df['prediction'] == 1]['var1'],bins=n_bins,norm=LogNorm())

#Make some axis-labels:
ax[0].set_xlabel('Variable 1')
ax[0].set_ylabel('Variable 2')
ax[1].set_xlabel('Variable 1')

#plt.show()
plt.savefig('RF_correlation_plots.png')
plt.close()

print("...done!")
print(" ")
#----------------------------------------

#9.) Get the roc-curve:
#----------------------------------------
print("Get and plot the ROC-Curve for Species 2...")

#This is ROC-curve for species 2, which is labeled with 1:
fpr_s2, tpr_s2, th_s2 = roc_curve(data_df['label'].values,data_df['probability2'].values,pos_label=1)

#fpr = false positive rate
#tpr = true positive rate
plt.subplots_adjust(bottom=0.15,top=0.9)
plt.plot(fpr_s2,tpr_s2,'rd',label='ROC: Species 2')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
#plt.show()
plt.savefig('RF_ROC_species2.png')
plt.close()

print("...done!")
print(" ")
#----------------------------------------

#10.) Get the confusion matrix:
#----------------------------------------
print("Calculate and show the confusion matrix...")

#Apparently, not all scikit versions support the plot_confusion_matrix() function
#so we have to do a little work-around. I am sorry for that

my_labels = [0,1,2]
#my_confusion_matrix = confusion_matrix(data_df['label'].values,data_df['prediction'].values,labels=my_labels,normalize='true')
my_confusion_matrix = confusion_matrix(data_df['label'].values,data_df['prediction'].values,labels=my_labels)
# do the normalization by hand
my_confusion_matrix = np.transpose( np.transpose(my_confusion_matrix) / my_confusion_matrix.astype(np.float).sum(axis=1) )

#Note: The following lines have been taken from:
#https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py

textFormat = '.2f'
matrixTitle = 'Normalized Confusion Matrix'
fig,ax = plt.subplots()
      
plt.rcParams['font.size'] = 20
plt.subplots_adjust(bottom=0.25,top=0.9)
im = ax.imshow(my_confusion_matrix,interpolation='nearest')

ax.set_xticks(np.arange(my_confusion_matrix.shape[1]))
ax.set_yticks(np.arange(my_confusion_matrix.shape[0]))
ax.set_xticklabels(my_labels)
ax.set_yticklabels(my_labels)
ax.set_xticks(np.arange(my_confusion_matrix.shape[1]+1)-.5,minor=True)
ax.set_yticks(np.arange(my_confusion_matrix.shape[0]+1)-.5,minor=True)

ax.tick_params(axis='both', which='major', labelsize=30)

ax.set_xlabel('Predicted Label',fontsize=30,labelpad=15)
ax.set_ylabel('True Label',fontsize=30,labelpad=25)
ax.set_title(matrixTitle,y = 1.03)
ax.figure.colorbar(im,ax=ax)

colorThresh = my_confusion_matrix.max()  / 2.
nDim = len(my_labels)
#++++++++++++++++++++++++++++++++
for i in range(0,nDim):
        #++++++++++++++++++++++++++++++++
        for j in range(0,nDim):
                  ax.text(j,i, format(my_confusion_matrix[i][j],textFormat),
                  ha = 'center',
                  va = 'center', 
                  color = "black" if my_confusion_matrix[i,j] > colorThresh else "white")
        #++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++

#plt.show()
plt.savefig('RF_confusion_matrix.png')
plt.close()

print("...done! Have a great day!")
print(" ")
#----------------------------------------


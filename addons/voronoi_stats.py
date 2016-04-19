#! /usr/bin/env python
#######################################################################################
# The purpose of this script is to take the output from the 2D planar slice averages
# that is generated from the Slices_Averages.py script and plot the ouput for 
# visualization..
#
# Author: Christopher Neal
#
# Date: 08-04-2015
# Updated: 12-19-2015
#
#######################################################################################


#### import modules
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import time
import os
import math

#Specify the path to the VoronoiData.txt file that contains the Voronoi Tesselation data
FilePathBase = '/Users/chris1/Dropbox/Grid_Generation/Mesh Shapes/3D Multiparticle Grids/Random/500_100Micron_Particles_25percentPhi/5K_Facets/'
FilePath=FilePathBase + 'VoronoiData.dat'


#Count the number of lines in the file
num_particles = sum(1 for line in open(FilePath))

#Open input file
f = open(FilePath, "r")

#Data in file has following form
# Particle ID, x,y,z, R, number of voronoi faces, voronoi volume, xc,yc,zc <- coordinates of voronoi centroid

#Loop over all lines in input file and parse
count=0 #Line counter
print("Reading Data File Contents")

Voronoi_Data = np.zeros((num_particles,10))
for Line in f:

	lineData = Line.rstrip()
	lineData = lineData.split()
		
	particleID = int(lineData[0])
	Voronoi_Data[particleID-1,0] = lineData[0]  #Particle ID Number
	Voronoi_Data[particleID-1,1] = lineData[1]  #X Coordinate of Particle
	Voronoi_Data[particleID-1,2] = lineData[2]  #Y Coordinate of Particle
	Voronoi_Data[particleID-1,3] = lineData[3]  #Z Coordinate of Particle
	Voronoi_Data[particleID-1,4] = lineData[4]  #Particle Radius
	Voronoi_Data[particleID-1,5] = lineData[5]  #Number of Voronoi Faces
	Voronoi_Data[particleID-1,6] = lineData[6]  #Voronoi Cell Volume
	Voronoi_Data[particleID-1,7] = lineData[7]  #X Coordinate of Voronoi Cell Centroid
	Voronoi_Data[particleID-1,8] = lineData[8]  #Y Coordinate of Voronoi Cell Centroid
	Voronoi_Data[particleID-1,9] = lineData[9]  #Z Coordinate of Voronoi Cell Centroid

f.close()


#Compute Statistics about the Voronoi Tesselation
CellVolumes = np.zeros(num_particles)
CellVolumeFractions = np.zeros(num_particles)

for i in range(0,num_particles):
	CellVolumes[i] = float(Voronoi_Data[i,6])
	CellVolumeFractions[i] = ((4.0/3.0)*math.pi*float(Voronoi_Data[i,4])**3)/(float(Voronoi_Data[i,6]))
	
VolMean = np.mean(CellVolumes)
print("\n Mean Cell Volume: %10.6E\n"%(VolMean))

VolStd = np.std(CellVolumes)
print("\n Standard Deviation of Cell Volume: %10.6E\n"%(VolStd))

VolMin = min(CellVolumes)
VolMax = max(CellVolumes)


VolFracMean = np.mean(CellVolumeFractions)
print("\n Mean Cell Volume Fraction: %10.6E\n"%(VolFracMean))

VolFracStd = np.std(CellVolumeFractions)
print("\n Standard Deviation of Cell Volume Fractions: %10.6E\n"%(VolFracStd))

VolFracMin = min(CellVolumeFractions)
VolFracMax = max(CellVolumeFractions)


#####Plot Variables in Plots#####
print("Outputting Statistics of Voronoi Tesselation\n")
#Create output directory and enter the directory
OutPutDir = FilePathBase +"/VoronoiData"
if not os.path.exists(OutPutDir):
	os.makedirs(OutPutDir)
	os.chdir(OutPutDir)
else:
	os.chdir(OutPutDir)


#Write statistics data to a text file 
f = open("VoronoiStats.txt", "w")
f.write( "%s:\t%10.6E\n"%("Mean of Volumes",VolMean) )
f.write( "%s:\t%10.6E\n"%("Standard Deviation of Volumes",VolStd) )
f.write( "%s:\t%10.6E\n"%("Minimum Volume",VolMin) )
f.write( "%s:\t%10.6E\n"%("Maximum Volume",VolMax) )

#Write volume fraction data as well
f.write( "%s:\t%10.6E\n"%("Mean of Volumes Fractions",VolFracMean) )
f.write( "%s:\t%10.6E\n"%("Standard Deviation of Volume Fractions",VolFracStd) )
f.write( "%s:\t%10.6E\n"%("Minimum Volume Fraction",VolFracMin) )
f.write( "%s:\t%10.6E\n"%("Maximum Volume Fraction",VolFracMax) )

f.close()

#MaxVal = np.amax(DataArray[:,i,:])
#MinVal = np.amin(DataArray[:,i,:])

#Change the min and max values a little bit so that all data lies within the bounds of the plots
#MaxVal = MaxVal + 0.05*abs(MaxVal)
#MinVal = MinVal - 0.05*abs(MinVal)


#Go back to the slice data directory
os.chdir("..")




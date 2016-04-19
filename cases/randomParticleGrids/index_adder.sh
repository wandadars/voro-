#!/bin/bash
#######################################################################################
# The purpose of this script is to add an increasing integer to each line of the
# sphereCenters.inp file(Like a line number essentially) because that is required for
# the voro++ library to read the file and utilize the data witin it.
#
# Author: Christopher Neal
#
# Date: 07-14-2015
# Updated: 07-14-2015
#
#######################################################################################

file="sphereCenters.inp"
newfile="newsphereCenters.inp"

#Make a copy of the original sphere centers file
cp $file "$file-orig"

c=1
while read line
do

   #This is the line counter to be added to each line
    prefix="$c"

    if [ $c == 1 ]; then

	#Create new file and echo contents into it
        echo "${prefix} $line">$newfile

    else
 	# Add the echo to the contents of the existing file
         echo "${prefix} $line">>$newfile
    fi


    #Increment counter
    c=$(($c+1))


    printf "%s %s\n" "$prefix	$line"

done < "$file"

#Move the new file to take the place of the original file
mv $newfile $file

#Delete the temporary file
rm -rf $newfile



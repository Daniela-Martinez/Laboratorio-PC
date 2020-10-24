#!/bin/bash
#Checksum 
md5sum < fcfm.png fcfm.png mystery_img1.txt mystery_img2.txt msg.txt > Datos_generados.txt
a=$(<Datos_propor.txt) #Datos del checksum proporcionados por el pofe.
b=$(<Datos_generados.txt)
if [ a==b ];
then 
    #Codificar
    base64 < msg.txt > cod1.txt
    base64 < fcfm.png > cod2.txt
    #Decodificar
    base64 -d < mystery_img1.txt > dec1.png
    base64 -d < mystery_img2.txt > dec2.png
else
    echo "Los datos no son correctos"
fi 



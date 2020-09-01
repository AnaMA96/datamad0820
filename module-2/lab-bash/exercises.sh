#Imprime en consola Hello World.

echo 'Hello World'

#Crea un directorio nuevo llamado new_dir.

mkdir new_dir

#Elimina ese directorio.

rmdir new_dir

#Copia el archivo sed.txt dentro de la carpeta lorem a la carpeta lorem-copy.

cp lorem/sed.txt lorem-copy/sed.txt

#Copia los otros dos archivos de la carpeta lorem a la carpeta lorem-copy en una sola línea mediante ;.

cp ./lorem/at.txt ./lorem-copy/at.txt; cp ./lorem/lorem.txt ./lorem-copy/lorem.txt

#Muestra el contenido del archivo sed.txt dentro de la carpeta lorem.

cat lorem/sed.txt

#Muestra el contenido de los archivos at.txt y lorem.txt dentro de la carpeta lorem.

cat lorem/at.txt; cat lorem/lorem.txt

#Visualiza las primeras 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy

cat lorem-copy/sed.txt | head -n 3

#Visualiza las ultimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy

cat lorem-copy/sed.txt | tail -n 3

#Añade Homo homini lupus. al final de archivo sed.txt dentro de la carpeta lorem-copy.

echo "Homo homini lupus." >> lorem-copy/sed.txt

#Visualiza las últimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy. Deberías ver ahora Homo homini lupus..

tail -n 3 lorem-copy/sed.txt

#Sustituye todas las apariciones de et por ET del archivo at.txt dentro de la carpeta lorem-copy. Deberás usar sed.

sed 's/et/ET/g' lorem-copy/at.txt

#Encuentra al usuario activo en el sistema.

who

#Encuentra dónde estás en tu sistema de ficheros.

pwd

#Lista los archivos que terminan por .txt en la carpeta lorem.

find lorem -name '*.txt'

#Cuenta el número de líneas que tiene el archivo sed.txt dentro de la carpeta lorem.

cat lorem/sed.txt | wc -l

#Cuenta el número de archivos que empiezan por lorem que están en este directorio y en directorios internos.

find . -name 'lorem.*'| wc -l

#Encuentra todas las apariciones de et en at.txt dentro de la carpeta lorem.

grep -ri "et" lorem/at.txt

#Cuenta el número de apariciones del string et en at.txt dentro de la carpeta lorem.

grep -o -i "et" lorem/at.txt | wc -l

#Cuenta el número de apariciones del string et en todos los archivos del directorio lorem-copy.

grep -o -i "et" lorem-copy/* | wc -l

#Bonus

#!/bin/bash

#Almacena en una variable name tu nombre.

name="Ana"

#Imprime esa variable.

echo $name

#Crea un directorio nuevo que se llame como el contenido de la variable name.

mkdir $name

#Elimina ese directorio.

rmdir $name

#Por cada archivo dentro de la carpeta lorem imprime el número de carácteres que tienen sus nombres. Intenta primero mostrar los archivos mediante un bucle for

for file in $(ls lorem) 
  
#Imprime los ficheros

echo item: $file | wc -m 

#Imprime las longitudes de los nombres de los ficheros

echo -n "$file" | wc -m 

#Imprime outputs con la siguiente estructura: lorem has 5 characters lenght

printf "%s has %s characters length\n" "$file" "$#file"

#Muestra los procesos de forma jerárquica que se están ejecutando en tu ordenador:
#Usando el comando top o htop

top 

#Usando el comando ps con argumentos

ps -e # -e to list all the processes on a system.
ps -f # -f offers full-format listing.

#Muestra información sobre tu procesador por pantalla

sysctl -n machdep.cpu.brand_string

#Crea 3 alias y haz que estén disponibles cada vez que inicias sesión

#Create the .bash_profile or .zsh file using the command line program called ‘nano’ if it doesn’t exist:

nano .bash_profile

#Introduce the three alias 

alias hello='ls -lah'

alias A='ls -lah'

alias l='ls -lah'

#Refresh the shell:

source ~/.zsh

#Comprime las carpetas lorem y lorem-copy en un archivo llamado lorem-compressed.tar.gz

 tar -cf lorem-compressed.tar.gz lorem/ lorem-copy/

#Descomprime el archivo lorem-compressed.tar.gz en la carpeta lorem-uncompressed

mkdir lorem-uncompressed
tar -xvf lorem-compressed.tar.gz

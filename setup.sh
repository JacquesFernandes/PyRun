echo "creating directory in /usr/bin/ ...";
mkdir /usr/bin/pyrun-src;

echo "moving execution files...";
cp main.py /usr/bin/pyrun-src/;
cp PyLin.py /usr/bin/pyrun-src/; 

echo "moving main pyrun file...";
cp pyrun /usr/bin/;

echo "Finished setting up pyrun!"

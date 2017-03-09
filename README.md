# BitFusion Code Challenge 

Build a docker container with a restful Flask app and a CLI tool that wraps around docker and instantiates your container:  

1. Build a container with a simple flask app 
2. Build a CLI in python to interact with your container 



Note: The following code must be run in python 3.x.x ;

A container image has been built by the Dockerfile found in the Container
directory. The flask application with in that container image is also
located in the Container directory.

In order to retrieve, run, stop, and remove the container based on this image,
the dockcli module must be used. It's code is in the CLI directory:

>> $ cd CLI


Once in the CLI directory, please run the following command, in order
to make the dockcli module available:

>> $ pip install --editable .


After this has successfully completed, decide on a name for the container,
and pass it in as an argument with the following command:

>> $ dockcli run \<containername\>


To stop and remove the container, run the following command:

>> $ dockcli stop \<containername\>


As it runs, the program will be updating you of its progress via stdOut.







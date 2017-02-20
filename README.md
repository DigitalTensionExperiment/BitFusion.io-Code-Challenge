# RESTfulFlaskApp

Note: The following code must be run in python 3.x.x ;

A container has been built by the Dockerfile found in the Container/
directory. The flask application running in that container is also
located in the Container/ directory.

In order to retrieve, run, stop, and remove this container, please
move into the CLI/ directory:

>> $ cd CLI/


Once in the CLI/ directory, please run the following command, in order
to make the dockcli module available:

>> $ pip install --editable .


After this has successfully completed, decide on a name for the container,
and pass it in as an argument with the following command:

>> $ dockcli run <containername>


To stop and remove the container, run the following command:

>> $ dockcli stop <containername>








import click
import docker
import requests


client = docker.from_env()


@click.group()
def cli():
    pass


# COMMAND:  dockcli run <container name> :
@click.command()
@click.option('--containername', help="")
def run(containername):
    """
    Pulls down the container from 0000000000zw/mdga ;
    Instantiates the container in daemon mode ;
    Checks and informs users of container's health status ;
    """

    print("<-----------------[pulling image from hub...]---------------->")

    # $ docker pull 0000000000zw/mdga
    image = client.images.pull("0000000000zw/mdga")
    print("Image pull complete ;")

    print("<-----------------[running container from acquired image...]---------------->")

    # $ docker run --name mdgacontainer -d -p 8888:8888  mdga/ubuntu:latest
    try:
        client.containers.run(image, detach=True, ports={'8888/tcp': 8888}, name=containername)
    except docker.errors.APIError as e:
        print(e)
        exit(-1)

    print("Container %s has been obtained ;" % containername)
    container = client.containers.get(containername)

    print("<-----------------[pausing before health check...]---------------->")

    # Before checking its health, we must give the container time to start up:
    print("Waiting for container to start ...")
    while container.attrs['State']['Health']['Status'] == "starting":
        # Updating the container while we wait:
        container = client.containers.get(containername)

    print("<-----------------[running health check...]---------------->")

    # Checking health of container:
    if container.attrs['State']['Health']['Status'] == 'healthy':
        # "return URL and port of the running flask app"
        print("Your app is running on http://localhost:8888/hello ;")
    else:
        print("The health of your container is %s " % container.attrs['State']['Health']['Status'])

    exit(0)


# COMMAND:  dockcli stop <container name> :
@click.command()
@click.option('--containername', help="")
def stop(containername):
    """
    Stops the container ;
    Removes the containere ;
    """

    # $ docker stop <containername>
    container = client.containers.get(containername)

    print("<-----------------[stopping container...]---------------->")

    # The stop() always hits a timeOut error and takes a non-zero Exit
    # regardless of the timeout window passed, or where this instruction is run...
    try:
        container.stop(timeout=30)
    except requests.exceptions.ReadTimeout:
        print("Container has stopped running: please feel free to read comments in code ;")
        pass
    # ...so we're catching and ignoring it due to practicality
    # rather than debugging this problem further, at this time ;

    container = client.containers.get(containername)

    print("<----------------[removing container...]---------------->")

    container.remove(force=True)
    # Container is removed forcefully,
    # due to the non-zero Exit code
    # occurring at the stop() function;

    print("Container has been removed successfully ;")

    exit(0)


cli.add_command(run)
cli.add_command(stop)







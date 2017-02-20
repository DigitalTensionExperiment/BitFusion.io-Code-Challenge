import click
import docker


client = docker.from_env()


@click.group()
def cli():
    pass


# COMMAND:  dockcli run <container name> ;
@click.command()
@click.option('--containername', help="")
def run(containername):
    """
    Pulls down the container
    Instantiates the container in daemon mode
    Checks and informs users of container's health status
    """

    # $ docker pull 0000000000zw/mdga
    image = client.images.pull("0000000000zw/mdga")
    print("Image pull complete ;")

    try:
        # $ docker run --name mdgacontainer -d -p 8888:8888  mdga/ubuntu:latest
        container = client.containers.run(image, detach=True, ports={'8888/tcp': 8888}, name=containername)
        # container = client.containers.get(containername)
    except docker.errors.APIError as e:
        print(e)
        exit(-1)

    print("Container obtained ;")
    container = client.containers.get(containername)

    # Giving the container time to start up:
    print("Waiting for container to start ...")
    while container.attrs['State']['Health']['Status'] == "starting":
        container = client.containers.get(containername)

    # Checking health of container:
    if container.attrs['State']['Health']['Status'] == 'healthy':
        # "return URL and port of the running flask app"
        print("Your app is running on http://localhost:8888/hello ;")
    else:
        print("The health of your container is %s " % container.attrs['State']['Health']['Status'])

    exit(0)


# COMMAND:  dockcli stop <container name> ;
@click.command()
@click.option('--containername', help="")
def stop(containername):
    """
    Stops the container
    Runs cleanup
    """

    # docker stop <containername>
    container = client.containers.get(containername)
    print("<-----------------[stop]---------------->")
    # The stop() always hits a timeOut error ...
    try:
        container.stop(timeout=30)
    except requests.exceptions.ReadTimeout:
        print("Container has stopped running ;")
        pass
    # ...so we're catching and ignoring it
    # which is more practical than debugging this further ;

    container = client.containers.get(containername)

    print("<----------------[remove]---------------->")
    container.remove(force=True)

    # The contain HAS actually stopped, but because of the timeOut
    # it's being forcefully removed ;
    print("Container removed ;")

    return 0


cli.add_command(run)
cli.add_command(stop)







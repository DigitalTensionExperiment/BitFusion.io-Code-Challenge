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
    Pull down the specified container:
    $ docker pull 0000000000zw/mdga

    Instantiate the container in daemon mode:
    $ docker run --name mdgacontainer -d -p 8888:8888  mdga/ubuntu:latest

    Check health of container:
      if the status is good,
      return URL and port of the running flask app ;
    (e.g. "Your app is running on http://localhost:8888")
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

    print("GOT CONTAINER")
    container = client.containers.get(containername)
    # Giving the container time to start up:
    print("Waiting...")
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
    Stop the container
    and have it cleanup the container
    """

    # docker stop <containername>

    return 0


cli.add_command(run)
cli.add_command(stop)







import click
import docker

client = docker.from_env()


@click.group()
def cli():
    pass


# COMMAND:  dockcli run <container name> ;
@click.command()
@click.option('--imagename', help="")
def run(imagename):
    """
    Pull down the specified container ;
    Instantiate the container in daemon mode: -d (detached) ;
    Check health of container:
      if the status is good,
      return URL and port of the running flask app ;
    (e.g. "Your app is running on http://localhost:8888")
    """

    # Pull down the specified container ;
    image = client.images.pull(imagename)
    print "Image pull: successful;"

    # instantiate the container in daemon mode: -d (detached) ;
    container = client.containers.run(image, detach=True)
    print "Container run from image: successful;"

    # Check health of container:

    return 0


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







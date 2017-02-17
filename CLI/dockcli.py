import click
import docker

client = docker.from_env()

# COMMANDS:
#  dockcli run <container name>
#  dockcli stop <container name>

@click.group()
def cli():
    pass

@click.command()
def run():
    """
    Pull down the container you created in step 1
    ** Using the Python docker module in your CLI,
    instantiate the container in daemon mode
    and set the name to <container name>

    ** Have it look up the health status
    (based on the healtcheck you created above),
    if the status is good, return the URL and port of the running flask app to the terminal
    (e.g. "Your app is running on http://localhost:8888")
    """

    return 0


@click.command()
def stop():
    """
    Stop the container
    and have it cleanup the container
    """

    return 0


cli.add_command(run)
cli.add_command(stop)







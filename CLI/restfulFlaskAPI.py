import click
import docker

client = docker.from_env()

@click.command()
@click.option('--string', default="Sono", help="Entered name of person who receives the hello ;")
@click.option('--repeat', default=1, help="Number of times to say hello ;")
def cli(string, repeat):
    """ This CLI tool instantiates [docker container] ; """
    for i in xrange(repeat):
        click.echo("Hey there, %s !" % string)










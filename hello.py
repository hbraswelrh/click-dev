"""

This is a silly implementation
Try this with different parameters

"""

import click
@click.command(help="This is not actually helpful.")
@click.option("--name", prompt="I need your name", help="Need name")
@click.option("--color", prompt="I need your color", help="This is your color")
def hello(name, color):
    if name == "Hannah":
        click.echo("Hannah you are always red.")
        click.echo(click.style(f"Hello World! {name}", fg="red"))
    else:
        #something else
        click.echo(click.style(f"Hello World! {name}", fg=color))

if __name__ =="__main__":
            hello()
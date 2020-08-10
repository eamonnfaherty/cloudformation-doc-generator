import click
import json
from cfn_flip import to_json

from . import core


@click.command()
@click.argument('f', type=click.File())
def generate(f):
    extension = f.name.split(".").pop()
    if extension in ["yaml", "yml"]:
        j = to_json(f)
    elif extension in ["json"]:
        j = f
    else:
        raise Exception("{}: not a valid file extension".format(extension))
    template = json.loads(j)
    result = core.generate(template, ".".join(f.name.split(".")[0:-1]))
    click.echo(result)


if __name__ == "__main__":
    generate()

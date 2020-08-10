from . import core
import json
from cfn_tools import load_yaml


def generate_from_json(template_content, name):
    result = core.generate(json.loads(template_content), name)
    return result


def generate_from_yaml(template_content, name):
    result = core.generate(load_yaml(template_content), name)
    return result

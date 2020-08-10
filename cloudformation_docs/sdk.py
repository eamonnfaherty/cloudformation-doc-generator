from . import core
import json
import yaml


def generate_from_json(template_content, name):
    result = core.generate(json.loads(template_content), name)
    return result


def generate_from_yaml(template_content, name):
    result = core.generate(yaml.safe_load(template_content), name)
    return result

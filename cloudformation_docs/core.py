from jinja2 import Template


def get_parameters(template):
    params = template.get('Parameters')
    if not params:
        params = template.get('parameters')
    if not params:
        params = []
    return params


def get_resources(template):
    resources = template.get('Resources')
    if not resources:
        resources = template.get('resources')
    if not resources:
        resources = []
    return resources


def get_outputs(template):
    outputs = template.get('Outputs')
    if not outputs:
        outputs = template.get('outputs')
    if not outputs:
        outputs = []
    return outputs


def get_description(template):
    description = template.get("Description")
    if not description:
        description = template.get('description')
    if not description:
        description = "No Template description set"
    return description


TEMPLATE = """# {{ name }}
# Description
{{ description }}

## Parameters
The list of parameters for this template:
{% for parameter in parameters %}
### {{ parameter }} 
Type: {{ parameters[parameter].Type }} {% if parameters[parameter].Default %}
Default: {{ parameters[parameter].Default}}{% endif %} {% if parameters[parameter].Description %}
Description: {{ parameters[parameter].Description}}{% endif %} {% endfor %}

## Resources
The list of resources this template creates:
{% for resource in resources %}
### {{ resource }} 
Type: {{ resources[resource].Type }} {% if resources[resource].Description %}
Description: {{ resources[resource].Description}}{% endif %} {% endfor %}

## Outputs
The list of outputs this template exposes:
{% for output in outputs %}
### {{ output }} 
{% if outputs[output].Description %}Description: {{ outputs[output].Description}}{% endif %}{% if outputs[output].Export %} 
Export name: {{ outputs[output].Export.Name }}{% endif %}  
{% endfor %}
"""


def generate(template, name):
    description = get_description(template)
    parameters = get_parameters(template)
    resources = get_resources(template)
    outputs = get_outputs(template)

    return Template(TEMPLATE).render(
        name=name,
        description=description,
        parameters=parameters,
        resources=resources,
        outputs=outputs,
    )

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cloudformation-docs",
    version="0.1.0",
    author="Eamonn Faherty",
    author_email="packages@designandsolve.co.uk",
    description="Generate docs from cloudformation templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/eamonnfaherty/cloudformation-javadocs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'cfn-docs = cloudformation_docs.cli:generate'
        ]},
    install_requires=[
        'click',
        'Jinja2>=2.10.1',
        'cfn_flip',
    ],
)

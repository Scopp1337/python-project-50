### Hexlet tests and linter status:
[![Actions Status](https://github.com/Scopp1337/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Scopp1337/python-project-50/actions)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Scopp1337_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Scopp1337_python-project-50)


## Demo links

[Example of a project operation](https://asciinema.org/a/tMcYsphjU72u6NdnCptrjiA6q)


## Gendiff - Difference Calculator
Gendiff is a smart file comparison tool that analyzes differences between configuration files and presents them in a clear, readable format. Perfect for tracking changes in JSON and YAML configurations.


## Quick Start

### Installation
git clone git@github.com:Scopp1337/python-project-50.git

cd python-project-50

uv build

uv tool install dist/*.whl

### Basic Usage
#### Compare two files (default stylish format)
gendiff file1.json file2.json

##### Compare with specific format
gendiff -f plain file1.yaml file2.yaml
gendiff -f json file1.yml file2.yml


## Features

Multi-format Support: Works with JSON and YAML files

Flexible Output: Three display formats - stylish, plain, and JSON

Smart Comparison: Deep analysis of nested structures

Developer-Friendly: Clear, structured diff output


## Supported Formats

Format	Extensions
JSON	.json
YAML	.yaml, .yml


## Usage Examples

### Stylish Format (Default)

gendiff file1.json file2.json

Displays hierarchical differences using "+" and "-" indicators.

### Plain Format

gendiff -f plain file1.yaml file2.yaml

Provides descriptive text summary of changes.

### JSON Format

gendiff -f json file1.yml file2.yml

Outputs differences as structured JSON data.


## Development

### Code Quality

make lint    # Run code linting

### Testing

make test-coverage    # Run tests with coverage report


## Requirements

Python 3.13+

UV 0.5.11+
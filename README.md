[![PyPI](https://img.shields.io/pypi/v/kappa-maki)](https://pypi.org/project/kappa-maki/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kappa-maki)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/kappa-maki)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/mit)

Forked from and inspired by the [behave-cucumber-formatter](https://github.com/BluThaitanium/Cucumber-Behave-Package/tree/main) plugin.

# Habushu Cucumber Formatter 🥒
A formatter for behave's outputs using Cucumber

Output is similar to `behave --format json.pretty`

## Installation
```bash
pip install habushu-cucumber-formatter
````

## Usage

```bash
behave --format kappa_maki:PrettyCucumberJSONFormatter
```
---
Or with an `.ini` file:
```ini
# -- FILE: behave.ini
[behave.formatters]
cucumber = habushu_cucumber_formatter:PrettyCucumberJSONFormatter
```
and use the shorthand:
```bash
behave --format cucumber 
```

## Un-Installation
```bash
pip uninstall habushu-cucumber-formatter
```

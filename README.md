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
behave --format habushu_cucumber_formatter:PrettyCucumberJSONFormatter
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

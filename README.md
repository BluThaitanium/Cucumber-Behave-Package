# Cucumber Behave Formatter 🥒
A formatter for behave's outputs using Cucumber

Output is similar to `behave --format json.pretty`

* Formatter from `https://docs.getxray.app/display/XRAY/Testing+using+Behave+in+Python`
* Inspiration from `https://github.com/iljabauer/behave-teamcity`

## Installation
```bash
pip install behave-cucumber-formatter
````

## Usage

```bash
behave --format behave_cucumber_formatter:PrettyCucumberJSONFormatter
```
---
Or with an `.ini` file:
```ini
# -- FILE: behave.ini
[behave.formatters]
cucumber = behave_cucumber_formatter:PrettyCucumberJSONFormatter
```
and use the shorthand:
```bash
behave --format cucumber 
```

## Un-Installation
```bash
pip uninstall behave-cucumber-formatter
```

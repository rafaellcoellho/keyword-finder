<p align="center">
  <a href="https://keyword-finder.heroku.com" target="_blank" rel="noopener noreferrer">
    <img alt="Logo" src="./logo.png" width="200px">
  </a>
</p>

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT Licence"></a>
  <a href="https://codeclimate.com/github/rafaellcoellho/keyword-finder/maintainability"><img src="https://api.codeclimate.com/v1/badges/944a007a44b90367d18e/maintainability" alt="Maintainability"></a>
</p>

An api that receives a word and a list of urls and returns the number of occurrences of that word in each url.

# Setup enviroment

Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/]) and run:

```bash
$ mkvirtualenv --python=python3.6 keyword-finder
```

To activate the virtual env just:

```bash
$ workon keyword-finder
```

Install requirements:
```bash
$ pip install -r requirements.txt
```

## Dev enviroment

Create a enviroment file, example:
```
REDIS_DB=1
```

Use makefile:
```bash
$ make -B run_local
```

## Tests

```bash
$ make -B tests
```

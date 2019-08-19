# Django Template

This folder contains all the sample configuration needed to create a fully functioning django app following all of Penn Labs' suggested configuration.

# Installation
In a new folder run `django-admin startproject <name of project>`, replacing `<name of project>` with the desired name for your project.

Run `cd <name of project>`, this folder is where you should run `git init` and configure git.

Copy everything from this folder in the templates repo to this folder.

Copy urls.py to `<name of project>/urls.py`

Delete `<name of project>/settings.py`

Move the settings folder to `<name of project>/settings/`

Edit `<name of project>/wsgi.py` and `manage.py` to replace `<name of project>.settings` with `<name of project>.settings.development`

Run `pipenv install -d` to install all packages needed

# Features
* CircleCI:
  * Workflow to test, build, publish, and deploy your django project using contexts to keep secrets safe
* Django
  * Multiple settings environments (development, production, and ci) each with specific configuration
    * CI
      * Configuration to upload test results to CircleCI
    * Production
      * Disable debug
      * Enable emoji support
      * Enable sentry reporting
      * Restrict `ALLOWED_HOSTS`
      * Configure Penn Labs accounts
  * Renamed admin interface
* Docker
  * .dockerignore file to prevent unnecessary files from being added to the docker image
  * Dockerfile to create a docker image to run your django project
* Git
  * .gitignore file to prevent common unnecessary files from being committed
* MIT License
* Python
  * Common dependencies pre-configured, split into regular and development packages
  * Testing, linting, code coverage, and uwsgi configuration

# Configuration
This section will lay out all the changes that need to be performed to the template configuration to use with a new app.

| File                    | Line | Description                                                                         |
|-------------------------|------|-------------------------------------------------------------------------------------|
| .circleci/config.yml    | 5    | Change pennlabs/example-project to the name of the new app to publish to docker hub |
| .circleci/config.yml    | 45   | In pennlabs.settings.ci, change pennlabs to the name of your django project         |
| .circleci/config.yml    | 119  | Change example-deploy to the CircleCI context containing production secrets         |
| settings/base.py        | 55   | In pennlabs.urls, change pennlabs to the name of your django project                |
| settings/base.py        | 73   | In pennlabs.wsgi.application, change pennlabs to the name of your django project    |
| settings/ci.py          | 1    | In pennlabs.settings.base, change pennlabs to the name of your django project       |
| settings/development.py | 1    | In pennlabs.settings.base, change pennlabs to the name of your django project       |
| settings/production.py  | 4    | In pennlabs.settings.base, change pennlabs to the name of your django project       |
| settings/production.py  | 16   | Change ALLOWED_HOSTS to reflect the FQDN used in production                         |
| settings/production.py  | 28   | Change example.pennlabs.org to the FQDN used in production                          |
| settings/production.py  | 29   | Change example_admin to the admin tag desired from platform                         |
| settings.cfg            | 9    | Change the modules on this line to the ones created in your django project          |
| settings.cfg            | 21   | In pennlabs.wsgi:application, change pennlabs to the name of your django project    |
| urls.py                 | 5    | Change Pennlabs Example Admin to a descriptive name of your django project          |

Also see [django-labs-accounts](https://github.com/pennlabs/django-labs-accounts) for configuration specific to Penn Labs accounts.
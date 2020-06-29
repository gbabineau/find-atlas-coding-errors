# Developer Notes

This relies on functionality based on [eBird API 2.0](https://documenter.getpostman.com/view/664302/S1ENwy59?version=latest).

Coding was greatly simplified using these [useful Python access functions](https://github.com/ProjectBabbler/ebird-api).

Unfortunately, there do not appear to be public API calls which let you obtain checklists by user. So it gets checklist from an area (e.g. county) and scans for ones from a particular user.

Then it goes through the checklist to look for specific species and codes.

## creating the `whl` file

`python setup.py sdist bdist_wheel`

## Testing install in virtual environment

Create the virtual environment
`python -m virtualenv env`

Activate the virtual environment

`.\env\Scripts\activate`

Test the installation

```batch
mkdir temp
rem activate the virtual environment
.\env\Scripts\activate
pushd temp
rem install the package
pip uninstall find-atlas-coding-errors
pip install ..\dist\find-atlas-coding-errors-0.0.4-py3-none-any.whl
python -m find-atlas-coding-errors --user "Guy Babineau" --area "US-VA-003" --date "2018-04-08"
popd
rem Deactivate the virtual environment
deactivate
rd temp
```

## Running Tests

`pytest`

## Create a new release version with `Bump2version`

Here is how to `bump2version` to update the versions across all files and then create a new release

```batch
bump2version patch
python setup.py sdist bdist_wheel
git push --tags
```

Then push and pull from remote!


## Getting the taxonomy

ussing a bash shell

```bash
curl --location --request GET 'https://api.ebird.org/v2/ref/taxonomy/ebird' --header 'X-eBirdApiToken: {{x-ebirdapitoken}}' > docs/taxonomy.txt
```

## finding county cods

Go to a list created in that county on ebird and then click on the county name
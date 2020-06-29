# find-atlas-review-errors

Version 0.0.4

![Application](https://github.com/gbabineau/find-atlas-review-errors/workflows/Python%20application/badge.svg) ![Labler](https://github.com/gbabineau/find-atlas-review-errors/workflows/Labeler/badge.svg)

## Installing

This requires some knowledge of working with command lines on your computer.

1. You will need to install Python.

1. Download the latest [WHL file](https://github.com/gbabineau/find-atlas-review-errors/blob/master/dist/find-atlas-review-errors-0.0.4-py3-none-any.whl).

1. Install the application using this command line text `pip install find-atlas-review-errors-0.0.4-py3-none-any.whl`

## Using

Warning, misuse of this utility can place a large demand on eBird.org servers which has a performance and cost impact on others and is not needed. You will be making the requests to eBird.org via a token you request from eBird.org using your eBird login credentials. According to eBird.org misuse of your key to access large amounts of data could result in eBird.org revoking your ability to access the data.

Request your key from [here](https://ebird.org/api/keygen). One you get it, save it as you will need it later.

Then from a command line, you can specify various command line parameters

type `python -m find-atlas-review-errors --help` for parameters

Example

```batch
C:\directory>python -m find-atlas-review-errors --user "Guy Babineau" --area "US-VA-003" --date "2018-04-01" --end "2018-04-14"

C:\directory>
```

## setting up the codes you care about

Unfortunately, these are currently set up manually by editing review_checklist.py


### Optional - save your eBird API key in an environment variable

You can save your API key in an environment variable called EBIRDAPIKEY. If you don't know how, that's fine. You can still use it on the command line. This is done to prevent the API key being shared accidentally in example scripts created for the documentation.

## What it means

I realized I had been coding woodpeckers wrongly. According to the handbook(http://amjv.org/wp-content/uploads/2018/05/VABBA2_Handbook_Draft_Final_2017.pdf), it says that woodpecker drumming gets an S or S7(as appropriate). And this is reiterated in https://ebird.org/atlasva/news/common-atlas-coding-boo-boos.

## How to fix

If desired, you can go to your observation in eBird and modify the checklist to change the code to the correct code

## Developer Notes

[See details](docs\developernotes.md)

## Other

[Contributing](CONTRIBUTING.md)

[License](LICENSE.md)

# WebScrapper
This is a small handy python application that can be used to keep track over certain products and their price and notify you via email when the price are lowered to your satisfaction.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requried dependencies.

```bash
$ pip install requests bs4
```

## Usage
To set the program up so that you don't have to run it again and again you can add the following snippet to the code.

```python
while True:
    check_price()
    time.sleep(60*60*12) 
```
This will run the check_price() function every 12 hrs.



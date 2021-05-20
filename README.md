# NPR Alarm Clock
_Using selenium and a chron job to create a simple alarm clock that plays NPR local news radio every weekday morning._

As a pretty regular listener of my local NPR news station, I decided to combine my weekday alarm with the start of Morning Edition (or at least, starting Morning Edition when I want to wake up).

## Selenium 
The selenium package opens an instance of a Chrome browser and presses the "Play" buttons for you. The chromedriver can be downloaded [here](
https://chromedriver.chromium.org/downloads). Be sure to match the version of chromedriver with your version of Chrome.

The main function of selenium in this case is to search the html of the [NPR Morning Edition](https://www.npr.org/programs/morning-edition/) page to find the class of the object needed to play the live radio. See the main chunk below:

```
# set chrome driver to open without GUI
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Using Chrome to access web without GUI
driver = webdriver.Chrome(executable_path='./chromedriver', options=options)  # headless (no window)

# Open the website
driver.get('https://www.npr.org/programs/morning-edition/')
```

Make sure to include the WebDriverWait lines to prevent this error:
```
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":".btn-live-radio"}
```
Without it your code barrels on to the next command without waiting for the webpage to update, so it thinks the element for the hidden button is missing.

## Cron job
This cron job will run the NPR_Alarm_Clock.py file every weekday morning at 8:10am. 

```
SHELL=/bin/bash
PATH=/usr/local/bin/:/usr/bin:/usr/sbin
10 8 * * 1-5 export DISPLAY=:0 && cd /path/to/python/file && python3 NPR_Alarm_Clock.py
```

## Features to Implement
- Ability to pause and unpause cron job (need to look into command line more)
- Include case for closing the browser window early without erroring out

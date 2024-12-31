# Import your IMDb watchlist to your [JustWatch](https://www.justwatch.com) account

### Prerequisites:
* Should have an IMDb and JustWatch account
* Should have ay least one movie/ show in your IMDb watchlist
* Python 3.x must be installed in your machine

### Procedure for watchlist:
* Go to your IMDb watchlist and scroll to the bottom of the page. You will find an option "Export this list". Once you click it, a file gets downloaded to your machine. Rename the file as WATCHLIST.py.
* Download the import_watchlist.py file from this repository and place it in the same folder where the WATCHLIST.csv file is present.
* Go to your JustWatch account and open DevTools.
* Go to the network tab in DevTools.
* Add a random movie/ show to your watchlist (This step is necessary because you need to find the authorization token of your account. Once they provide any other way to obtain the value, I will update here).
* Click any request that says "graphql".
* Go to the request headers section.
* From the```authorization``` header, Copy the authorization token and paste this at line no. 100 of the import_watchlist.py file. Refer [this](https://github.com/prasanth-G24/Imdb_to_JustWatch/issues/3#issuecomment-2566439959) for screenshot.
* Save the file. To import your watchlist, Open your command prompt or terminal and run ```python3 import_watchlist.py```.

### Procedure for seenlist:
* Go to your IMDb ratings and click to three dots on the top of the page. You will find an option "Export". Once you click it, a file named "ratings.csv" gets downloaded to your machine. Do not rename the file.
* Download the import_seenlist.py file and place it in the same folder where the ratings.csv file is residing.
* The rest is the same as watchlist.
* To import the seenlist, Open your command prompt or terminal and run ```python3 import_seenlist.py```.

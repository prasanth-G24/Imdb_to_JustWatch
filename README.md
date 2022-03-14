# Import your IMDb watchlist to your [JustWatch](https://www.justwatch.com) account

### Prerequisites:
* Should have an IMDb and JustWatch account
* Should have ay least one movie/ show in your IMDb watchlist
* Python 3.x must be installed in your machine

### Procedure for watchlist:
* Go to your IMDb watchlist and scroll to the bottom of the page. You will find an option "Export this list". Once you click it, a file named "WATCHLIST.csv" gets downloaded to your machine. Do not rename the file.
* Download the import_watchlist.py file and place it in the same folder where the WATCHLIST.csv file is residing.
* Go to your JustWatch account and open DevTools by clicking F12.
* Go to the network tab in DevTools.
* Add a random movie/ show to your watchlist (This step is necessary because you need to find the justwatch id and authtoken of your account. Once they provide any other way to obtain these values, I will update here).
* Click the one that has the status "204".
*  Go to the request headers section. You need to do 2 things.
1) From the ```path``` header, Copy the value of ```justwatch_id=```. Then paste it in line no. 32 of the import_watchlist.py file.
2) From the```authorization``` header, Copy the authorization token and paste this at line no. 33 of the import_watchlist.py file.
* Save the file. To import your watchlist, Open your command prompt or terminal and run ```python3 import_watchlist.py```.

Refer [this issue](https://github.com/prasanth-G24/Imdb_to_JustWatch/issues/2) for screenshots.

### Procedure for seenlist:
* Go to your IMDb ratings and click to three dots on the top of the page. You will find an option "Export". Once you click it, a file named "ratings.csv" gets downloaded to your machine. Do not rename the file.
* Download the import_seenlist.py file and place it in the same folder where the ratings.csv file is residing.
* The rest is the same as watchlist.
* To import the seenlist, Open your command prompt or terminal and run ```python3 import_seenlist.py```.

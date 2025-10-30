# folio-searcher
Stripped version of automate-missing-lists for only Folio searches but with better output data.

## Installs
[Python Download](https://www.python.org/downloads/)	
- Download the latest version of python from python.org. 
- When installing, make sure to check the box "Add python to PATH." 
- Run **installs.bat**
	- If this fails, ensure pip is installed. Run the python installer again and click **Modify**. Here you can see if pip is installed before running again.

## Setup
- Paste barcodes into barcodes.txt. It is intended to read them as a column, pasted directly from a spreadsheet. **Do not include a heading column title.**

## Operation Instructions
**Requirements**: Working log in to SCU  [FOLIO](https://scu.folio.indexdata.com/)

Setup:
1. Log into FOLIO using Google Chrome (Layout may differ if not on Chrome)
2. Right click when in Folio and pick *Inspect Element*. The keyboard shortcut for this is F12 on most systems.
3. The inspect window will have a bar at the very top with "Elements", "Console", "Sources", "Network", etc.
4. Navigate to "Application" tab and open Cookies
5. Refresh the page
6. Locate 'folioAccessToken' and copy the VALUE field
7. **For any trouble locating the access token, refer to *config_token_location.png***
8. Paste the value into **FOLIO_TOKEN.txt** and save the file.

Usage:
1. Run **run_folio.bat** --- *If this fails, ensure FOLIO_TOKEN.txt has the full token and is saved.*
11. Upon execution the command window will pop up. This is to monitor for any unexpected responses, however at this time it is safe to wait until the program finishes execution.
12. Results are saved in results.csv, which should be opened in Excel or similar.
	--- Note: barcode order is **preserved** in the output file, allowing for direct copy-pasting
- FOLIO token will change with each new session (Login), so token will have to be reconfigured for each new session.



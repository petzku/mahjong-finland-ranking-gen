# MFRS ranking generator
Semi-automatically generates HTML table for MFRS, with changes from previous rankings.

## Usage
0. Install Python, if you don't have it already. Any version >=3.6 should work, but as of the writing of this, has only been tested with Python 3.11.
1. Create two CSV files, `vanha.csv` and `uusi.csv` with the old and new ranking data, respectively. The data should be tab-separated (can just copy-paste from Excel)
2. Run `rankgen.py`. Double-clicking on the file may be sufficient; if not, on Windows, you may need to run `py -3 rankgen.py` in terminal.
3. Check that the generated HTML is appropriate, and copy-paste it onto the page.
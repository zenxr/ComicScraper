# Comic Scraper

This is a python3 script to download comics. It's intended for a certain website, but could be easily modified for others.

### Requirements

The project may later support automated installation of dependencies via pip, but for now check the imports at the top of the script for required modules.

* `python3`
* `beautifulsoup4`
* `requests`

### Running

Copy the `example_config.py` file to a new file called `config.py` and modify accordingly.

Modify the `url` variable to reflect the desired URL. Modify the `download_directory` variable to reflect the desired location to save files. I plan on wrapping this into a tkinter GUI, so later the url will be pasted in, and a file browser will be used to indicate where to store the downloads.

Run the program with `python scraper.py`.

# Comic Scraper

The project utilizes beautifulsoup to scrape a site and downloads and organizes comics. I'm still deciding on what type of GUI to make for it,
I'm not a fan of tkinter, even though its pretty simple. I'd rather create a web app so that users on my local network can read from any device.
However, the downloading functionality is working flawlessly.

### Requirements

The project may later support automated installation of dependencies via pip, but for now check the imports at the top of the script for required modules.

* `python3`
* `beautifulsoup4`
* `requests`

### Running

Copy the `example_config.py` file to a new file called `config.py` and modify accordingly.

Modify the `url` variable to reflect the desired URL. Modify the `download_directory` variable to reflect the desired location to save files. I plan on wrapping this into a tkinter GUI, so later the url will be pasted in, and a file browser will be used to indicate where to store the downloads.

Run the program with `python scraper.py`.

### What it does
The `scraper.py` script is given a URL to the main page for a comic which contains a list of URLs to chapters.
It builds a list of chapters to be downloaded, then for each chapter a list of images is saved.

Individual complete comics are stored in a configurable location (somewhat of a library) with the following structure:
```
Title
├── chapter01
|    ├── page01.ext
|    ├── page02.ext
│    └── page...
├── chapter02
|    ├── page01.ext
|    ├── page02.ext
│    └── page...
└── chapter...
     ├── page01.ext
     ├── page02.ext
     └── page...
```

### Project Structure
This is likely to change as I determine what direction to take for the GUI. The `example_config` file is intended to be copied to `config.py` and
edited for the user's preferences.

```
ComicScraper
├── README.md
├── config.py
├── example_config.py
├── requirements.txt
└── scraper.py
```

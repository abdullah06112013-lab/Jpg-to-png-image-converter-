# JPG to PNG Converter

A simple image converter with two interfaces: a browser-based HTML app and a Python command-line tool. Converts JPG/JPEG images into PNG format.

## Features

- 🖼️ Converts single images or entire folders (Python version)
- 💻 Two ways to use it — a simple webpage, or a command-line script
- ⚡ Fast, runs entirely on your own computer — no files are uploaded anywhere
- 🆓 No API key or sign-up required

## Demo

Open `jpg_to_png_converter.html` in any web browser, choose a JPG photo, and download the converted PNG.

## Getting Started

### Option 1: Browser version (`jpg_to_png_converter.html`)

No installation needed.

1. Download `jpg_to_png_converter.html`
2. Double-click it to open in your browser
3. Click the file picker, choose a `.jpg` or `.jpeg` photo
4. Click **Download PNG** to save the converted file

> Works completely offline — your photo never leaves your computer.

### Option 2: Python version (`jpg_to_png_converter.py`)

**Requirements:** Python 3 and the `Pillow` library.

```bash
pip install Pillow
```

Convert a single file:
```bash
python jpg_to_png_converter.py photo.jpg
```

Convert every JPG in a folder:
```bash
python jpg_to_png_converter.py my_folder
```

The converted PNG is saved right next to the original file.

## How It Works

- The **HTML version** uses the browser's built-in Canvas API to redraw the image and export it as a PNG.
- The **Python version** uses the [Pillow](https://pypi.org/project/Pillow/) imaging library to open and re-save the file in PNG format.

## Built With

- HTML, CSS, and vanilla JavaScript (browser version)
- Python 3 + Pillow (command-line version)

## License

This project is free to use and modify.
## Other Projects
Check out my [JPG to PNG Converter](https://github.com/abdullah06112013-lab/Language-converter) too!

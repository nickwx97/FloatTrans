# Floating Transparent Image Overlay

The Floating Transparent Image Overlay is a Python-based tool that allows you to display an image as an overlay on your Windows desktop. The image maintains transparency and supports clickthrough functionality, meaning users can interact with the elements underneath the overlay without needing to move it. This project is built using Python’s tkinter library for the GUI, PIL (Pillow) for image manipulation, and WinAPI for handling window transparency and clickthrough.

  

### Features

- Display any image as an overlay on the desktop

- Transparent background support

- Clickthrough functionality, allowing interaction with background windows

  

## Technologies Used

- Python 3.12+

- tkinter for the graphical user interface

- PIL (Pillow) for image processing

- WinAPI (through ctypes) for managing transparency and window properties

  

## Usage

- Download latest release and place EXE in repository base directory.

- Modify the config.ini file to specify the image path, transparency settings, and hotkey to close the overlay.

- Run EXE

  

## Known Issues

The application currently supports Windows only due to its reliance on WinAPI for clickthrough functionality.

  

## Future Enhancements

- Cross-platform support (Linux and macOS)

- GUI for easy configuration of settings

- Support for multiple image overlays

- Drag-and-drop functionality for image files

  

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you find any bugs or have suggestions for new features.

1. Clone the repository

```bash

git clone https://github.com/nickwx97/FloatTrans.git

cd FloatTrans

```

2. Install requirements

```bash

pip install -r requirements.txt

```

3. Compiling

```bash

.\compile.ps1

```

  

## License

This project is licensed under the GPL-3.0 license - see the LICENSE file for details.

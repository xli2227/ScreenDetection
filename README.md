# ScreenDetection

This application takes screenshot of a certain screen area and applies
[Tesseract OCR](https://nanonets.com/blog/ocr-with-tesseract/) to extracting the numbers within the image.


## For Mac: Installation Instruction

#### Required Dependencies

- Python Dependency Management - [Peotry](https://python-poetry.org/)  
    - Set config `poetry config virtualenvs.in-project true`

#### Steps

- Install package
```
poetry install
```

- [Optional] Fix some unresolved playsound dependency issue
```
# Make sure you are in this folder

pip3 install playsound

```

- Shell into virtual env
```
peotry shell
```

- Now you are able to execute the main program

```
python3 src/exeution.py
```

## For Windows: Installation Instruction

[Install Python3.x](https://www.python.org/downloads/windows/) 

```
pip install -U Pillow
pip install pytesseract
pip install opencv-python
pip install --upgrade setuptools wheel
pip install playsound
```

===> After all the installation, you will see

```
tesseract is not installed or it's not in your PATH
```
Referring to: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
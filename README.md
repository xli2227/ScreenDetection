# ScreenDetection

This application takes screenshot of a certain screen area and applies
[Tesseract OCR](https://nanonets.com/blog/ocr-with-tesseract/) to extracting the numbers within the image.


## Installation Instruction

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
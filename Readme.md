# ROBOT STUDY

# Robot Framework is implemented with Python, so you need to have Python installed.
# On Windows machines, make sure to add Python to PATH during installation.

## Installing Robot Framework with pip is simple:

# ```pip install -r requirements.txt ```

## To check that the installation was successful, run

# ``` robot --version ```

## To Execute the cases on terminal, use below code
 
``` 
robot --pythonpath . <folder_path>

for eg :) folder_name = robot_test 

robot --pythonpath . robot_test
```

## To Execute a single case on terminal, use below code

```
robot --pythonpath . <test_folder_name>/<file_name>.robot

for eg:) test_folder_name = robot_test, file_name = Testsuite.robot

robot --pythonpath . robot_test/TestSuite.robot
```

## Install Tessaract OCR tool on Machine to Use Pytesseract Library

### Windows:
Windows: Download the installer from Tesseract at UB Mannheim.
https://github.com/UB-Mannheim/tesseract/wiki

### macOS: 
Use Homebrew command
```commandline
brew install tesseract
```

### Linux: 
Install using your package manager. For example, on Ubuntu:
```commandline
sudo apt-get install tesseract-ocr
```

### Steps to follow on windows while configuring action-runner
#### Pre-condition:
Set the Execution policy to remote signed, for more information use below URL

https://www.sharepointdiary.com/2014/03/fix-for-powershell-script-cannot-be-loaded-because-running-scripts-is-disabled-on-this-system.html
Open powershell as administrator, use below command

```
Set-ExecutionPolicy RemoteSigned
```
Give Input as "A" to Yes To All and press Enter.

#### If the machine does not have Python, Tesseract-OCR, PIP on env path, We need to add manually

PYTHON to add in env path

```commandline
C:\Users\<username>\actions-runner\_work\_tool\Python\3.9.13\x64
```
Tesseract-OCR to add in env path

```commandline
C:\Program Files\Tesseract-OCR\
```

PIP library to add in env path

```commandline
C:\Users\<username>\actions-runner\_work\_tool\Python\3.9.13\x64\lib\site-packages
```

### To verify the added path configuration

Use below command to verify
#### For Python verification

```commandline
python --version
```
output: 
```
Python 3.9.13
```

#### For Tesseract-OCR verification
```commandline
tesseract --version
```
output: 
```
tesseract v5.4.0.20240606
 leptonica-1.84.1
  libgif 5.2.1 : libjpeg 8d (libjpeg-turbo 3.0.1) : libpng 1.6.43 : libtiff 4.6.0 : zlib 1.3 : libwebp 1.4.0 : libopenjp2 2.5.2
 Found AVX512BW
 Found AVX512F
 Found AVX512VNNI
 Found AVX2
 Found AVX
 Found FMA
 Found SSE4.1
 Found libarchive 3.7.4 zlib/1.3.1 liblzma/5.6.1 bz2lib/1.0.8 liblz4/1.9.4 libzstd/1.5.6
```

#### For PIP verification
```commandline
python -m pip --version
```
output: 
```
pip 24.0 from C:\Users\<username>\actions-runner\_work\_tool\Python\3.9.13\x64\lib\site-packages\pip (python 3.9)
```

#### Configuring the action-runner on windows
Get the required access for the repository and verify the following things

On repository the Settings option should be displayed.
Click on Settings and verify the options are displayed
Actions > Runners > New self hosted runner.

If the options are displayed, then we can able to add manage action runner

To add New action runner for windows, Click on New self hoster runner button.

Select the machine as windows and x64 as architecture type.

Now open the powershell window as administrator and follow the steps displayed on github action runner config page.
Similarly for Mac, Linux machines.

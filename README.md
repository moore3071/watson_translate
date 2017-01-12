# watson_translate
Hooks into the bluemix service to do basic translation

## Setup
First install the required package with

```python
pip install --upgrade watson-developer-cloud
```

Next user credentials must be added to the file.

```bash
cp credentials_template.json credentials.json
```

Then edit credentials.json to include your username
and password for your Bluemix translate service

## Running
Run the file with
```bash
python test.py
```

Ensure that you're using the same version of Python
as the one which you used pip with above. In my case on
Arch Linux, I have to type

```bash
python2 test.py
```

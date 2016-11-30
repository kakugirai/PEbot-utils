# PEbot
Register PE class in God mode
## Installation
### macOS
install [Chrome](https://www.google.com/chrome/browser/desktop/index.html) and ChromeDriver

```
brew install chromedriver
```

then

```
pip install -r requirements.txt
```
### Ubuntu
install Chrome

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb
sudo apt-get install -f
```

install **xvfb** so we can run Chrome headlessly

```
sudo apt-get install xvfb
```

install ChromDriver, you can find latest ChromeDriver release [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)

```
wget http://chromedriver.storage.googleapis.com/2.25/chromedriver_linux64.zip
sudo apt-get install unzip
unzip chromedriver_linux64.zip
chmod +x chromedriver
```

add ```chromedriver``` to $PATH

```
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```

finally

```
pip install -r requirements.txt
```

## TODOs
- [ ] Separate login process and library function (argparse)
- [ ] Provide available courses list

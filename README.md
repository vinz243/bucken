# bucken
Simple CLI tool written in python to manage BUCK maven dependencies


While working on a buck project, I wanted to add some maven dependencies, and those deps requires other deps and I soon found my self wondering how I could autmoatically download and link deps.

After many attempts, trying to make some code executed at runtime which would list deps and add them, I finally opted for a CLI approch.

This tool simply generate a BUCK file containing all instructions with everythiong pre downloaded (hashes...), a bit like npm does

## Installing

#### System-dependencies

You will need LXML:

- Debian/Ubuntu:
```sh
sudo apt-get install python-lxml
```
- Mac OS X:
```
sudo port install py27-lxml
```

#### python deps

- `dpath`
- `docopt`

#### Installation

```sh
cd ~/
git clone https://github.com/vinz243/bucken.git
chmod +x ./backen
cd /usr/bin && sudo ln -s ~/backen/backen
```

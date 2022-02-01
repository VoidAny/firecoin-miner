dependencies:
	pip3 install -r requirements.txt

install:
	cp miner.py /usr/local/bin/fireminer
	chmod +x /usr/local/bin/fireminer

uninstall:
	rm /usr/local/bin/fireminer

all: dependencies install
SOURCES/tailable-0.1.0.tar.gz:
	wget \
	https://github.com/LukasNormantas-awin/tailable/\
	archive/v0.1.0.tar.gz \
	-O SOURCES/tailable-0.1.0.tar.gz

RPMS/x86_64/tailable-0.1.0-1.x86_64.rpm: SOURCES/tailable-0.1.0.tar.gz
	rpmbuild -bb ./SPECS/tailable.spec

.PHONY: clean

clean:
	rm -rf ./BUILD/*
	rm -rf ./SOURCES/*
	rm -rf ./RPMS/*

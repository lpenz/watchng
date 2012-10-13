
PREFIX=/usr/local
BINDIR=$(PREFIX)/bin
MANDIR=$(PREFIX)/share/man

CFLAGS=-Wall -Werror


all: watchng.1

.PHONY: all install clean

watchng.1: manual.t2t
	txt2tags -t man -i $^ -o $@

README.textile: manual.t2t
	txt2tags -t html -H -i $^ -o $@
	sed -i -e 's@<B>@**@g' -e 's@</B>@**@g' $@

clean:
	rm -f watchng.1

install: watchng.1
	mkdir -p $(BINDIR)
	install watchng $(BINDIR)/watchng
	mkdir -p $(MANDIR)/man1
	install watchng.1 $(MANDIR)/man1/watchng.1


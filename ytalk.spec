Summary:     uses internet talk protocol to create multiuser chat sessions
Summary(de): benutzt das Internet-Talk-Protokoll zum Erstellen von Multiuser-Chat-Sitzungen 
Summary(fr): Utilise le protocole talk pour cr�er des discussions multi-utilisateurs
Summary(pl): klient talk umo�liwiaj�cy jednoczesn� rozmow� z kilkoma osobami
Summary(tr): Talk protokolu kullanarak ikiden fazla ki�inin konu�mas�n� sa�lar
Name:        ytalk
Version:     3.1
Release:     1
Copyright:   BSD
Group:       Networking
Source:      http://www.eleves.ens.fr:8080/home/espel/ytalk/%{name}-%{version}.tar.gz
Patch:       ytalk.patch
URL:         http://www.eleves.ens.fr:8080/home/espel/ytalk/ytalk.html
Buildroot:   /tmp/%{name}-%{version}-root

%description
ytalk is an extension of the standard Internet 'talk' protocol that allows 
more than two users per conversation, redirection of program output to others, 
as well as an easy-to-use menu of commands. It uses the same talk daemon
as the standard talk program.

%description -l de
ytalk ist eine Erweiterung des herk�mmlichen Internet-'talk'-Protokolls, die
mehr als zwei Benutzer pro Unterhaltung und die Umleitung von Programmausgaben
an andere erm�glicht und ein einfaches Befehlsmen� enth�lt. Es verwendet 
denselben Talk-D�mon wie das Standardprogramm.

%description -l fr
ytalk est une extension du protocole standard Internet 'talk' qui accepte
plus de deux utilisateurs par conversation, la redirection des affichages
aux autres, aussi bien que menus de commandes simples � utiliser. Il 
utilise le m�me d�mon que le programme talk.

%description -l pl
Ytalk jest rozszerzeniem standardowego protoko�u internetowego talk.
Pozwala na prowadzenie konwersacji przez wi�cej ni� dwie osoby, u�ywa
tego samego demona talkd co standardowy klient talk.

%description -l tr
ytalk, standart talk yaz�l�m�n�n geli�mi� bir s�r�m�d�r. �kiden fazla
ki�inin ayn� anda konu�malar�n� ve program ��kt�lar�n�n kullan�c�lara
y�nlendirilmelerini sa�lar. Kolay kullan�labilir bir komut men�s� i�erir.
Standart talkd daemon'u kullan�r.

%prep
%setup -q
%patch -p1 

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--with-x
make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/lib/X11/{,pl}/app-defaults
make install \
	prefix=$RPM_BUILD_ROOT/usr \
	sysconfdir=$RPM_BUILD_ROOT/etc

%files
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*
%config %verify(not size md5 mtime) /etc/ytalkrc

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Nov 21 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.1-1]
- new autoconf based %build and %install,
- added using $RPM_OPT_FLAGS during compile,
- added "rm -rf $RPM_BUILD_ROOT" on top %install,
- modified pl Summary,
- added ytalk.patch with fix path to system ytalkrc (must be
  /etc/ytalk) and modify default ytalkrc.

* Thu Jul 23 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [3.0.3-4]
- added pl translation,
- added buildroot support,
- added %verify in %config file,

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc

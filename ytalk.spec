Summary:	Uses internet talk protocol to create multiuser chat sessions
Summary(de):	Benutzt das Internet-Talk-Protokoll zum Erstellen von Multiuser-Chat-Sitzungen 
Summary(fr):	Utilise le protocole talk pour cr�er des discussions multi-utilisateurs
Summary(pl):	Klient talk umo�liwiaj�cy jednoczesn� rozmow� z kilkoma osobami
Summary(tr):	Talk protokolu kullanarak ikiden fazla ki�inin konu�mas�n� sa�lar
Name:		ytalk
Version:	3.1.1
Release:	3
License:	BSD
Group:		Networking
Group(de):	Netzwerkwesen
Group(es):	Red
Group(pl):	Sieciowe
Group(pt_BR):	Rede
Source0:	http://www.eleves.ens.fr/home/espel/ytalk/%{name}-%{version}.tar.gz
Patch0:		%{name}.patch
URL:		http://www.eleves.ens.fr/home/espel/ytalk/ytalk.html
BuildRequires:	autoconf
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ytalk is an extension of the standard Internet 'talk' protocol that
allows more than two users per conversation, redirection of program
output to others, as well as an easy-to-use menu of commands. It uses
the same talk daemon as the standard talk program.

%description -l de
ytalk ist eine Erweiterung des herk�mmlichen
Internet-'talk'-Protokolls, die mehr als zwei Benutzer pro
Unterhaltung und die Umleitung von Programmausgaben an andere
erm�glicht und ein einfaches Befehlsmen� enth�lt. Es verwendet
denselben Talk-D�mon wie das Standardprogramm.

%description -l fr
ytalk est une extension du protocole standard Internet 'talk' qui
accepte plus de deux utilisateurs par conversation, la redirection des
affichages aux autres, aussi bien que menus de commandes simples �
utiliser. Il utilise le m�me d�mon que le programme talk.

%description -l pl
Ytalk jest rozszerzeniem standardowego protoko�u internetowego talk.
Pozwala na prowadzenie konwersacji przez wi�cej ni� dwie osoby, u�ywa
tego samego demona talkd co standardowy klient talk.

%description -l tr
ytalk, standart talk yaz�l�m�n�n geli�mi� bir s�r�m�d�r. �kiden fazla
ki�inin ayn� anda konu�malar�n� ve program ��kt�lar�n�n kullan�c�lara
y�nlendirilmelerini sa�lar. Kolay kullan�labilir bir komut men�s�
i�erir. Standart talkd daemon'u kullan�r.

%prep
%setup -q
%patch -p1 

%build
autoconf
CPPFLAGS="-I%{_includedir}/ncurses" \
CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--without-x
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%config %verify(not size md5 mtime) %{_sysconfdir}/ytalkrc

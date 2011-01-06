Summary:	Uses internet talk protocol to create multiuser chat sessions
Summary(de.UTF-8):	Benutzt das Internet-Talk-Protokoll zum Erstellen von Multiuser-Chat-Sitzungen
Summary(es.UTF-8):	Usa el protocolo de talk de la internet para crear sesiones de chat entre varios usuarios
Summary(fr.UTF-8):	Utilise le protocole talk pour créer des discussions multi-utilisateurs
Summary(pl.UTF-8):	Klient talk umożliwiający jednoczesną rozmowę z kilkoma osobami
Summary(pt_BR.UTF-8):	Usa o protocolo de talk da internet para criar sessões de chat entre vários usuários
Summary(tr.UTF-8):	Talk protokolu kullanarak ikiden fazla kişinin konuşmasını sağlar
Name:		ytalk
Version:	3.1.1
Release:	12
License:	BSD
Group:		Networking
Source0:	http://www.iagora.com/~espel/ytalk/%{name}-%{version}.tar.gz
# Source0-md5:	e678401ab48be6728ec700458ad8ace0
Patch0:		%{name}.patch
URL:		http://www.iagora.com/~espel/ytalk/ytalk.html
BuildRequires:	autoconf
BuildRequires:	ncurses-devel >= 5.0
Provides:	talk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ytalk is an extension of the standard Internet 'talk' protocol that
allows more than two users per conversation, redirection of program
output to others, as well as an easy-to-use menu of commands. It uses
the same talk daemon as the standard talk program.

%description -l de.UTF-8
ytalk ist eine Erweiterung des herkömmlichen
Internet-'talk'-Protokolls, die mehr als zwei Benutzer pro
Unterhaltung und die Umleitung von Programmausgaben an andere
ermöglicht und ein einfaches Befehlsmenü enthält. Es verwendet
denselben Talk-Dämon wie das Standardprogramm.

%description -l es.UTF-8
ytalk es una extensión del protocolo "talk" de Internet que permite
más de dos usuarios por conversación, nueva orientación de la salida
del programa para otros, así como un menú de comandos fácil de usar.
Utiliza el mismo daemon "talk" que el programa "talk" padrón.

%description -l fr.UTF-8
ytalk est une extension du protocole standard Internet 'talk' qui
accepte plus de deux utilisateurs par conversation, la redirection des
affichages aux autres, aussi bien que menus de commandes simples à
utiliser. Il utilise le même démon que le programme talk.

%description -l pl.UTF-8
Ytalk jest rozszerzeniem standardowego protokołu internetowego talk.
Pozwala na prowadzenie konwersacji przez więcej niż dwie osoby, używa
tego samego demona talkd co standardowy klient talk.

%description -l pt_BR.UTF-8
ytalk é uma extensão do protocolo "talk" da Internet que permite mais
de dois usuários por conversação, redirecionamento da saída do
programa para outros, assim como um menu de comandos fácil de usar.
Ele utiliza o mesmo daemon "talk" que o programa "talk" padrão.

%description -l tr.UTF-8
ytalk, standart talk yazılımının gelişmiş bir sürümüdür. İkiden fazla
kişinin aynı anda konuşmalarını ve program çıktılarının kullanıcılara
yönlendirilmelerini sağlar. Kolay kullanılabilir bir komut menüsü
içerir. Standart talkd daemon'u kullanır.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
LIBS="-ltinfo" \
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses" \
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
	sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog BUGS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ytalkrc

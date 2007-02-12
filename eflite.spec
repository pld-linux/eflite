Summary:	FLite Emacspeak server
Summary(pl.UTF-8):	FLite - serwer Emacspeak
Summary(ru.UTF-8):	FLite сервер для Emacspeak
Name:		eflite
Version:	0.4.0a
Release:	0.3
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/eflite/%{name}-%{version}.tar.gz
# Source0-md5:	9b19610a304a1c9e367ce5bdc9d0fa70
Patch0:		%{name}-doc.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://eflite.sourceforge.net/
BuildRequires:	emacs
BuildRequires:	flite-devel >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Emacspeak interface to Festival Lite speech synthesizer.

%description -l pl.UTF-8
Ten pakiet zawiera interfejs Emacspeak do syntezatora mowy Festival
Lite.

%description -l ru.UTF-8
Это интерфейс для Emacspeak для синтезатора речи Festival Lite.

%prep
%setup -q -n %{name}-0.4.0
%patch0 -p1
%patch1 -p1

%build
%configure \
	--with-vox=cmu_us_kal16 \
	--with-audio=oss

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README ChangeLog eflite_test.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*

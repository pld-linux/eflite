Name:		eflite
Version:	0.4.0a
Release:	0.2
Summary:	FLite Emacspeak server
Summary(ru_RU.KOI8-R):	FLite сервер для Emacspeak
License:	GPL
Group:		Applications/Sound
URL:		http://eflite.sourceforge.net/
Source0:	http://dl.sourceforge.net/eflite/%{name}-%{version}.tar.gz
# Source0-md5:	9b19610a304a1c9e367ce5bdc9d0fa70
Patch0:		%{name}-doc.patch
Patch1:		%{name}-DESTDIR.patch
BuildRequires:	emacs
BuildRequires:	flite-devel >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Emacspeak interface to Festival Lite speech synthesizer.

%description -l ru_RU.KOI8-R
Это интерфейс для Emacspeak для синтезатора речи Festival Lite.

%package emacspeak
Summary:	FLite Emacspeak server blurb
Group:		Applications/Sound
Requires:	emacspeak

%description emacspeak
FLite Emacspeak server blurb file.

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
install -d $RPM_BUILD_ROOT%{_emacs_lispdir}/emacspeak/blurbs

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

cat <<EOF > $RPM_BUILD_ROOT%{_emacs_lispdir}/emacspeak/blurbs/eflite.blurb
blurb: eflite
program: %{_bindir}/eflite
tcl:
device:
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README ChangeLog eflite_test.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*

%files emacspeak
%defattr(644,root,root,755)
%{_emacs_lispdir}/emacspeak/blurbs/eflite.blurb

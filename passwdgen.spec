Summary:	Random password generator
Summary(pl):	Generator losowych hase³
Name:		passwdgen
Version:	2.2
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://members-http-4.rwc1.sfba.home.net/denisl/passwdgen/download/%{name}-%{version}.tar.gz
URL:		http://members.home.com/denisl/passwdgen/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	libstdc++-devel

%description
passwdgen is a utility for generating random passwords. Amongst
passwdgen's features is the ability to generate pronounceable
passwords and passwords of entirely left, right, or alternating keys.

%description -l pl
passwdgen jest narzêdziem do generowania losowych hase³. Mo¿e
generowaæ has³a mo¿liwe do wymówienia, a tak¿e sk³adaj±ce siê ze
znaków wprowadzanych jedn± rêk±.

%package devel
Summary:	passwdgen development package
Summary(pl):	passwdgen dla programistów
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and libtool script for linking with passwdgen library.

%description devel -l pl
Pliki nag³ówkowe i skrypt libtoola do biblioteki passwdgen.

%package static
Summary:	passwdgen static library
Summary(pl):	Statyczna biblioteka passwdgen
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static version of passwdgen library.

%description static -l pl
Statyczna wersja biblioteki passwdgen.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/*.so.*.*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}/passwdgen

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

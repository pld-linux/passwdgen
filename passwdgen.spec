Summary:	Random password generator
Summary(pl):	Generator losowych hase³
Name:		passwdgen
Version:	2.2
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://members-http-4.rwc1.sfba.home.net/denisl/passwdgen/download/%{name}-%{version}.tar.gz
# Source0-md5:	097cf193d1b040cf0d135945714faa83
Patch0:		%{name}-amfix.patch
Patch1:		%{name}-gcc3.patch
URL:		http://members.home.com/denisl/passwdgen/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files and libtool script for linking with passwdgen library.

%description devel -l pl
Pliki nag³ówkowe i skrypt libtoola do biblioteki passwdgen.

%package static
Summary:	passwdgen static library
Summary(pl):	Statyczna biblioteka passwdgen
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of passwdgen library.

%description static -l pl
Statyczna wersja biblioteki passwdgen.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/*.so.*.*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/passwdgen

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

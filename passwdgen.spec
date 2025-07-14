Summary:	Random password generator
Summary(pl.UTF-8):	Generator losowych haseł
Name:		passwdgen
Version:	2.2
Release:	8
License:	GPL
Group:		Applications/System
Source0:	http://www.securityfocus.com/data/tools/%{name}-%{version}.tar.gz
# Source0-md5:	097cf193d1b040cf0d135945714faa83
Patch0:		%{name}-amfix.patch
Patch1:		%{name}-gcc3.patch
Patch2:		%{name}-acfix.patch
Patch3:		%{name}-urandom.patch
Patch4:		%{name}-optfix.patch
Patch5:		%{name}-gcc4.patch
URL:		http://directory.fsf.org/pwdgen.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
passwdgen is a utility for generating random passwords. Amongst
passwdgen's features is the ability to generate pronounceable
passwords and passwords of entirely left, right, or alternating keys.

%description -l pl.UTF-8
passwdgen jest narzędziem do generowania losowych haseł. Może
generować hasła możliwe do wymówienia, a także składające się ze
znaków wprowadzanych jedną ręką.

%package devel
Summary:	passwdgen development package
Summary(pl.UTF-8):	passwdgen dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files and libtool script for linking with passwdgen library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i skrypt libtoola do biblioteki passwdgen.

%package static
Summary:	passwdgen static library
Summary(pl.UTF-8):	Statyczna biblioteka passwdgen
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of passwdgen library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki passwdgen.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

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

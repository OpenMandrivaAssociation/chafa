%define major		0
%define libname		%mklibname %{name}
%define develname	%mklibname %{name} -d

Name:		chafa
Version:	1.18.2
Release:	3
Summary:	Image-to-text converter for terminal
License:	LGPLv3+
Group:		System/Libraries
URL:		https://hpjansson.org/chafa/
Source0:	https://github.com/hpjansson/chafa/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildSystem:	autotools

BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libavif)
BuildRequires:	pkgconfig(libheif)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libjxl)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(libwebpdemux)

%description
Chafa is a command-line utility that converts all kinds of images, including
animated image formats like GIFs, into ANSI/Unicode character output that can
be displayed in a terminal.

#------------------------------------------------

%package -n	%{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n	%{libname}
The core of Chafa which converts all kinds of images, including
animated image formats like GIFs, into ANSI/Unicode characters.

#------------------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{develname}
Header files for development with %{name}.

#------------------------------------------------

%package	doc
Summary:	Chafa documentation
Group:		Documentation
BuildArch:	noarch
Recommends:	%{name}-devel

%description	doc
Documentation for %{name}.

# Pregenerated man page and gtk-doc HTML live in the tarball; VPATH
# install skips both when xsltproc/gtk-doc rebuild is disabled.
%install -a
install -dm755 %{buildroot}%{_mandir}/man1
install -pm644 docs/chafa.1 %{buildroot}%{_mandir}/man1/
install -dm755 %{buildroot}%{_datadir}/gtk-doc/html/%{name}
cp -a docs/html/* %{buildroot}%{_datadir}/gtk-doc/html/%{name}/

%files
%license COPYING.LESSER
%doc README* NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files -n %{libname}
%license COPYING.LESSER
%{_libdir}/lib%{name}.so.%{major}{,.*}

%files -n %{develname}
%license COPYING.LESSER
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%dir %{_libdir}/chafa/
%{_libdir}/chafa/include/

%files doc
%doc AUTHORS
%license COPYING.LESSER
%doc %{_datadir}/gtk-doc/html/%{name}

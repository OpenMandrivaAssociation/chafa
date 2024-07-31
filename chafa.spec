%define major		0
%define libname		%mklibname %{name}
%define develname	%mklibname %{name} -d

Name:		chafa
Version:	1.14.2
Release:	1
Summary:	Image-to-text converter for terminal
License:	LGPLv3+
Group:		System/Libraries
URL:		https://hpjansson.org/chafa/
Source0:	https://github.com/hpjansson/chafa/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:  pkgconfig(libjxl)

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

#------------------------------------------------

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static --disable-rpath
%make_build

%install
%make_install

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

%define major	1
%define libname	%mklibname gii %{major}
%define devname	%mklibname gii -d

Summary:	A flexible library for input handling
Name:		libgii
Version:	1.0.2
Release:	19
License:	MIT
Group:		System/Libraries
Url:		http://www.ggi-project.org/
Source0:	http://www.ggi-project.org/ftp/ggi/v2.1/%{name}-%{version}.src.tar.bz2
Patch0:		libgii-1.0.2-wformat.patch
BuildRequires:	chrpath
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xxf86dga)

%description
LibGII is an input library developed by the GGI Project
(http://www.ggi-project.org). Its design philosophy is similar to
LibGGI, which deals with graphics output.

LibGII is based on the concept of input streams, which virtualize
access to the underlying input drivers. Events from various input
devices are abstracted into easy-to-use structures. LibGII also allows
the application to join streams together, receiving input from an
arbitrary combination of devices.

LibGII is a separate component from LibGGI, although LibGGI depends on
LibGII for input purposes. (LibGGI's input functions are simply
wrappers for LibGII functions.)

%package -n	%{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}gii-static-devel < 1.0.2-19

%description -n	%{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-debug \
	--disable-static

%make

%install
%makeinstall_std

chrpath -d %{buildroot}%{_bindir}/mhub
chrpath -d %{buildroot}%{_bindir}/xsendbut
chrpath -d %{buildroot}%{_libdir}/libgii.so.%{major}*
chrpath -d %{buildroot}%{_libdir}/ggi/input/*.so

%files
%doc ChangeLog ChangeLog.1999 FAQ INSTALL INSTALL.autoconf NEWS 
%doc README doc/README*
%config(noreplace) %{_sysconfdir}/ggi/filter/keytrans
%config(noreplace) %{_sysconfdir}/ggi/filter/mouse
%config(noreplace) %{_sysconfdir}/ggi/libgii.conf
%dir %{_sysconfdir}/ggi
%{_bindir}/*
%dir %{_sysconfdir}/ggi/filter
%dir %{_libdir}/ggi/input
%dir %{_libdir}/ggi/filter
%{_libdir}/ggi/*/*.so
%{_mandir}/man1/*
%{_mandir}/man7/*

%files -n %{libname}
%{_libdir}/libgii.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/ggi
%dir %{_includedir}/ggi/input
%dir %{_includedir}/ggi/internal
%{_includedir}/ggi/*.h
%{_includedir}/ggi/input/*.h
%{_includedir}/ggi/internal/*.h
%{_libdir}/*.so
%{_mandir}/man3/*
%{_mandir}/man5/*


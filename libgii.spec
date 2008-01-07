%define __libtoolize true
%define major	1
%define libname	%mklibname gii %{major}

Summary:	A flexible library for input handling
Name:		libgii
Version:	1.0.2
Release:	%mkrel 7
License:	GPL
Group:		System/Libraries
URL:		http://www.ggi-project.org/
Source0:	http://www.ggi-project.org/ftp/ggi/v2.1/%{name}-%{version}.src.tar.bz2
BuildRequires:	X11-devel
%ifarch x86_86
BuildRequires:	chrpath
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{libname}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
# lib64gii2-devel conflicts with libgii0-devel too
Conflicts:	libgii0-devel
Conflicts:	%{_lib}gii0-devel

%description -n	%{libname}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package -n	%{libname}-static-devel
Summary:	Static libraries for developing programs that will use %{name}
Group:		Development/Other
Requires:	%{libname}-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
Obsoletes:	libgii0-static-devel = 0.9.1-2mdk

%description -n	%{libname}-static-devel
This package contains the static libraries that programmers will need
to develop applications which will use %{name}.

%prep
%setup -q

%build
%configure2_5x	--disable-debug \
		--enable-static

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%ifarch x86_86
chrpath -d %{_bindir}/mhub
chrpath -d %{_bindir}/xsendbut
chrpath -d %{buildroot}%{_libdir}/libgii.so.%{major}*
chrpath -d %{buildroot}%{_libdir}/ggi/input/*.so
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
 
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog ChangeLog.1999 FAQ INSTALL INSTALL.autoconf NEWS README doc/README*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/ggi/*/*.la
%{_libdir}/ggi/*/*.so
%{_mandir}/man1/*
%{_mandir}/man7/*
%config(noreplace) %{_sysconfdir}/ggi/filter/keytrans
%config(noreplace) %{_sysconfdir}/ggi/filter/mouse
%config(noreplace) %{_sysconfdir}/ggi/libgii.conf
%dir %{_sysconfdir}/ggi
%dir %{_libdir}/ggi/input
%dir %{_libdir}/ggi/filter

%files -n %{libname}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.%{major}*

%files -n %{libname}-devel
%defattr(644,root,root,755)
%dir %{_includedir}/ggi
%dir %{_includedir}/ggi/input
%dir %{_includedir}/ggi/internal
%{_includedir}/ggi/*.h
%{_includedir}/ggi/input/*.h
%{_includedir}/ggi/internal/*.h
%{_libdir}/*.so
%{_libdir}/*.la
%{_mandir}/man3/*
%{_mandir}/man5/*


%files -n %{libname}-static-devel
%defattr(644,root,root,755)
%{_libdir}/*.a

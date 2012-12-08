%define major		1
%define libname		%mklibname gii %{major}
%define develname	%mklibname gii -d

Summary:	A flexible library for input handling
Name:		libgii
Version:	1.0.2
Release:	19
License:	MIT
Group:		System/Libraries
URL:		http://www.ggi-project.org/
Source0:	http://www.ggi-project.org/ftp/ggi/v2.1/%{name}-%{version}.src.tar.bz2
Patch0:		libgii-1.0.2-wformat.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xxf86dga)
BuildRequires:	chrpath

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

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}gii1-devel < 1.0.2-19
Obsoletes:	%{_lib}gii1-static-devel < 1.0.2-19
Obsoletes:	%{_lib}gii-static-devel < 1.0.2-19

%description -n	%{develname}
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
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/ggi/filter
%dir %{_libdir}/ggi/input
%dir %{_libdir}/ggi/filter
%{_libdir}/ggi/*/*.so
%{_mandir}/man1/*
%{_mandir}/man7/*

%files -n %{libname}
%attr(755,root,root) %{_libdir}/*.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/ggi
%dir %{_includedir}/ggi/input
%dir %{_includedir}/ggi/internal
%{_includedir}/ggi/*.h
%{_includedir}/ggi/input/*.h
%{_includedir}/ggi/internal/*.h
%{_libdir}/*.so
%{_mandir}/man3/*
%{_mandir}/man5/*

%changelog
* Mon Jan 02 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.0.2-17mdv2012.0
+ Revision: 748666
- cleaned up spec
- disabled static build
- removed old pre2009 scripts

  + Andrey Bondrov <abondrov@mandriva.org>
    - Fix file list
    - Rebuild for .la files issue

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-16
+ Revision: 662370
- mass rebuild

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 1.0.2-15
+ Revision: 636053
- fix BR
- tighten BR

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-14mdv2011.0
+ Revision: 602550
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-13mdv2010.1
+ Revision: 520819
- rebuilt for 2010.1

* Wed Aug 12 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-12mdv2010.0
+ Revision: 415601
- fix -Wformat warnings

* Thu Nov 06 2008 Olivier Blin <blino@mandriva.org> 1.0.2-11mdv2009.1
+ Revision: 300316
- rebuild for new libx11

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-10mdv2009.0
+ Revision: 222590
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Jan 19 2008 Funda Wang <fwang@mandriva.org> 1.0.2-9mdv2008.1
+ Revision: 155056
- fix requires on devel package name

* Mon Jan 07 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.2-8mdv2008.1
+ Revision: 146170
- rebuild for new era
- new devel policy
- correct license (MIT not GPL)
- resync SVN to 7mdv (SVN only contained 1mdv for some reason)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Feb 14 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-1mdv2007.0
+ Revision: 121188
- new version
- spec file clean

  + Lenny Cartier <lenny@mandriva.com>
    - Import libgii

* Sun Apr 30 2006 Stefan van der Eijk <stefan@eijk.nu> 0.9.1-2mdk
- rebuild for sparc
- %%mkrel

* Fri Aug 19 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.9.1-1mdk
- 0.9.1
- %%mkrel

* Tue Dec 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.0-1mdk
- 0.9.0
- drop P0 (merged upstream)

* Tue Sep 21 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.8.5-2mdk
- drop keys that are dead (not handled) nowadays

* Fri Jun 18 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.8.5-1mdk
- 0.8.5
- drop P0


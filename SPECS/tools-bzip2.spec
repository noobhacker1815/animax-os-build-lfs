%global debug_package %{nil}
%define	_optflags -march=x86-64 -mtune=generic -O2 -pipe -fPIC
#TARBALL:	http://anduin.linuxfromscratch.org/LFS/bzip2-1.0.6.tar.gz
#TARBALL:	http://www.linuxfromscratch.org/patches/lfs/8.2/bzip2-1.0.6-install_docs-1.patch
#MD5SUM:	00b516f4704d4a7cb50a1d97e6e8e15b;SOURCES/bzip2-1.0.6.tar.gz
#MD5SUM:	6a5ac7e89b791aae556de0f745916f7f;SOURCES/bzip2-1.0.6-install_docs-1.patch
#-----------------------------------------------------------------------------
Summary:	The Bzip2 package contains programs for compressing and decompressing files.
Name:		tools-bzip2
Version:	1.0.6
Release:	2
License:	GPL
URL:		http://www.bzip.org/1.0.6/
Group:		LFS/Tools
Vendor:	Octothorpe
Source0:	http://www.bzip.org/1.0.6/bzip2-%{version}.tar.gz
Patch0:	bzip2-%{version}-install_docs-1.patch
%description
The Bzip2 package contains programs for compressing and decompressing files.
Compressing text files with bzip2 yields a much better compression percentage
than with the traditional gzip
#-----------------------------------------------------------------------------
%prep
%setup -q -n bzip2-%{version}
%patch0 -p1
%build
	  CFLAGS='%_optflags '
	CXXFLAGS='%_optflags '
	sed -i "s|-O2|${CFLAGS}|g" Makefile
	sed -i "s|-O2|${CFLAGS}|g" Makefile-libbz2_so
	make -f Makefile-libbz2_so
	make clean
	make %{?_smp_mflags}
%install
	make PREFIX=%{buildroot}%{_prefix} install
	cp -av libbz2.so*  %{buildroot}%{_libdir}
	rm -v %{buildroot}%{_bindir}/{bzcmp,bzegrep,bzfgrep,bzless}
	ln -sv bzdiff %{buildroot}%{_bindir}/bzcmp
	ln -sv bzgrep %{buildroot}%{_bindir}/bzegrep
	ln -sv bzgrep %{buildroot}%{_bindir}/bzfgrep
	ln -sv bzmore %{buildroot}%{_bindir}/bzless
	rm -rf %{buildroot}%{_docdir}
	rm -rf %{buildroot}%{_mandir}
#-----------------------------------------------------------------------------
#	Create file list
	find %{buildroot} -name '*.la' -delete
	find "${RPM_BUILD_ROOT}" -not -type d -print > filelist.rpm
	sed -i "s|^${RPM_BUILD_ROOT}||" filelist.rpm
#-----------------------------------------------------------------------------
%files -f filelist.rpm
   %defattr(-,lfs,lfs)
#-----------------------------------------------------------------------------
%changelog
*	Sun Mar 11 2018 baho-utot <baho-utot@columbus.rr.com> 1.0.6-2
*	Mon Jan 01 2018 baho-utot <baho-utot@columbus.rr.com> 1.0.6-1
-	LFS-8.1

%define debug_package %{nil}

Summary:	A robust high performance CORBA ORB for C++ and Python
Name:		python-omniorb
Version:	3.7
Release:	2
License:	GPL
Group:		System/Libraries
Source0:	http://softlayer-dal.dl.sourceforge.net/project/omniorb/omniORBpy/omniORBpy-3.7/omniORBpy-%{version}.tar.bz2
Source1:    %{name}.rpmlintrc
Patch0:		omniORBpy-3.4-link.patch
URL:		https://omniorb.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	openssl-devel
BuildRequires:	omniorb
BuildRequires:	omniorb-devel
BuildRequires:	python-omniidl

%description
omniORB is a robust high performance CORBA ORB for C++ and Python.
It is freely available under the terms of the GNU Lesser General Public License
(for the libraries), and GNU General Public License (for the tools). omniORB
is largely CORBA 2.6 compliant.

omniORB is one of only three ORBs to have been awarded the Open Group's Open
Brand for CORBA. This means that omniORB has been tested and certified CORBA
compliant, to version 2.1 of the CORBA specification. You can find out more
about the branding program at the Open Group. 

%prep
%setup -qn omniORBpy-%{version}
%patch0 -p0

%build
%configure2_5x --with-openssl
%make

%install
%makeinstall_std
# don't conflict with python-omniidl
rm -f %{buildroot}%{py_puresitedir}/omniidl_be/__init__.py*

rm -f %{buildroot}%{py_puresitedir}/CORBA.py
rm -f %{buildroot}%{py_puresitedir}/PortableServer.py

# Custom install target forces generation of .pyc files
find %{buildroot} -name \*.pyc | xargs rm -f

%files
%defattr (-,root,root)
%{py_platsitedir}/*
%ifarch x86_64
%{py_puresitedir}/*
%endif
%{_includedir}/omniORB4/*.hh
%{_includedir}/*.h


%changelog
* Sat Apr 09 2011 Funda Wang <fwang@mandriva.org> 3.4-6mdv2011.0
+ Revision: 652098
- link with libpython

* Wed Nov 17 2010 Paulo Andrade <pcpa@mandriva.com.br> 3.4-5mdv2011.0
+ Revision: 598474
- Do not install PortableServer.py when built to not conflict with pyorbit

* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 3.4-4mdv2011.0
+ Revision: 593983
- rebuild

* Thu Sep 30 2010 Paulo Andrade <pcpa@mandriva.com.br> 3.4-3mdv2011.0
+ Revision: 582207
- Conflict conditionally with pyorbit

* Tue May 11 2010 Paulo Andrade <pcpa@mandriva.com.br> 3.4-2mdv2010.1
+ Revision: 544457
- Explicitly confict with pyorbit.

* Thu Feb 18 2010 Paulo Andrade <pcpa@mandriva.com.br> 3.4-1mdv2010.1
+ Revision: 507778
- Import python-omniorb (omniORBpy) version 3.4.
- python-omniorb



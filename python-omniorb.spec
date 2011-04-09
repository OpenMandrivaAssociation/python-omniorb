Summary:	A robust high performance CORBA ORB for C++ and Python
Name:		python-omniorb
Version:	3.4
Release:	%mkrel 6
License:	GPL
Group:		System/Libraries
Source0:	http://downloads.sourceforge.net/omniorb/omniORBpy-%{version}.tar.gz
Patch0:		omniORBpy-3.4-link.patch
URL:		http://omniorb.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
rm -fr %buildroot
%makeinstall_std
# don't conflict with python-omniidl
rm -f %{buildroot}%{py_puresitedir}/omniidl_be/__init__.py*

rm -f %{buildroot}%{py_puresitedir}/CORBA.py
rm -f %{buildroot}%{py_puresitedir}/PortableServer.py

# Custom install target forces generation of .pyc files
find %{buildroot} -name \*.pyc | xargs rm -f

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%{py_platsitedir}/*
%{py_puresitedir}/*
%{_includedir}/omniORB4/*.hh
%{_includedir}/*.h

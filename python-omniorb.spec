%define conflict_with_pyorbit	0

Summary:	A robust high performance CORBA ORB for C++ and Python
Name:		python-omniorb
Version:	3.4
Release:	%mkrel 5
License:	GPL
Group:		System/Libraries
Source0:	http://sourceforge.net/projects/omniorb/files/omniORBpy/omniORBpy-3.4/omniORBpy-3.4.tar.gz
URL:		http://omniorb.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%py_requires -d
BuildRequires:	openssl-devel
BuildRequires:	omniorb
BuildRequires:	omniorb-devel
BuildRequires:	python-omniidl
%if %{conflict_with_pyorbit}
Conflicts:	pyorbit
%endif

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
%setup -q -n omniORBpy-%{version}

%build
%configure --with-omniroot=%{_prefix} --with-openssl
%make

%install
%makeinstall_std
# don't conflict with python-omniidl
rm -f %{buildroot}%{py_puresitedir}/omniidl_be/__init__.py*

%if !%{conflict_with_pyorbit}
rm -f %{buildroot}%{py_puresitedir}/CORBA.py
rm -f %{buildroot}%{py_puresitedir}/PortableServer.py
%endif

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

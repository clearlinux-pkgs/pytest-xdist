#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-xdist
Version  : 1.13.1
Release  : 9
URL      : https://pypi.python.org/packages/source/p/pytest-xdist/pytest-xdist-1.13.1.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pytest-xdist/pytest-xdist-1.13.1.tar.gz
Summary  : py.test xdist plugin for distributed testing and loop-on-failing modes
Group    : Development/Tools
License  : MIT
Requires: pytest-xdist-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://drone.io/bitbucket.org/pytest-dev/pytest-xdist/status.png
:target: https://drone.io/bitbucket.org/pytest-dev/pytest-xdist/latest
.. image:: https://pypip.in/v/pytest-xdist/badge.png
:target: https://pypi.python.org/pypi/pytest-xdist

%package python
Summary: python components for the pytest-xdist package.
Group: Default

%description python
python components for the pytest-xdist package.


%prep
%setup -q -n pytest-xdist-1.13.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

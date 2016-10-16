#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-xdist
Version  : 1.15.0
Release  : 10
URL      : http://pypi.debian.net/pytest-xdist/pytest-xdist-1.15.0.tar.gz
Source0  : http://pypi.debian.net/pytest-xdist/pytest-xdist-1.15.0.tar.gz
Summary  : py.test xdist plugin for distributed testing and loop-on-failing modes
Group    : Development/Tools
License  : MIT
Requires: pytest-xdist-python
BuildRequires : execnet
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://travis-ci.org/pytest-dev/pytest-xdist.svg?branch=master
:target: https://travis-ci.org/pytest-dev/pytest-xdist

%package python
Summary: python components for the pytest-xdist package.
Group: Default
Requires: py-python

%description python
python components for the pytest-xdist package.


%prep
%setup -q -n pytest-xdist-1.15.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

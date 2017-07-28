#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-xdist
Version  : 1.18.2
Release  : 22
URL      : http://pypi.debian.net/pytest-xdist/pytest-xdist-1.18.2.tar.gz
Source0  : http://pypi.debian.net/pytest-xdist/pytest-xdist-1.18.2.tar.gz
Summary  : py.test xdist plugin for distributed testing and loop-on-failing modes
Group    : Development/Tools
License  : MIT
Requires: pytest-xdist-python
Requires: execnet
Requires: pytest
BuildRequires : execnet
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
.. image:: http://img.shields.io/pypi/v/pytest-xdist.svg
:target: https://pypi.python.org/pypi/pytest-xdist

%package python
Summary: python components for the pytest-xdist package.
Group: Default

%description python
python components for the pytest-xdist package.


%prep
%setup -q -n pytest-xdist-1.18.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1501249448
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1501249448
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*

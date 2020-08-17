#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-xdist
Version  : 2.0.0
Release  : 75
URL      : https://files.pythonhosted.org/packages/88/ea/3f917e75050ded89382bd346ba6f80a1f0b6ad8f1f1167e5444556922c27/pytest-xdist-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/88/ea/3f917e75050ded89382bd346ba6f80a1f0b6ad8f1f1167e5444556922c27/pytest-xdist-2.0.0.tar.gz
Summary  : pytest xdist plugin for distributed testing and loop-on-failing modes
Group    : Development/Tools
License  : MIT
Requires: pytest-xdist-license = %{version}-%{release}
Requires: pytest-xdist-python = %{version}-%{release}
Requires: pytest-xdist-python3 = %{version}-%{release}
Requires: execnet
Requires: psutil
Requires: pytest
Requires: pytest-forked
BuildRequires : buildreq-distutils3
BuildRequires : execnet
BuildRequires : pluggy
BuildRequires : psutil
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytest-forked
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: http://img.shields.io/pypi/v/pytest-xdist.svg
:alt: PyPI version
:target: https://pypi.python.org/pypi/pytest-xdist

%package license
Summary: license components for the pytest-xdist package.
Group: Default

%description license
license components for the pytest-xdist package.


%package python
Summary: python components for the pytest-xdist package.
Group: Default
Requires: pytest-xdist-python3 = %{version}-%{release}

%description python
python components for the pytest-xdist package.


%package python3
Summary: python3 components for the pytest-xdist package.
Group: Default
Requires: python3-core
Provides: pypi(pytest_xdist)
Requires: pypi(execnet)
Requires: pypi(psutil)
Requires: pypi(pytest)
Requires: pypi(pytest_forked)

%description python3
python3 components for the pytest-xdist package.


%prep
%setup -q -n pytest-xdist-2.0.0
cd %{_builddir}/pytest-xdist-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597679730
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-xdist
cp %{_builddir}/pytest-xdist-2.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pytest-xdist/82dbfd684f7c04da81d4faa852c6317142daa3e7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest-xdist/82dbfd684f7c04da81d4faa852c6317142daa3e7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-xdist
Version  : 2.5.0
Release  : 94
URL      : https://files.pythonhosted.org/packages/5d/43/9dbc32d297d6eae85d6c05dc8e8d3371061bd6cbe56a2f645d9ea4b53d9b/pytest-xdist-2.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5d/43/9dbc32d297d6eae85d6c05dc8e8d3371061bd6cbe56a2f645d9ea4b53d9b/pytest-xdist-2.5.0.tar.gz
Summary  : pytest xdist plugin for distributed testing and loop-on-failing modes
Group    : Development/Tools
License  : MIT
Requires: pytest-xdist-license = %{version}-%{release}
Requires: pytest-xdist-python = %{version}-%{release}
Requires: pytest-xdist-python3 = %{version}-%{release}
Requires: execnet
Requires: pytest-forked
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(execnet)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
pytest-xdist
        ============

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
Requires: pypi(pytest)
Requires: pypi(pytest_forked)

%description python3
python3 components for the pytest-xdist package.


%prep
%setup -q -n pytest-xdist-2.5.0
cd %{_builddir}/pytest-xdist-2.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639421199
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-xdist
cp %{_builddir}/pytest-xdist-2.5.0/LICENSE %{buildroot}/usr/share/package-licenses/pytest-xdist/82dbfd684f7c04da81d4faa852c6317142daa3e7
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
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

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : importlib_metadata
Version  : 3.4.0
Release  : 41
URL      : https://files.pythonhosted.org/packages/0c/89/412afa5f0018dccf637c2d25b9d6a41623cd22beef6797c0d67a2082ccfe/importlib_metadata-3.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/0c/89/412afa5f0018dccf637c2d25b9d6a41623cd22beef6797c0d67a2082ccfe/importlib_metadata-3.4.0.tar.gz
Summary  : Read metadata from Python packages
Group    : Development/Tools
License  : Apache-2.0
Requires: importlib_metadata-license = %{version}-%{release}
Requires: importlib_metadata-python = %{version}-%{release}
Requires: importlib_metadata-python3 = %{version}-%{release}
Requires: zipp
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zipp

%description
.. image:: https://img.shields.io/pypi/v/importlib_metadata.svg
:target: `PyPI link`_

%package license
Summary: license components for the importlib_metadata package.
Group: Default

%description license
license components for the importlib_metadata package.


%package python
Summary: python components for the importlib_metadata package.
Group: Default
Requires: importlib_metadata-python3 = %{version}-%{release}

%description python
python components for the importlib_metadata package.


%package python3
Summary: python3 components for the importlib_metadata package.
Group: Default
Requires: python3-core
Provides: pypi(importlib_metadata)
Requires: pypi(zipp)

%description python3
python3 components for the importlib_metadata package.


%prep
%setup -q -n importlib_metadata-3.4.0
cd %{_builddir}/importlib_metadata-3.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610377529
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/importlib_metadata
cp %{_builddir}/importlib_metadata-3.4.0/LICENSE %{buildroot}/usr/share/package-licenses/importlib_metadata/da4dc954bbc3ab0893517cb1d7af5598f7a3daf4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/importlib_metadata/da4dc954bbc3ab0893517cb1d7af5598f7a3daf4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

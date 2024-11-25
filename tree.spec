#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v21
# autospec commit: 5424026
#
Name     : tree
Version  : 2.2.0
Release  : 23
URL      : https://oldmanprogrammer.net/tar/tree/tree-2.2.0.tgz
Source0  : https://oldmanprogrammer.net/tar/tree/tree-2.2.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: tree-bin = %{version}-%{release}
Requires: tree-license = %{version}-%{release}
Requires: tree-man = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Please read the INSTALL file for installation instructions, particularly if
you are installing on a non-Linux machine.

%package bin
Summary: bin components for the tree package.
Group: Binaries
Requires: tree-license = %{version}-%{release}

%description bin
bin components for the tree package.


%package license
Summary: license components for the tree package.
Group: Default

%description license
license components for the tree package.


%package man
Summary: man components for the tree package.
Group: Default

%description man
man components for the tree package.


%prep
%setup -q -n tree-2.2.0
cd %{_builddir}/tree-2.2.0
pushd ..
cp -a tree-2.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1732553278
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}

pushd ../buildavx2
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1732553278
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tree
cp %{_builddir}/tree-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/tree/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3 PREFIX="%{buildroot}/usr" MANDIR="%{buildroot}/usr/share/man"
popd
GOAMD64=v2
%make_install PREFIX="%{buildroot}/usr" MANDIR="%{buildroot}/usr/share/man"
## install_append content
mkdir -p %{buildroot}/usr/bin
mv %{buildroot}/tree %{buildroot}/usr/bin/
rm -f %{buildroot}*/tree

## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tree

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tree/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/tree.1

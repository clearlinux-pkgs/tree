#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tree
Version  : 1.7.0
Release  : 6
URL      : http://mama.indstate.edu/users/ice/tree/src/tree-1.7.0.tgz
Source0  : http://mama.indstate.edu/users/ice/tree/src/tree-1.7.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: tree-bin
Requires: tree-man

%description
Please read the INSTALL file for installation instructions, particularly if
you are installing on a non-Linux machine.

%package bin
Summary: bin components for the tree package.
Group: Binaries
Requires: tree-man

%description bin
bin components for the tree package.


%package man
Summary: man components for the tree package.
Group: Default

%description man
man components for the tree package.


%prep
%setup -q -n tree-1.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1527825693
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1527825693
rm -rf %{buildroot}
%make_install BINDIR="%{buildroot}%{_bindir}" MANDIR="%{buildroot}%{_mandir}/man1"
## make_install_append content
chmod 0644 %{buildroot}/usr/share/man/man1/*
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tree

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/tree.1

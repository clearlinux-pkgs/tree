#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tree
Version  : 1.7.0
Release  : 1
URL      : http://mama.indstate.edu/users/ice/tree/src/tree-1.7.0.tgz
Source0  : http://mama.indstate.edu/users/ice/tree/src/tree-1.7.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: tree-bin
Requires: tree-doc

%description
Please read the INSTALL file for installation instructions, particularly if
you are installing on a non-Linux machine.

%package bin
Summary: bin components for the tree package.
Group: Binaries

%description bin
bin components for the tree package.


%package doc
Summary: doc components for the tree package.
Group: Documentation

%description doc
doc components for the tree package.


%prep
%setup -q -n tree-1.7.0

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install BINDIR="%{buildroot}%{_bindir}" MANDIR="%{buildroot}%{_mandir}/man1"

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tree

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

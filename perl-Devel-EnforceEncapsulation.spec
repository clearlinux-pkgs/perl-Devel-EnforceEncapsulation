#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Devel-EnforceEncapsulation
Version  : 0.51
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/C/CD/CDOLAN/Devel-EnforceEncapsulation-0.51.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CD/CDOLAN/Devel-EnforceEncapsulation-0.51.tar.gz
Summary  : 'Find access violations to blessed objects'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Devel-EnforceEncapsulation-license = %{version}-%{release}
Requires: perl-Devel-EnforceEncapsulation-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Devel::EnforceEncapsulation - Find access violations to blessed objects
LICENSE
This library is free software; you can redistribute it and/or modify it
under the same terms as Perl itself.

%package dev
Summary: dev components for the perl-Devel-EnforceEncapsulation package.
Group: Development
Provides: perl-Devel-EnforceEncapsulation-devel = %{version}-%{release}
Requires: perl-Devel-EnforceEncapsulation = %{version}-%{release}

%description dev
dev components for the perl-Devel-EnforceEncapsulation package.


%package license
Summary: license components for the perl-Devel-EnforceEncapsulation package.
Group: Default

%description license
license components for the perl-Devel-EnforceEncapsulation package.


%package perl
Summary: perl components for the perl-Devel-EnforceEncapsulation package.
Group: Default
Requires: perl-Devel-EnforceEncapsulation = %{version}-%{release}

%description perl
perl components for the perl-Devel-EnforceEncapsulation package.


%prep
%setup -q -n Devel-EnforceEncapsulation-0.51
cd %{_builddir}/Devel-EnforceEncapsulation-0.51

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Devel-EnforceEncapsulation
cp %{_builddir}/Devel-EnforceEncapsulation-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Devel-EnforceEncapsulation/0d5fe9e3a709805feea74211fbd38ff6ad9add68 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::EnforceEncapsulation.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Devel-EnforceEncapsulation/0d5fe9e3a709805feea74211fbd38ff6ad9add68

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

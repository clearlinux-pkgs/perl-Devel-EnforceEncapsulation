#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-EnforceEncapsulation
Version  : 0.51
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/C/CD/CDOLAN/Devel-EnforceEncapsulation-0.51.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CD/CDOLAN/Devel-EnforceEncapsulation-0.51.tar.gz
Summary  : 'Find access violations to blessed objects'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Devel-EnforceEncapsulation-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Devel::EnforceEncapsulation - Find access violations to blessed objects
LICENSE
This library is free software; you can redistribute it and/or modify it
under the same terms as Perl itself.

%package dev
Summary: dev components for the perl-Devel-EnforceEncapsulation package.
Group: Development
Provides: perl-Devel-EnforceEncapsulation-devel = %{version}-%{release}

%description dev
dev components for the perl-Devel-EnforceEncapsulation package.


%package license
Summary: license components for the perl-Devel-EnforceEncapsulation package.
Group: Default

%description license
license components for the perl-Devel-EnforceEncapsulation package.


%prep
%setup -q -n Devel-EnforceEncapsulation-0.51

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Devel-EnforceEncapsulation
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Devel-EnforceEncapsulation/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.2/Devel/EnforceEncapsulation.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::EnforceEncapsulation.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Devel-EnforceEncapsulation/LICENSE

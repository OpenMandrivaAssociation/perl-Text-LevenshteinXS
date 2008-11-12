%define module   Text-LevenshteinXS
%define version    0.03
%define release    %mkrel 2

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    An XS implementation of the Levenshtein edit distance
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(Test)
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module implements the Levenshtein edit distance in a XS way.

The Levenshtein edit distance is a measure of the degree of proximity between
two strings. This distance is the number of substitutions, deletions or
insertions ("edits") needed to transform one string into the other one (and
vice versa). When two strings have distance 0, they are the same. A good point
to start is: <http://www.merriampark.com/ld.htm>

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorarch/Text
%perl_vendorarch/auto/Text


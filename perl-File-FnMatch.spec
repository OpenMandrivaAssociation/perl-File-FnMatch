%define modname	File-FnMatch
%define modver	0.02

Summary:	Simple filename and pathname matching
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	13
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/~mjp/%{modname}-%{modver}/FnMatch.pm
Source0:	http://search.cpan.org//CPAN/authors/id/M/MJ/MJP/File-FnMatch-0.02.tar.gz
BuildRequires:	perl-devel

%description
File::FnMatch::fnmatch() provides simple, shell-like pattern matching.

Though considerably less powerful than regular expressions, shell patterns
are nonetheless useful and familiar to a large audience of end-users.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*


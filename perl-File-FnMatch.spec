%define upstream_name File-FnMatch
%define upstream_version 0.02

Summary:	Simple filename and pathname matching
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	10
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/~mjp/%{upstream_name}-%{upstream_version}/FnMatch.pm
Source0:	http://search.cpan.org//CPAN/authors/id/M/MJ/MJP/File-FnMatch-0.02.tar.gz

BuildRequires:	perl-devel

%description
File::FnMatch::fnmatch() provides simple, shell-like pattern matching.

Though considerably less powerful than regular expressions, shell patterns
are nonetheless useful and familiar to a large audience of end-users.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/*/*


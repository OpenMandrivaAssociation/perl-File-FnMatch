%define module File-FnMatch
%define name perl-%{module}
%define version	0.02
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Simple filename and pathname matching
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org//CPAN/authors/id/M/MJ/MJP/File-FnMatch-0.02.tar.gz
Url:		http://search.cpan.org/~mjp/%{module}-%{version}/FnMatch.pm
BuildRoot:	%{_tmppath}/%{name}-buildroot/
BuildRequires:	perl-devel

%description
File::FnMatch::fnmatch() provides simple, shell-like pattern matching.

Though considerably less powerful than regular expressions, shell patterns
are nonetheless useful and familiar to a large audience of end-users.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/*/*


%define upstream_name    File-FnMatch
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    9

Summary:	Simple filename and pathname matching
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/~mjp/%{upstream_name}-%{upstream_version}/FnMatch.pm
Source0:	http://search.cpan.org//CPAN/authors/id/M/MJ/MJP/File-FnMatch-0.02.tar.gz

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-8mdv2012.0
+ Revision: 765242
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-7
+ Revision: 763755
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-6
+ Revision: 763244
- force it
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-5
+ Revision: 667140
- mass rebuild

* Sun Apr 03 2011 Funda Wang <fwang@mandriva.org> 0.20.0-4
+ Revision: 650065
- rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.20.0-3mdv2011.0
+ Revision: 564435
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 555284
- rebuild

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 409299
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.02-5mdv2009.1
+ Revision: 351748
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.02-4mdv2009.0
+ Revision: 223732
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.02-3mdv2008.1
+ Revision: 152076
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.02-2mdv2008.0
+ Revision: 23410
- rebuild


* Tue May 16 2006 Olivier Blin <oblin@mandriva.com> 0.02-1mdk
- initial Mandriva release


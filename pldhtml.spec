Summary:	PLD html pages
Summary(pl):	Strony html PLD
Name:		pldhtml
Version:	0.2
Release:	1
Group:		Documentation
Group(pl):	Dokumentacja
Copyright:	GPL
Vendor:		PLD
Source0:	%{name}-%{version}.tar.bz2
Obsoletes:	indexhtml
Provides:	indexhtml
BuildRoot:   	/tmp/%{name}-%{version}-root

%description
HTML pages of Polish(ed) Linux Distribution project.

%description -l pl
Strony html projektu PLD.

%prep
%setup  -q -n main

%build
find . -type d -name CVS |xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/doc/HTML

cp -pr * $RPM_BUILD_ROOT/usr/doc/HTML

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/usr/doc/HTML

%changelog
* Fri Mar 19 1999 Artur Frysiak <wiget@pld.org.pl>
  [1-1]
- initial release make from CVS

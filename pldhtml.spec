Summary:	PLD HTML pages
Summary(pl.UTF-8):	Strony HTML PLD
Name:		pldhtml
Version:	0.2
Release:	1
License:	GPL
Vendor:		PLD
Group:		Documentation
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	757042065994e36ae606138f67da1a6e
Obsoletes:	indexhtml
Provides:	indexhtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML pages of Polish(ed) Linux Distribution project.

%description -l pl.UTF-8
Strony HTML projektu PLD.

%prep
%setup  -q -n main

%build
find . -type d -name CVS |xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/doc/HTML

cp -pr * $RPM_BUILD_ROOT%{_datadir}/doc/HTML

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/doc/HTML

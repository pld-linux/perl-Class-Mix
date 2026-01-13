#
# Conditional build:
%bcond_without	tests	# unit tests

%define		pdir	Class
%define		pnam	Mix
Summary:	Class::Mix - dynamic class mixing
Summary(pl.UTF-8):	Class::Mix - dynamiczne mieszanie klas
Name:		perl-Class-Mix
Version:	0.006
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	14f9d08abf878afc1592f3861cf98be4
URL:		https://metacpan.org/dist/Class-Mix
BuildRequires:	perl-Params-Classify
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mix_class function provided by this module dynamically generates
`anonymous' classes with specified inheritance.

%description -l pl.UTF-8
Funkcja mix_class dostarczana przez ten moduł dynamicznie generuje
"anonimowe" klasy o określonym dziedziczeniu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
        --destdir=$RPM_BUILD_ROOT \
        --installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/Mix.pm
%{_mandir}/man3/Class::Mix.3pm*

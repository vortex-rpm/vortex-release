%define debug_package %{nil}

Summary:	Vortex repository configuration
Name:		vortex-release

%if 0%{?rhel} == 6

Version:	6
Release:	2.vortex%{?dist}
%global     _source1 vortex.repo

%else

Version:    7
Release:    2.vortex%{?dist}
%global     _source1 vortex-el7.repo

%endif

Vendor:		Vortex RPM
License:	GPLv3
Group:		System Environment/Base
URL:		http://vortex-rpm.org/
Source0:	RPM-GPG-KEY-VORTEX
Source1:	%{_source1}
Requires:	redhat-release >= %{version}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package contains Vortex repository GPG key and yum configuration.

%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
install -D -p -m 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-VORTEX
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/vortex.repo

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/vortex.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-VORTEX

%changelog
* Thu Jul 02 2015 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - %{version}-%{release}
- Tryig to make it work for both EL6 and EL7.

* Tue Sep 08 2011 Ilya A. Otyutskiy <sharp@thesharp.ru> - 6-1.vortex
- Initial packaging for Enterprise Linux (Closes LP: #843700)


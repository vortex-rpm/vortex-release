%define debug_package %{nil}

Summary:	Vortex repository configuration
Name:		vortex-release
Version:	5
Release:	1.vortex%{?dist}
License:	GPLv3
Group:		System Environment/Base
URL:		http://launchpad.net/vortex
Source0:	RPM-GPG-KEY-VORTEX
Source1:	vortex.repo
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
install -D -p -m 0644 RPM-GPG-KEY-VORTEX %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-VORTEX
install -D -p -m 0644 vortex.repo %{buildroot}%{_sysconfdir}/yum.repos.d/vortex.repo

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/vortex.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-VORTEX

%changelog
* Tue Aug 11 2011  Ilya A. Otyutskiy <sharp@thesharp.ru> 5-1.vortex
- Initial packaging for CentOS (Closes LP: #824754)


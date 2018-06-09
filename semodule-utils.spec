Summary:	SELinux developer tools for policy module packages
Summary(pl.UTF-8):	Narzędzia do tworzenia modułów polityk SELinuksa
Name:		semodule-utils
Version:	2.8
Release:	1
License:	GPL v2
Group:		Applications/System
#Source0Download: https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:	https://raw.githubusercontent.com/wiki/SELinuxProject/selinux/files/releases/20180524/%{name}-%{version}.tar.gz
# Source0-md5:	51c69e612481ce971e2ae825139d2ca0
URL:		https://github.com/SELinuxProject/selinux/wiki
BuildRequires:	libsepol-static >= 2.8
Requires:	libsepol >= 2.8
Conflicts:	policycoreutils < 2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Security-enhanced Linux is a patch of the Linux kernel and a number of
utilities with enhanced security functionality designed to add
mandatory access controls to Linux. The Security-enhanced Linux kernel
contains new architectural components originally developed to improve
the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds
of mandatory access control policies, including those based on the
concepts of Type Enforcement, Role-based Access Control, and
Multi-level Security.

This package contains SELinux developer tools for policy module
packages.

%description -l pl.UTF-8
Security-enhanced Linux jest prototypem jądra Linuksa i wielu
aplikacji użytkowych o funkcjach podwyższonego bezpieczeństwa.
Zaprojektowany jest tak, aby w prosty sposób ukazać znaczenie
obowiązkowej kontroli dostępu dla społeczności linuksowej. Ukazuje
również jak taką kontrolę można dodać do istniejącego systemu typu
Linux. Jądro SELinux zawiera nowe składniki architektury pierwotnie
opracowane w celu ulepszenia bezpieczeństwa systemu operacyjnego
Flask. Te elementy zapewniają ogólne wsparcie we wdrażaniu wielu typów
polityk obowiązkowej kontroli dostępu, włączając te wzorowane na: Type
Enforcement (TE), kontroli dostępu opartej na rolach (RBAC) i
zabezpieczeniach wielopoziomowych.

Ten pakiet zawiera narzędzia do tworzenia modułów polityk SELinuksa.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/semodule_expand
%attr(755,root,root) %{_bindir}/semodule_link
%attr(755,root,root) %{_bindir}/semodule_package
%attr(755,root,root) %{_bindir}/semodule_unpackage
%{_mandir}/man8/semodule_expand.8*
%{_mandir}/man8/semodule_link.8*
%{_mandir}/man8/semodule_package.8*
%{_mandir}/man8/semodule_unpackage.8*

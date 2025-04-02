#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.3.4
%define		qtver		5.15.2
%define		kpname		ocean-sound-theme
Summary:	Sound files for Plasma
Summary(pl.UTF-8):	Pliki dżwiękowe dla Plasmy
Name:		kp6-%{kpname}
Version:	6.3.4
Release:	1
License:	BSD-2-Clause/CC-BY-3.0/CC0-1.0/LGPL-3.0-or-later
Group:		X11/Applications/Sound
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	8bf1a7d70ee1571cf7ecdb9714b6170b
URL:		http://www.kde.org/
BuildRequires:	cmake >= 3.16.0
BuildRequires:	kf6-extra-cmake-modules >= 1.4.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	kp5-%{kpname} < %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sound files for Plasma. Ocean sound theme.

%description -l pl.UTF-8
Pliki dżwiękowe dla Plasmy. Temat muzyczny "Ocean".

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DBUILD_QT5=OFF \
	-DBUILD_QT6=ON
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/sounds/ocean

Name:           oberon-governor
Version:        1.0.0
Release:        1
Summary:        A GPU governor for the cyan-skillfish gpu in the bc-250
Source0: https://github.com/alexghow903/oberon-governor/archive/refs/heads/main.zip
URL: https://gitlab.com/mothenjoyer69/oberon-governor
License:        MIT
BuildRequires:  g++
BuildRequires:  libdrm-devel
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mock
%description
A GPU governor for the cyan-skillfish gpu in the bc-250\
%prep
%setup -n oberon-governor-main
%build
cmake .
%{make_build}
%install
%{make_install}
%files
/etc/oberon-config.yaml
/etc/systemd/system/oberon-governor.service
/var/usrlocal/bin/oberon-governor

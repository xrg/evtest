%define git_repo evtest
%define git_head HEAD

Name:		evtest
Version:    %git_get_ver
Release:    %mkrel %git_get_rel2
Summary:	A tool to print evdev kernel events
Group:		System/Kernel and hardware
License:	GPLv2+
URL:		https://cgit.freedesktop.org/evtest/
Source:     %git_bs_source %{name}-%{version}.tar.gz
BuildRequires: asciidoc
BuildRequires:	xsltproc
BuildRequires: xmlto-notex


%description
evtest displays information on the input device specified on the command line, including all the events supported by the device. It then monitors the device and displays all the events layer events generated.


%prep
%git_get_source
%setup -q

%build
./autogen.sh --prefix=%{_prefix}
%make


%install
%make_install PREFIX=%{_prefix}

%files
%doc COPYING README
%{_bindir}/*
%{_mandir}/man1/*

%changelog -f %{_sourcedir}/%{name}-changelog.gitrpm.txt

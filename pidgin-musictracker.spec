%define name pidgin-musictracker
%define version 0.4.8
%define release %mkrel 1

Summary: Plugin for Pidgin that displays the current song in the status
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://pidgin-musictracker.googlecode.com/files/%{name}-%{version}.tar.bz2
Patch: pidgin-musictracker-0.4.8-disable-werror.patch
License: GPLv2+
Group: Networking/Instant messaging
Url: http://code.google.com/p/pidgin-musictracker/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: pidgin-devel
BuildRequires: dbus-glib-devel
BuildRequires: xmms2-devel
Requires: pidgin

%description
Welcome to musictracker, a plugin for Pidgin which displays the music
track currently playing in your status.

Currently supported players: Amarok, Rhythmbox, Audacious, XMMS,
MPC/MPD, Exaile, Banshee, Quod Libet.


%prep
%setup -q
%patch -p1
autoreconf

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %buildroot%_libdir/pidgin/musictracker.{a,la}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS  THANKS AUTHORS
%_libdir/pidgin/musictracker.so


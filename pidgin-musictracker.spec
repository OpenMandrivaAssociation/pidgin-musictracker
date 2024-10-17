%define name pidgin-musictracker
%define version 0.4.22
%define release 4

Summary: Plugin for Pidgin that displays the current song in the status
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://pidgin-musictracker.googlecode.com/files/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Networking/Instant messaging
Url: https://code.google.com/p/pidgin-musictracker/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: pidgin-devel
BuildRequires: dbus-glib-devel >= 0.73
%if %mdvver <= 201000
BuildRequires: xmms2-devel
%endif
Requires: pidgin

%description
Welcome to musictracker, a plugin for Pidgin which displays the music
track currently playing in your status.

Currently supported players: Amarok, Rhythmbox, Audacious, XMMS,
MPC/MPD, Exaile, Banshee, Quod Libet.


%prep
%setup -q

%build
%configure2_5x --disable-werror
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %buildroot%_libdir/pidgin/musictracker.{a,la}

%find_lang musictracker

%clean
rm -rf %{buildroot}

%files -f musictracker.lang
%defattr(-,root,root)
%doc README NEWS  THANKS AUTHORS
%_libdir/pidgin/musictracker.so



%changelog
* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 0.4.22-3mdv2012.0
+ Revision: 773024
- relink against libpcre.so.1

* Wed Oct 19 2011 Götz Waschk <waschk@mandriva.org> 0.4.22-2
+ Revision: 705368
- disable Werror to make it build
- rebuild

* Mon Oct 18 2010 Götz Waschk <waschk@mandriva.org> 0.4.22-1mdv2011.0
+ Revision: 586614
- update to new version 0.4.22

* Thu Mar 04 2010 Götz Waschk <waschk@mandriva.org> 0.4.21-1mdv2010.1
+ Revision: 514116
- disable xmms2 support for Cooker
- new version 0.4.21

* Tue Sep 22 2009 Götz Waschk <waschk@mandriva.org> 0.4.20-1mdv2010.0
+ Revision: 447189
- update to new version 0.4.20

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 0.4.19-1mdv2010.0
+ Revision: 390502
- update to new version 0.4.19

* Tue May 12 2009 Götz Waschk <waschk@mandriva.org> 0.4.18-1mdv2010.0
+ Revision: 374909
- new version

* Tue Apr 28 2009 Götz Waschk <waschk@mandriva.org> 0.4.17-1mdv2010.0
+ Revision: 369099
- update to new version 0.4.17

* Thu Mar 19 2009 Götz Waschk <waschk@mandriva.org> 0.4.16-1mdv2009.1
+ Revision: 357842
- update to new version 0.4.16

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 0.4.15-1mdv2009.1
+ Revision: 347586
- new version
- drop patch
- disable moc debug output

* Mon Jan 12 2009 Götz Waschk <waschk@mandriva.org> 0.4.14-1mdv2009.1
+ Revision: 328585
- update to new version 0.4.14

* Fri Jan 09 2009 Götz Waschk <waschk@mandriva.org> 0.4.13-1mdv2009.1
+ Revision: 327423
- new version
- drop patch
- upate file list

* Thu Dec 04 2008 Götz Waschk <waschk@mandriva.org> 0.4.12-1mdv2009.1
+ Revision: 309962
- update to new version 0.4.12

* Tue Oct 14 2008 Götz Waschk <waschk@mandriva.org> 0.4.11-1mdv2009.1
+ Revision: 293544
- new version

* Wed Sep 24 2008 Götz Waschk <waschk@mandriva.org> 0.4.10-1mdv2009.0
+ Revision: 287739
- new version
- drop patch 1
- bump dbus-glib dep

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 0.4.8-2mdv2009.0
+ Revision: 286523
- fix crash with audacious

* Sun Sep 21 2008 Götz Waschk <waschk@mandriva.org> 0.4.8-1mdv2009.0
+ Revision: 286292
- new version
- update name and URLs
- fix build
- update build deps

* Thu Jul 03 2008 Götz Waschk <waschk@mandriva.org> 0.4.1-1mdv2009.0
+ Revision: 230929
- import pidgin-musictracker



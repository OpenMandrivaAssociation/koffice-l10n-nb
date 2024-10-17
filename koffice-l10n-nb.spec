Name: koffice-l10n-nb
Version: 2.3.2
Release: %mkrel 2
Summary: Language files for KOffice Norwegian
Group: System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
URL: https://www.koffice.org
BuildArch: noarch
Source: ftp://ftp.kde.org/pub/kde/stable/koffice-%version/src/koffice-l10n/%name-%version.tar.bz2
BuildRequires: gettext >= 0.15
BuildRequires: kdelibs4-devel
Requires: locales-nb
Requires: koffice-core
Provides: koffice-l10n

%description 
Provides Norwegian translations for KOffice.

%files 
%defattr(-,root,root,-)
%{_kde_datadir}/*/*/*

#------------------------------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot


%changelog
* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 2.3.2-2mdv2011.0
+ Revision: 639863
- rebuild

* Fri Feb 18 2011 Funda Wang <fwang@mandriva.org> 2.3.2-1
+ Revision: 638330
- New version 2.3.2

* Thu Jan 20 2011 Funda Wang <fwang@mandriva.org> 2.3.1-1
+ Revision: 631766
- New version 2.3.1

* Thu Dec 30 2010 Funda Wang <fwang@mandriva.org> 2.3.0-1mdv2011.0
+ Revision: 626267
- New version 2.3.0

* Thu Dec 09 2010 Funda Wang <fwang@mandriva.org> 2.2.91-1mdv2011.0
+ Revision: 617999
- New version 2.2.91

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 2.2.84-1mdv2011.0
+ Revision: 598546
- New version 2.2.84

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 2.2.83-1mdv2011.0
+ Revision: 589874
- New version 2.2.83

* Wed Oct 06 2010 Funda Wang <fwang@mandriva.org> 2.2.82-1mdv2011.0
+ Revision: 583751
- new version 2.2.82

* Wed Sep 15 2010 Funda Wang <fwang@mandriva.org> 2.2.81-1mdv2011.0
+ Revision: 578548
- new version 2.2.81

* Sat Aug 28 2010 Funda Wang <fwang@mandriva.org> 2.2.2-1mdv2011.0
+ Revision: 573633
- new version 2.2.2

* Sun Jul 11 2010 Funda Wang <fwang@mandriva.org> 2.2.1-1mdv2011.0
+ Revision: 550697
- new version 2.2.1

* Thu May 27 2010 Funda Wang <fwang@mandriva.org> 2.2.0-1mdv2010.1
+ Revision: 546378
- new version 2.2.0

* Wed Apr 28 2010 Funda Wang <fwang@mandriva.org> 2.1.91-1mdv2010.1
+ Revision: 540385
- new version 2.1.91

* Sat Apr 17 2010 Funda Wang <fwang@mandriva.org> 2.1.82-1mdv2010.1
+ Revision: 535943
- new version 2.1.82

* Thu Jan 14 2010 Funda Wang <fwang@mandriva.org> 2.1.1-1mdv2010.1
+ Revision: 491266
- new version 2.1.1

* Tue Nov 24 2009 Funda Wang <fwang@mandriva.org> 2.1.0-1mdv2010.1
+ Revision: 469532
- new version 2.1.0

* Fri Nov 13 2009 Funda Wang <fwang@mandriva.org> 2.0.91-1mdv2010.1
+ Revision: 465554
- new version 2.0.91

* Thu Sep 17 2009 Funda Wang <fwang@mandriva.org> 2.0.82-1mdv2010.0
+ Revision: 443743
- new version 2.0.82

* Thu Aug 13 2009 Funda Wang <fwang@mandriva.org> 2.0.2-1mdv2010.0
+ Revision: 415825
- new version 2.0.2

* Sat Jun 27 2009 Funda Wang <fwang@mandriva.org> 2.0.1-1mdv2010.0
+ Revision: 389670
- New version 2.0.1

* Thu Apr 09 2009 Funda Wang <fwang@mandriva.org> 1.9.99.0-1mdv2010.0
+ Revision: 365289
- new version 1.9.99.0

* Sat Jan 17 2009 Funda Wang <fwang@mandriva.org> 1.9.98.5-1mdv2009.1
+ Revision: 330495
- new version 1.9.98.5

* Thu Dec 11 2008 Funda Wang <fwang@mandriva.org> 1.9.98.3-1mdv2009.1
+ Revision: 312736
- new version 1.9.98.3

* Thu Nov 20 2008 Funda Wang <fwang@mandriva.org> 1.9.98.2-1mdv2009.1
+ Revision: 305053
- add source and spec
- Created package structure for koffice-l10n-nb.


* Wed May 24 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.1-1mdk
- 1.5.1

* Wed Apr 12 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.0-1mdk
- 1.5.0

* Thu Mar 30 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5-0.rc1.1mdk
- 1.5.0-rc1

* Mon Oct 17 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.2-1mdk
- 1.4.2

* Fri Aug 12 2005 Laurent MONTEL <lmontel@mandriva.com> 20mdk
- Remove conflict with kde-i18n

* Thu Jul 28 2005 Laurent MONTEL <lmontel@mandriva.com> 10mdk
- Fix provides koffice-l10n

* Mon Jul 25 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.1-1mdk
- 1.4.1

* Fri Jun 17 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.0-1mdk
- 1.4.0

* Tue Apr 19 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.91-1mdk
- 1.3.91

* Wed Nov 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.5-1mdk
- 1.3.5

* Wed Oct 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.4-1mdk
- 1.3.4

* Tue Sep 21 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.3-1mdk
- 1.3.3

* Tue May 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.1-1mdk
- 1.3.1

* Sat Apr 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.3-2mdk
- fix description
- fix obsolete-not-provided
- spec cosmetics

* Tue Jan 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-1mdk
- 1.3

* Fri Dec 19 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-0.rc2.1mdk
- rc2

* Fri Nov 28 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-0.rc1.2mdk
- Fix buildrequires

* Thu Jun 26 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-0.beta2.1mdk
- beta2


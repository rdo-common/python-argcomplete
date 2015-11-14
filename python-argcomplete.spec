%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%if 0%{?fedora}
%global with_python3 1
%endif

Summary:	Bash tab completion for argparse
Name:		python-argcomplete
Version:	1.0.0
Release:	1%{?dist}
License:	ASL 2.0
Group:		Development/Libraries
Url:		https://github.com/kislyuk/argcomplete
Source0:	http://pypi.python.org/packages/source/a/argcomplete/argcomplete-%{version}.tar.gz
BuildRequires:	python2-devel
BuildRequires:	python-setuptools
%if 0%{?with_python3}
BuildRequires:	python-tools
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%endif
BuildArch:	noarch
Requires:	python-argparse

%description
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

It makes two assumptions:

 * You're using bash as your shell
 * You're using argparse to manage your command line arguments/options

Argcomplete is particularly useful if your program has lots of
options or subparsers, and if your program can dynamically suggest
completions for your argument/option values (for example, if the user
is browsing resources over the network).

%package -n python2-argcomplete
Summary:     %{summary}
%if 0%{?with_python3} == 0
Provides:    /usr/bin/register-python-argcomplete
%endif
%{?python_provide:%python_provide python2-argcomplete}

%description -n python2-argcomplete
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

It makes two assumptions:

 * You're using bash as your shell
 * You're using argparse to manage your command line arguments/options

Argcomplete is particularly useful if your program has lots of
options or subparsers, and if your program can dynamically suggest
completions for your argument/option values (for example, if the user
is browsing resources over the network).

%if 0%{?with_python3}
%package -n python3-argcomplete
Summary:     %{summary}
Provides:    /usr/bin/register-python-argcomplete
%{?python_provide:%python_provide python3-argcomplete}

%description -n python3-argcomplete
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

It makes two assumptions:

 * You're using bash as your shell
 * You're using argparse to manage your command line arguments/options

Argcomplete is particularly useful if your program has lots of
options or subparsers, and if your program can dynamically suggest
completions for your argument/option values (for example, if the user
is browsing resources over the network).

%endif

%prep
%setup -n argcomplete-%{version} -q

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
%if 0%{?with_python3}
%py3_install
sed -i '1s|#!/usr/bin/python2|#!%{__python3}|' %{buildroot}%{_bindir}/*
%endif

%files -n python2-argcomplete
%license LICENSE.rst
%doc README.rst
%{python_sitelib}/argcomplete-%{version}-py*.egg-info
%{python_sitelib}/argcomplete/

%if 0%{?with_python3}
%files -n python3-argcomplete
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/argcomplete-%{version}-py*.egg-info
%{python3_sitelib}/argcomplete/
%endif

%{_bindir}/activate-global-python-argcomplete
%{_bindir}/python-argcomplete-check-easy-install-script
%{_bindir}/register-python-argcomplete

%changelog
* Sat Nov 14 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@laptop> - 1.0.0-1
- Update to latest version (#1227119)
- Use %license
- Update to new python packaging style
- Remove 2to3 invocation, the code is already python3 compatible
- Move scripts to python3 subpackage
- Add Provides:/usr/bin/register-python-activate so packages can depend on it

* Fri Nov 06 2015 Robert Kuska <rkuska@redhat.com> - 0.8.9-4
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 2 2015 - Steve Traylen <steve.traylen@cern.ch> 0.8.8-2
- Add python3 package (#1225934)

* Tue Jun 02 2015 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.8.9-1
- Update to 0.8.9 (#1227119)

* Tue May 5 2015 - Steve Traylen <steve.traylen@cern.ch> 0.8.8-1
- Updating package to 0.8.8

* Sun Dec 14 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 0.8.4-1
- Updating package to 0.8.4

* Fri Sep 12 2014 - Steve Traylen <steve.traylen@cern.ch> 0.8.1-1
- Updating package to 0.8.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 0.8.0-1
- Updating package to 0.8.0

* Sun Mar 30 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 0.7.1-1
- Updating package to 0.7.1

* Mon Mar 24 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 0.7.0-1
- Updating package to 0.7.0

* Mon Jan 13 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 0.6.7-2
- Removing '%exclude %{python_sitelib}/test' fom %files as no longer needed.

* Mon Jan 13 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 0.6.7-1
- Applying latest patch of argcomplete.

* Wed Jan 8 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 0.6.3-4
- Pushing new build for update as previous was not picked up.

* Wed Oct 16 2013 - Dale Macartney <dbmacartney@gmail.com> 0.6.3-3
- Correct missing files for el6

* Tue Oct 15 2013 - Dale Macartney <dbmacartney@gmail.com> 0.6.3-2
- Initial packaging for Fedora Project and including LICENSE.rst in docs

* Thu Jan 31 2013 - Marco Neciarini <marco.nenciarini@2ndquadrant.it> 0.3.5-1
- Initial packaging.

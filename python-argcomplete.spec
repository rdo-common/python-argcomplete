%global modname argcomplete

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{modname}
Summary:        Bash tab completion for argparse
Version:        1.0.0
Release:        3%{?dist}
License:        ASL 2.0
URL:		https://github.com/kislyuk/argcomplete
Source0:	http://pypi.python.org/packages/source/a/argcomplete/%{modname}-%{version}.tar.gz
BuildArch:	noarch

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

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%description -n python2-%{modname}
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

It makes two assumptions:

 * You're using bash as your shell
 * You're using argparse to manage your command line arguments/options

Argcomplete is particularly useful if your program has lots of
options or subparsers, and if your program can dynamically suggest
completions for your argument/option values (for example, if the user
is browsing resources over the network).

Python 2 version.

%if 0%{?with_python3}
%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python-tools
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{modname}
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

It makes two assumptions:

 * You're using bash as your shell
 * You're using argparse to manage your command line arguments/options

Argcomplete is particularly useful if your program has lots of
options or subparsers, and if your program can dynamically suggest
completions for your argument/option values (for example, if the user
is browsing resources over the network).

Python 3 version.
%endif

%prep
%setup -n %{modname}-%{version} -q

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python3}
%py3_install
for file in activate-global-python-argcomplete python-argcomplete-check-easy-install-script register-python-argcomplete ; do
mv %{buildroot}%{_bindir}/$file ./$file.py3
done
%endif

%py2_install
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/

%if 0%{?with_python3}
for file in activate-global-python-argcomplete python-argcomplete-check-easy-install-script register-python-argcomplete ; do
mv ./$file.py3 %{buildroot}%{_bindir}/$file
done
install -p -m0644 %{python3_sitelib}/%{modname}/bash_completion.d/python-argcomplete.sh %{buildroot}%{_sysconfdir}/bash_completion.d/
%else
install -p -m0644 %{python2_sitelib}/%{modname}/bash_completion.d/python-argcomplete.sh %{buildroot}%{_sysconfdir}/bash_completion.d/
%endif

%files -n python2-%{modname}
%license LICENSE.rst
%doc README.rst
%{python2_sitelib}/%{modname}*

%if 0%{?with_python3}
%files -n python3-%{modname}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/%{modname}*
%endif

# This goes in the python2-argcomplete package when we build without python3,
# otherwise it goes into the python3 subpackage
%{_bindir}/activate-global-python-argcomplete
%{_bindir}/python-argcomplete-check-easy-install-script
%{_bindir}/register-python-argcomplete
%{_sysconfdir}/bash_completion.d/python-argcomplete.sh

%changelog
* Sat Dec 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-3
- Ship bash completion file within RPM

* Sat Nov 14 2015 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.0-2
- A few minor changes to simplify and take care of cornercases

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

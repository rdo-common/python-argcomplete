%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary:	Bash tab completion for argparse
Name:		python-argcomplete
Version:	0.8.1
Release:	1%{?dist}
License:	ASL 2.0
Group:		Development/Libraries
Url:		https://github.com/kislyuk/argcomplete
Source0:	http://pypi.python.org/packages/source/a/argcomplete/argcomplete-%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:	python-setuptools
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

%prep
%setup -n argcomplete-%{version} -q

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.rst LICENSE.rst
%{_bindir}/activate-global-python-argcomplete
%{_bindir}/python-argcomplete-check-easy-install-script
%{_bindir}/register-python-argcomplete
%{python_sitelib}/argcomplete-%{version}-py*.egg-info
%{python_sitelib}/argcomplete/


%changelog
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

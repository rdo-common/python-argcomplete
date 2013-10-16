%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary: 	Bash tab completion for argparse
Name: 		python-argcomplete
Version: 	0.6.3
Release: 	3%{?dist}
License: 	ASL 2.0
Group: 		Development/Libraries
Url: 		https://github.com/kislyuk/argcomplete
Source0:	http://pypi.python.org/packages/source/a/argcomplete/argcomplete-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildArch: 	noarch
Requires:  	python-argparse

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
%doc README.rst
%doc LICENSE.rst
%{_bindir}/activate-global-python-argcomplete
%{_bindir}/python-argcomplete-check-easy-install-script
%{_bindir}/register-python-argcomplete
%{python_sitelib}/argcomplete-%{version}-py*.egg-info
%{python_sitelib}/argcomplete/
%exclude %{python_sitelib}/test


%changelog
* Wed Oct 16 2013 - Dale Macartney <dbmacartney@gmail.com> 0.6.3-3
- Correct missing files for el6

* Tue Oct 15 2013 - Dale Macartney <dbmacartney@gmail.com> 0.6.3-2
- Initial packaging for Fedora Project and including LICENSE.rst in %doc

* Thu Jan 31 2013 - Marco Neciarini <marco.nenciarini@2ndquadrant.it> 0.3.5-1
- Initial packaging.

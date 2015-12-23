%global srcname kuryr
%global docpath doc/build/html
%global upstream_version 0.1.0.dev220

%{!?upstream_version: %global upstream_version %{version}}

Name:          python-%{srcname}
Version:       0.1.0
Release:       0.1%{?dist}
Summary:       Kuryr Docker Plugin
Epoch:         1

License:       ASL 2.0
URL:           http://launchpad.net/kuryr
Source0:       https://tarballs.openstack.org/%{srcname}/%{srcname}-master.tar.gz
Source1:       kuryr.service

BuildArch:     noarch
BuildRequires: python2-devel
BuildRequires: python-oslo-sphinx
BuildRequires: python-pbr
BuildRequires: python-setuptools
BuildRequires: python-sphinx
BuildRequires: systemd-units

Summary:       Docker Plugin using Neutron as backend
Group:         Applications/System

Requires:      docker
Requires:      python-babel
Requires:      python-flask
Requires:      python-jsonschema
Requires:      python-netaddr
Requires:      python-oslo-concurrency
Requires:      python-oslo-serialization >= 1.4.0
Requires:      python-oslo-utils >= 1.4.0
Requires:      python-neutronclient
Requires:      python-pyroute2

%description
Kuryr is a Docker network plugin that uses Neutron to provide networking
services to Docker containers . It provides containerised images for the common
Neutron plugins.

%prep
%setup -q -n %{srcname}-%{upstream_version}


%build
# Dependences should be installed through yum/dnf
rm -f requirements.txt test-requirements.txt
%{__python2} setup.py build
# TODO(devvesa): skip this step until reno will be available on repositories
# %{__python2} setup.py build_sphinx

%install
# export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
# TODO(devvesa): skip this step until reno will be available on repositories
# %doc %{docpath}
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{upstream_version}-py%{python2_version}.egg-info
%{_bindir}/kuryr-server

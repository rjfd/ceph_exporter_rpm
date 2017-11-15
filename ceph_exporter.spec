#
# spec file for package golang-github-digitalocean-ceph_exporter
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
%global import_path     code.google.com/p/go.net


Name:           golang-github-digitalocean-ceph_exporter
Version:        1.1.0+git20171115.80aa3ff
Release:        0
License:        Apache-2.0
Summary:        Prometheus exporter for ceph cluster metrics
Url:            https://github.com/digitalocean/ceph_exporter
Group:          System/Management
Source:         ceph_exporter-%{version}.tar.gz
Source1:        prometheus-ceph_exporter.service
BuildRequires:  librados-devel
BuildRequires:  librbd-devel
BuildRequires:  systemd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Prometheus exporter that scrapes meta information about a running
ceph cluster.  All the information gathered from the cluster is done
by interacting with the monitors using an appropriate wrapper over
rados_mon_command(). Hence, no additional setup is necessary other
than having a working ceph cluster.

%prep
%setup -q -n ceph_exporter-%{version}
rm -rf vendor

%build
# set up temporary build gopath, and put our directory there
make

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 ./ceph_exporter %{buildroot}%{_bindir}/ceph_exporter
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/prometheus-ceph_exporter.service

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{_bindir}/ceph_exporter
%{_unitdir}/prometheus-ceph_exporter.service

%changelog


%global debug_package %{nil}
%global commit0 0ff469a701f5d7641818b616bf80af30e89c0fb6

Name: kind
Version: v0.9.0
Release:        1%{?dist}
Summary: Kubernetes IN Docker - local clusters for testing Kubernetes.

License: Apache License 2.0
URL: https://kind.sigs.k8s.io/
Source0: https://github.com/kubernetes-sigs/kind/archive/%{commit0}.tar.gz

ExclusiveArch: x86_64

%description
kind is a tool for running local Kubernetes clusters using Docker container "nodes".

%prep
%setup -n %{name}-%{commit0}


%build
%configure
%make_build


%install
%make_install


%check


%files
%license
%doc


%changelog
* Sun Jan 17 2021 Anthony Rabbito <hello@anthonyrabbito.com> - 0.9.0

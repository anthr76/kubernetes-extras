%global commit 0ff469a701f5d7641818b616bf80af30e89c0fb6
%global goipath sigs.k8s.io/kind
%global forgeurl https://github.com/kubernetes-sigs/kind

Version: v0.9.0

%gometa

%global common_description %{expand:kind is a tool for running local Kubernetes clusters using Docker container "nodes".}

%global golicenses    LICENSE
%global godocs        *.md

%global godevelheader %{expand:
# The devel package will usually benefit from corresponding project binaries.
Requires:  %{name} = %{version}-%{release}
}

Name:           %{goname}
Release:        7%{?dist}
Summary:        Kubernetes IN Docker - local clusters for testing Kubernetes.
License:        %{golicenses}
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%check
%gocheck

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Sun Jan 17 2021 Anthony Rabbito <hello@anthonyrabbito.com> - 0.9.0
v0.9.0 Focuses on stability enhancements following v0.8.0 / v0.8.1, a new wave of features will ship in v0.10.0.

Breaking changes have been kept to a minimum, primarily that Kubernetes v1.12.X is no longer supported to make way for some fixes requiring beta-grade kubeadm.

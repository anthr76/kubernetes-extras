%global goipath         sigs.k8s.io/kind
%global forgeurl 	https://github.com/kubernetes-sigs/kind
%global tag 		v0.9.0

%gometa

%global common_description %{expand:
Kubernetes IN Docker - local clusters for testing Kubernetes.}

%global golicenses      LICENSE
%global godocs          README.md OWNERS

Name:           kind
Release:        1%{?dist}
Summary:        Kubernetes IN Docker - local clusters for testing Kubernetes

License:        ASL 2.0

Version:	v0.9.0

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang >= 1.14
BuildRequires: golang(github.com/golangci/lint-1)

%if %{with check}
# Tests
BuildRequires:  golang(sigs.k8s.io/kind/pkg/internal/assert)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/internal/integration)
%endif

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
%gobuild -o %{gobuilddir}/bin/kind %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE %{golicenses}
%doc code-of-conduct.md CONTRIBUTING.md README.md
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Jan 18 17:39:05 EST 2021 anthr76 <hello@anthonyrabbito.com> - 0.9.0-1
- Initial package


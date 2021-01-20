%bcond_with check
%bcond_without snapshot

%global goipath         sigs.k8s.io/kind
%global forgeurl	https://github.com/kubernetes-sigs/kind


%if %{with snapshot}
%global commit          ee165688557465ff456077293061f344b05b130f
%gometa
Version:                0
Release:        	2%{?dist}
%else
%global tag             v0.9.0
Version:                0.9.0
%gometa
Release:        	6%{?dist}
%endif

%global common_description %{expand:
Kubernetes IN Docker - local clusters for testing Kubernetes.}

%global golicenses      LICENSE
%global godocs          README.md OWNERS

Name:           kind
Summary:        Kubernetes IN Docker - local clusters for testing Kubernetes

License:        ASL 2.0

URL:            %{gourl}
Source0:        %{gosource}

Source1:	bash-completion
Source2:	zsh-completion
Source3:	fish-completion

BuildRequires: golang >= 1.14

# HACK: These aren't correctly resolving or need to be packaged in copr.
BuildRequires: golang(github.com/golangci/lint-1)
BuildRequires: golang(github.com/alessio/shellescape)
BuildRequires: golang-gotest-devel
BuildRequires: golang-k8s-code-generator

BuildRequires:  golang(github.com/alessio/shellescape)
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/coreos/go-iptables/iptables)
BuildRequires:  golang(github.com/evanphx/json-patch/v5)
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(github.com/pelletier/go-toml)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/vishvananda/netlink)
BuildRequires:  golang(github.com/vishvananda/netlink/nl)
BuildRequires:  golang(gopkg.in/yaml.v3)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/sets)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/version)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/klog)
BuildRequires:  golang(k8s.io/utils/net)

%if %{with check}
BuildRequires: podman
BuildRequires: systemd
%endif


%description
%{common_description}

%gopkg

%prep
%goprep


%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%gobuild -o %{gobuilddir}/bin/kind %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

# shell completion
install -D -p -m 0644 %{S:1} %{buildroot}%{_datadir}/bash-completion/completions/kind
install -D -p -m 0644 %{S:2} %{buildroot}%{_datadir}/zsh/site-functions/_kind
install -D -p -m 0644 %{S:3} %{buildroot}%{_datadir}/fish/completions/kind.fish

# Disabling due to Docker deps. Will revist.
%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE %{golicenses}
%doc code-of-conduct.md CONTRIBUTING.md README.md
%doc %{godocs}
%{_bindir}/*
# filesystem owns all the parent directories here
%{_datadir}/bash-completion/completions/kind
# own parent directories in case zsh is not installed
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_kind
# own parent directories in case fish is not installed
%dir %{_datadir}/fish
%dir %{_datadir}/fish/completions
%{_datadir}/fish/completions/kind.fish

%gopkgfiles

%changelog
* Tue Jan 19 22:11:00 EST 2021 anthr76 <hello@anthonyrabbito.com> - 0-2
- Disable tests
* Tue Jan 19 21:50:00 EST 2021 anthr76 <hello@anthonyrabbito.com> - 0.9.0-6
- Lock versioning.
* Tue Jan 19 21:46:00 EST 2021 anthr76 <hello@anthonyrabbito.com> - 0-1
- Add a snapshot.
* Tue Jan 19 20:12:00 EST 2021 anthr76 <hello@anthonyrabbito.com> - 0.9.0-5
- Add snapshot support, and enable checks.
* Tue Jan 19 18:24:00 EST 2021 anthr76 <hello@anthonyrabbito.com> - 0.9.0-4
- Let filesystem own shell completions incase they're not installed.
* Tue Jan 19 18:07:00 EST 2021 anthr76 <hello@anthonyrabbito.com> - 0.9.0-3
- Add shell completions
* Tue Jan 19 00:19:00 EST 2021 anthr76 <hello@anthonyrabbito.com> - 0.9.0-2
- Change versioning schema
* Mon Jan 18 17:39:05 EST 2021 anthr76 <hello@anthonyrabbito.com> - 0.9.0-1
- Initial package

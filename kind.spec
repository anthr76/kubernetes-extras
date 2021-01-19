%bcond_without vendor
 
%if %{without vendor}
%bcond_without check
%endif

# https://github.com/kubernetes-sigs/kind
%global goipath         github.com/kubernetes-sigs/kind
Version:                v0.9.0

%gometa

%global common_description %{expand:
Kubernetes IN Docker - local clusters for testing Kubernetes.}

	
%global golicenses      LICENSE
%global godocs          README.md OWNERS


Name:           %{goname}
Release:        8%{?dist}
Summary:        Kubernetes IN Docker - local clusters for testing Kubernetes.
License:        %{golicenses}
URL:            %{gourl}
Source0:        %{gosource}

	
%if %{with vendor}
# git clone https://github.com/kubernetes-sigs/kind.git kind-%%{version}
# cd kind-%%{version}
# git checkout %%{version}
# go mod vendor
# cd ..
# tar --exclude .git -czf kind-%%{version}-vendored.tar.gz kind-%%{version}
Source0:        kind-%{version}-vendored.tar.gz
%else
Source0:        %{gosource}
%endif

BuildRequires: golang >= 1.14

%if %{with vendor}
Provides:  golang(github.com/alessio/shellescape)
Provides:  golang(github.com/BurntSushi/toml)
Provides:  golang(github.com/coreos/go-iptables/iptables)
Provides:  golang(github.com/evanphx/json-patch/v5)
Provides:  golang(github.com/golangci/golangci-lint/cmd/golangci-lint)
Provides:  golang(github.com/mattn/go-isatty)
Provides:  golang(github.com/pelletier/go-toml)
Provides:  golang(github.com/pkg/errors)
Provides:  golang(github.com/spf13/cobra)
Provides:  golang(github.com/spf13/pflag)
Provides:  golang(github.com/vishvananda/netlink)
Provides:  golang(github.com/vishvananda/netlink/nl)
Provides:  golang(gopkg.in/yaml.v3)
Provides:  golang(gotest.tools/gotestsum)
Provides:  golang(k8s.io/api/core/v1)
Provides:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
Provides:  golang(k8s.io/apimachinery/pkg/util/errors)
Provides:  golang(k8s.io/apimachinery/pkg/util/sets)
Provides:  golang(k8s.io/apimachinery/pkg/util/version)
Provides:  golang(k8s.io/client-go/kubernetes)
Provides:  golang(k8s.io/client-go/rest)
Provides:  golang(k8s.io/code-generator/cmd/deepcopy-gen)
Provides:  golang(k8s.io/klog)
Provides:  golang(k8s.io/utils/net)
Provides:  golang(sigs.k8s.io/kind/cmd/kind/app)
Provides:  golang(sigs.k8s.io/kind/pkg/apis/config/defaults)
Provides:  golang(sigs.k8s.io/kind/pkg/apis/config/v1alpha4)
Provides:  golang(sigs.k8s.io/kind/pkg/build/nodeimage)
Provides:  golang(sigs.k8s.io/kind/pkg/build/nodeimage/internal/container/docker)
Provides:  golang(sigs.k8s.io/kind/pkg/build/nodeimage/internal/kube)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/constants)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions/config)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions/installcni)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions/installstorage)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions/kubeadminit)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions/kubeadmjoin)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions/loadbalancer)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions/waitforready)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/delete)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/kubeadm)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/kubeconfig)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/kubeconfig/internal/kubeconfig)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/loadbalancer)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/logs)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/patch)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/providers)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/providers/common)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/providers/docker)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/internal/providers/podman)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/nodes)
Provides:  golang(sigs.k8s.io/kind/pkg/cluster/nodeutils)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/build)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/build/nodeimage)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/completion)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/completion/bash)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/completion/fish)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/completion/zsh)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/create)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/create/cluster)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/delete)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/delete/cluster)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/delete/clusters)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/export)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/export/kubeconfig)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/export/logs)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/get)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/get/clusters)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/get/kubeconfig)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/get/nodes)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/load)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/load/docker-image)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/load/image-archive)
Provides:  golang(sigs.k8s.io/kind/pkg/cmd/kind/version)
Provides:  golang(sigs.k8s.io/kind/pkg/errors)
Provides:  golang(sigs.k8s.io/kind/pkg/exec)
Provides:  golang(sigs.k8s.io/kind/pkg/fs)
Provides:  golang(sigs.k8s.io/kind/pkg/internal/apis/config)
Provides:  golang(sigs.k8s.io/kind/pkg/internal/apis/config/encoding)
Provides:  golang(sigs.k8s.io/kind/pkg/internal/cli)
Provides:  golang(sigs.k8s.io/kind/pkg/internal/env)
Provides:  golang(sigs.k8s.io/kind/pkg/internal/runtime)
Provides:  golang(sigs.k8s.io/kind/pkg/log)
Provides:  golang(sigs.k8s.io/yaml)
%else

BuildRequires:  golang(github.com/alessio/shellescape)
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/coreos/go-iptables/iptables)
BuildRequires:  golang(github.com/evanphx/json-patch/v5)
BuildRequires:  golang(github.com/golangci/golangci-lint/cmd/golangci-lint)
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(github.com/pelletier/go-toml)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/vishvananda/netlink)
BuildRequires:  golang(github.com/vishvananda/netlink/nl)
BuildRequires:  golang(gopkg.in/yaml.v3)
BuildRequires:  golang(gotest.tools/gotestsum)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/sets)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/version)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/code-generator/cmd/deepcopy-gen)
BuildRequires:  golang(k8s.io/klog)
BuildRequires:  golang(k8s.io/utils/net)
BuildRequires:  golang(sigs.k8s.io/kind/cmd/kind/app)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/apis/config/defaults)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/apis/config/v1alpha4)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/build/nodeimage)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/build/nodeimage/internal/container/docker)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/build/nodeimage/internal/kube)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/constants)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions/config)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions/installcni)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions/installstorage)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions/kubeadminit)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions/kubeadmjoin)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions/loadbalancer)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/create/actions/waitforready)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/delete)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/kubeadm)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/kubeconfig)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/kubeconfig/internal/kubeconfig)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/loadbalancer)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/logs)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/patch)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/providers)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/providers/common)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/providers/docker)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/internal/providers/podman)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/nodes)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cluster/nodeutils)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/build)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/build/nodeimage)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/completion)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/completion/bash)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/completion/fish)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/completion/zsh)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/create)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/create/cluster)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/delete)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/delete/cluster)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/delete/clusters)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/export)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/export/kubeconfig)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/export/logs)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/get)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/get/clusters)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/get/kubeconfig)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/get/nodes)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/load)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/load/docker-image)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/load/image-archive)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/cmd/kind/version)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/errors)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/exec)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/fs)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/internal/apis/config)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/internal/apis/config/encoding)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/internal/cli)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/internal/env)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/internal/runtime)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/log)
BuildRequires:  golang(sigs.k8s.io/yaml)

%if %{with check}
# Tests
BuildRequires:  golang(sigs.k8s.io/kind/pkg/internal/assert)
BuildRequires:  golang(sigs.k8s.io/kind/pkg/internal/integration)
%endif

%description
%{common_description}
	
%if %{without vendor}
%gopkg
%endif

%prep	
%if %{with vendor}
%goprep -k
%else
%goprep
%endif

BuildRequires: golang(https://github.com/alessio/shellescape)
BuildRequires: golang(https://github.com/golangci/golangci-lint/cmd/golangci-lint)
BuildRequires: golang(https://github.com/golangci/golangci-lint/tree/master/cmd/golangci-lint)
BuildRequires: golang(https://github.com/gotestyourself/gotestsum)
BuildRequires: golang(https://github.com/kubernetes/code-generator/tree/master/cmd/deepcopy-gen)

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%gobuild -o %{gobuilddir}/bin/kind %{goipath}

%install
%if %{without vendor}
%gopkginstall
%endif

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

%if %{without vendor}
%gopkgfiles
%endif

%changelog
* Mon Jan 18 13:40:10 EST 2021 anthr76 <hello@anthonyrabbito.com> - v0.9.0-10
- Initial package


# copr/kubernetes-extras

Fedora Copr repository for Kubernetes based apps. Please help contribute to add and update rpm specs based off Fedora's packaing guide lines.

TO-DO:
- Add OBS repo for OpenSUSE Tumbleweed based on SUSE packaging guidelines
- Add flatpak repo for CLI tool based applications
- Automate version releases
- Make upstream projects aware

## Current packages

| Name                                       | Build Status                                                                                                                                                                                                                                                                                    | Architecture      |                                                                                        Distros                                                                                               |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| golang-github-alessio-shellescape          | [![Copr build status](http://copr.fedorainfracloud.org/coprs/anthr76/kubernetes-extras/package/golang-github-alessio-shellescape/status_image/last_build.png?ts=1)](https://copr.fedorainfracloud.org/coprs/anthr76/kubernetes-extras/package/golang-github-alessio-shellescape/)                   | `arm64/amd64`     |                                                                                             Fedora 33, Fedora Rawhide                                                                        |
| kind                                       | [![Copr build status](http://copr.fedorainfracloud.org/coprs/anthr76/kubernetes-extras/package/kind/status_image/last_build.png?ts=1)](https://copr.fedorainfracloud.org/coprs/anthr76/kubernetes-extras/package/kind/)                                                                             | `arm64/amd64`     |                                                                                             Fedora 33, Fedora Rawhide                                                                        |

#### Usage

[Copr Page](https://copr.fedorainfracloud.org/coprs/anthr76/kubernetes-extras/)

```console
# dnf copr enable anthr76/kubernetes-extras
# dnf install <package>
```

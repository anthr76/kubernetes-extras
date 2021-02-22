# home:anthr76:kubernetes

Offline reproducible rpm builds for various Linux Distros.

This serves as an GitHub issue tracker and discussion point for the Kubernetes OBS repo. OBS and Git integration is tough but this repo can serve for requests of packages and issues for users not willing to interface with the OpenBuildService. In the future I would like to integrate automations to bump package versions, and etc while doing most of the logic on OBS but using some type of CI on GitHub. If you have any ideas on how to make that happen feel free to get in touch! Also don't hesitate to contribute.

The state of Dev-Ops CLI based application availability on Linux is *rough* to say the least. It's for good reason though. Building GoLang is tough. Perhaps in the future a majority if not all of all the Go apps won't have to be bundled but for now they are. 

## Current packages

TO-DO

#### Usage [^1]

[OBS Page](https://build.opensuse.org/project/show/home:anthr76:kubernetes)

![Fedora](https://software.opensuse.org/assets/download/fedora-69875974db5339cbd66d30d26f109a8b7ac22ae7e9cef6e3657193297780b689.png)

Fedora 33

```console
# dnf config-manager --add-repo https://download.opensuse.org/repositories/home:anthr76:kubernetes/Fedora_33/home:anthr76:kubernetes.repo
# dnf install <package>
```

Ubuntu 20.04/Pop_OS 20.04

```console
$ echo 'deb http://download.opensuse.org/repositories/home:/anthr76:/kubernetes/Ubuntu_20.04/ /' | sudo tee /etc/apt/sources.list.d/home:anthr76:kubernetes.list
$ curl -fsSL https://download.opensuse.org/repositories/home:anthr76:kubernetes/Ubuntu_20.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_anthr76_kubernetes.gpg > /dev/null
# apt update
# apt install <package>
```

Ubuntu 20.10/Pop_OS 20.10

```console
$ echo 'deb http://download.opensuse.org/repositories/home:/anthr76:/kubernetes/Ubuntu_20.04/ /' | sudo tee /etc/apt/sources.list.d/home:anthr76:kubernetes.list
$ curl -fsSL https://download.opensuse.org/repositories/home:anthr76:kubernetes/Ubuntu_20.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_anthr76_kubernetes.gpg > /dev/null
# apt update
# apt install <package>
```

[^1]: More exotic distros can be found [here](https://software.opensuse.org//download.html?project=home%3Aanthr76%3Akubernetes&package=flux) substitute flux for another package.

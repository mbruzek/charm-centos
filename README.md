# Overview

CentOS is a Linux distribution that provides a free, community supported 
platform which aims to be compatible with Red Hat Enterprise Linux (RHEL).

This charm provides a minimal CentOS image with the base CentOS operating
system.

# Usage

Juju 1.24.0 has initial support for CentOS (the Juju client is already 
supported on CentOS).  CentOS should be deployable on any cloud that supports
`cloud-init` on it's CentOS images. Check with the 
cloud provider and [Juju documentation](https://jujucharms.com/docs) for more
details about CentOS support.

To deploy the charm:

    juju deploy centos 

## Known Limitations and Issues

This charm may not deploy on all Juju environments, check with the cloud 
provider and [Juju documentation](https://jujucharms.com/docs) for more
details about CentOS support.

# Configuration

This charm has no configuration. It is a charm that deploys a minimal CentOS
image.

# Contact Information

This charm was created by Matt Bruzek <matthew.bruzek@canonical.com>

## Upstream Project Name

- [CentOS](https://www.centos.org)
- [CentOS wiki](https://wiki.centos.org/)
- [CentOS documentation](https://www.centos.org/docs/)
- [CentOS bug tracker](https://bugs.centos.org/my_view_page.php)
- [CentOS mailing lists](https://wiki.centos.org/GettingHelp/ListInfo)
- For help in real time, #centos on irc.freenode.net is a valuable source 
of information about CentOS issues.F

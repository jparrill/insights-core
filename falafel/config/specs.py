#!/usr/bin/env python

from falafel.config import SimpleFileSpec, PatternSpec, CommandSpec, format_rpm, json_format, First, All, NoneGroup
from falafel.config import DockerHostSimpleFileSpec, DockerHostPatternSpec, DockerHostCommandSpec


static_specs = {
    "nproc.conf"                : PatternSpec(r"etc/security/limits\.d/.*-nproc\.conf"),
    "display_java"              : CommandSpec("/usr/sbin/alternatives --display java"),
    "blkid"                     : CommandSpec("/usr/sbin/blkid -c /dev/null"),
    "bond"                      : PatternSpec(r"proc/net/bonding/bond.*"),
    "catalina.out"              : First([PatternSpec(r"var/log/tomcat.*/catalina\..+", large_content=True),
                                    PatternSpec(r"tomcat-logs/tomcat.*/catalina\..+", large_content=True)]),
    "cciss"                     : PatternSpec(r"proc/driver/cciss/cciss.*"),
    "chkconfig"                 : CommandSpec("/sbin/chkconfig --list"),
    "chronyc_sources"           : CommandSpec("/usr/bin/chronyc sources"),
    "cib.xml"                   : SimpleFileSpec("var/lib/pacemaker/cib/cib.xml"),
    "cinder.conf"               : SimpleFileSpec("etc/cinder/cinder.conf"),
    "cluster.conf"              : SimpleFileSpec("etc/cluster/cluster.conf"),
    "cmdline"                   : SimpleFileSpec("proc/cmdline"),
    "cpuinfo"                   : SimpleFileSpec("proc/cpuinfo"),
    "cobbler_settings"          : SimpleFileSpec("etc/cobbler/settings"),
    "cobbler_modules.conf"      : SimpleFileSpec("etc/cobbler/modules.conf"),
    "corosync"                  : SimpleFileSpec("etc/sysconfig/corosync"),
    "woopsie"                   : CommandSpec(r"/usr/bin/find /var/crash /var/tmp -path '*.reports-*/whoopsie-report'"),
    "current_clocksource"       : SimpleFileSpec("sys/devices/system/clocksource/clocksource0/current_clocksource"),
    "cpuinfo_max_freq"          : PatternSpec(r"sys/devices/system/cpu/cpu.*/cpufreq/cpuinfo_max_freq"),
    "date"                      : CommandSpec("/bin/date"),
    "date_iso"                  : CommandSpec("/bin/date --iso-8601=seconds"),
    "df_-alP"                   : CommandSpec("/usr/bin/df -alP"),
    "df_-al"                    : CommandSpec("/usr/bin/df -al"),
    "df_-li"                    : CommandSpec("/usr/bin/df -li"),
    "dig"                       : CommandSpec("/usr/bin/dig +dnssec . DNSKEY"),
    "dirsrv"                    : SimpleFileSpec("etc/sysconfig/dirsrv"),
    "dmesg"                     : CommandSpec("/bin/dmesg", large_content=True),
    "dmidecode"                 : CommandSpec("/usr/sbin/dmidecode"),
    "dumpe2fs-h"                : CommandSpec("/sbin/dumpe2fs -h {dumpdev}", dumpdev=r"\S+"),
    "docker_sysconfig"          : DockerHostSimpleFileSpec("etc/sysconfig/docker"),
    "docker_network"            : DockerHostSimpleFileSpec("etc/sysconfig/docker-network"),
    "docker_storage"            : DockerHostSimpleFileSpec("etc/sysconfig/docker-storage"),
    "docker_storage_setup"      : DockerHostSimpleFileSpec("etc/sysconfig/docker-storage-setup"),
    "docker_info"               : CommandSpec("/usr/bin/docker info"),
    "docker_list_images"        : CommandSpec("/usr/bin/docker images --all --no-trunc --digests"),
    "docker_list_containers"    : CommandSpec("/usr/bin/docker ps --all --no-trunc --size"),
    "docker_image_inspect"      : DockerHostCommandSpec("/usr/bin/docker inspect --type=image {DOCKER_IMAGE_NAME}"),
    "docker_container_inspect"  : DockerHostCommandSpec("/usr/bin/docker inspect --type=container {DOCKER_CONTAINER_NAME}"),
    "docker_host_machine-id"    : DockerHostSimpleFileSpec("etc/redhat-access-insights/machine-id"),
    "engine.log"                : SimpleFileSpec("var/log/ovirt-engine/engine.log"),
    "ethtool-a"                 : CommandSpec("/sbin/ethtool -a {iface}", iface=r"\S+"),
    "ethtool-c"                 : CommandSpec("/sbin/ethtool -c {iface}", iface=r"\S+"),
    "ethtool"                   : CommandSpec("/sbin/ethtool {iface}", iface=r"[^-]\S+"),
    "ethtool-g"                 : CommandSpec("/sbin/ethtool -g {iface}", iface=r"\S+"),
    "ethtool-i"                 : CommandSpec("/sbin/ethtool -i {iface}", iface=r"\S+"),
    "ethtool-k"                 : CommandSpec("/sbin/ethtool -k {iface}", iface=r"\S+"),
    "ethtool-S"                 : CommandSpec("/sbin/ethtool -S {iface}", iface=r"\S+"),
    "dcbtool_gc_dcb"            : CommandSpec("/sbin/dcbtool gc {iface} dcb", iface=r"\S+"),
    "exim.conf"                 : SimpleFileSpec("etc/exim.conf"),
    "fdisk-l"                   : CommandSpec("/sbin/fdisk -l"),
    "fstab"                     : SimpleFileSpec("etc/fstab"),
    "foreman_production.log"    : SimpleFileSpec("var/log/foreman/production.log", large_content=True),
    "galera.cnf"                : SimpleFileSpec("etc/my.cnf.d/galera.cnf"),
    "getenforce"                : CommandSpec("/usr/sbin/getenforce"),
    "getsebool"                 : CommandSpec("/usr/sbin/getsebool -a"),
    "glance-api.conf"           : SimpleFileSpec("etc/glance/glance-api.conf"),
    "glance-cache.conf"         : SimpleFileSpec("etc/glance/glance-cache.conf"),
    "glance-registry.conf"      : SimpleFileSpec("etc/glance/glance-registry.conf"),
    "grub2.cfg"                 : SimpleFileSpec("boot/grub2/grub.cfg"),
    "grub.conf"                 : SimpleFileSpec("boot/grub/grub.conf"),
    "grub_config_perms"         : CommandSpec("/usr/bin/ls -l /boot/grub2/grub.cfg"),
    "haproxy_cfg"               : SimpleFileSpec("etc/haproxy/haproxy.cfg"),
    "heat.conf"                 : SimpleFileSpec("etc/heat/heat.conf"),
    "heat_crontab"              : CommandSpec("/usr/bin/crontab -l -u heat"),
    "hostname"                  : First([CommandSpec("/bin/hostname"),
                                    SimpleFileSpec("hostname")]),
    "hosts"                     : SimpleFileSpec("etc/hosts"),
    "hponcfg-g"                 : CommandSpec("hponcfg -g"),
    "sysconfig_httpd"           : SimpleFileSpec("etc/sysconfig/httpd"),
    "httpd_access_log"          : SimpleFileSpec("var/log/httpd/access_log", large_content=True),
    "httpd.conf"                : PatternSpec(r"etc/httpd/conf/httpd\.conf"),
    "httpd.conf.d"              : PatternSpec(r"etc/httpd/conf\.d/.+\.conf"),
    "httpd_ssl_access_log"      : SimpleFileSpec("var/log/httpd/ssl_access_log", large_content=True),
    "ifcfg"                     : PatternSpec(r"etc/sysconfig/network-scripts/ifcfg-.*"),
    "ifconfig"                  : CommandSpec("/sbin/ifconfig -a"),
    "imagemagick_policy"        : PatternSpec(r"etc/ImageMagick.*/policy\.xml"),
    "init.ora"                  : SimpleFileSpec("{ORACLE_HOME}/dbs/init.ora"),
    "installed-rpms"            : First([CommandSpec("/bin/rpm -qa --qf='%s'" % format_rpm(), multi_output=False),
                                   CommandSpec("/bin/rpm -qa --qf='%s'" % format_rpm(1), multi_output=False),
                                   CommandSpec("/bin/rpm -qa --qf='%s'" % format_rpm(3), multi_output=False),
                                   CommandSpec("/bin/rpm -qa --qf='%s'" % json_format(), multi_output=False),
                                   SimpleFileSpec("installed-rpms"),
                                   SimpleFileSpec("rpm-manifest")]),
    "interrupts"                : SimpleFileSpec("proc/interrupts"),
    "ip_addr"                   : CommandSpec("/sbin/ip addr"),
    "ip_route_show_table_all"   : CommandSpec("/sbin/ip route show table all"),
    "iptables"                  : CommandSpec("/sbin/iptables-save"),
    "ipv4_neigh"                : CommandSpec("/sbin/ip -4 neighbor show nud all"),
    "kdump.conf"                : SimpleFileSpec("etc/kdump.conf"),
    "kdump"                     : SimpleFileSpec("etc/sysconfig/kdump"),
    "kexec_crash_loaded"        : SimpleFileSpec("sys/kernel/kexec_crash_loaded"),
    "keystone_crontab"          : CommandSpec("/usr/bin/crontab -l -u keystone"),
    "keystone.conf"             : SimpleFileSpec("etc/keystone/keystone.conf"),
    "ksmstate"                  : SimpleFileSpec("sys/kernel/mm/ksm/run"),
    "libvirtd.log"              : SimpleFileSpec("var/log/libvirt/libvirtd.log"),
    "limits.conf"               : SimpleFileSpec("etc/security/limits.conf"),
    "limits.d"                  : PatternSpec(r"etc/security/limits\.d/.*"),
    "locale"                    : CommandSpec("/usr/bin/locale"),
    "lsblk"                     : CommandSpec("/bin/lsblk"),
    "lscpu"                     : CommandSpec("/usr/bin/lscpu"),
    "lsinitrd_lvm.conf"         : All([CommandSpec("/sbin/lsinitrd -f /etc/lvm/lvm.conf"),
                                    CommandSpec("/usr/bin/lsinitrd -f /etc/lvm/lvm.conf")]),
    "lsof"                      : CommandSpec("lsof", large_content=True),
    "ls_boot"                   : CommandSpec("/bin/ls -lanR /boot"),
    "ls_dev"                    : CommandSpec("/bin/ls -lanR /dev"),
    "ls_etc"                    : CommandSpec("/bin/ls -lanR /etc"),
    "lsmod"                     : CommandSpec("/sbin/lsmod"),
    "lspci"                     : CommandSpec("/sbin/lspci"),
    "lvm.conf"                  : SimpleFileSpec("etc/lvm/lvm.conf"),
    "lvs"                       : NoneGroup([CommandSpec('/sbin/lvs -a -o +lv_tags,devices --config="global{locking_type=0}"')]),
    "lvs_noheadings"            : CommandSpec("/sbin/lvs --nameprefixes --noheadings --separator='|' -a -o lv_name,vg_name,lv_size,region_size,mirror_log,lv_attr,devices,region_size --config=\"global{locking_type=0}\""),
    "mdstat"                    : SimpleFileSpec("proc/mdstat"),
    "meminfo"                   : SimpleFileSpec("proc/meminfo"),
    "messages"                  : SimpleFileSpec("var/log/messages", large_content=True),
    "modinfo"                   : CommandSpec("/usr/sbin/modinfo {module}", module=r"\S+"),
    "modprobe.conf"             : SimpleFileSpec("etc/modprobe.conf"),
    "modprobe.d"                : PatternSpec(r"etc/modprobe\.d/.*\.conf"),
    "mount"                     : CommandSpec("/bin/mount"),
    "multipath.conf"            : SimpleFileSpec("etc/multipath.conf"),
    "multipath_-v4_-ll"         : CommandSpec("/sbin/multipath -v4 -ll"),
    "named-checkconf_p"         : CommandSpec("/usr/sbin/named-checkconf -p"),
    "netconsole"                : SimpleFileSpec("etc/sysconfig/netconsole"),
    "netstat"                   : CommandSpec("/bin/netstat -neopa"),
    "netstat-s"                 : CommandSpec("/bin/netstat -s"),
    "netstat_-agn"              : CommandSpec("/bin/netstat -agn"),
    "neutron.conf"              : SimpleFileSpec("etc/neutron/neutron.conf"),
    "neutron_plugin.ini"        : SimpleFileSpec("etc/neutron/plugin.ini"),
    "nfnetlink_queue"           : SimpleFileSpec("proc/net/netfilter/nfnetlink_queue"),
    "nova.conf"                 : SimpleFileSpec("etc/nova/nova.conf"),
    "nscd.conf"                 : SimpleFileSpec("etc/nscd.conf"),
    "nsswitch.conf"             : SimpleFileSpec("etc/nsswitch.conf"),
    "ntpq_pn"                   : CommandSpec("/usr/sbin/ntpq -pn"),
    "ovirt_engine_confd"        : PatternSpec(r"etc/ovirt-engine/engine\.conf\.d/.*"),
    "ovirt_engine_server.log"   : SimpleFileSpec("var/log/ovirt-engine/server.log"),
    "ovs-vsctl_show"            : CommandSpec("/usr/bin/ovs-vsctl show"),
    "pacemaker.log"             : SimpleFileSpec("var/log/pacemaker.log"),
    "parted_-l"                 : CommandSpec("/sbin/parted -l"),
    "password-auth"             : SimpleFileSpec("etc/pam.d/password-auth"),
    "pluginconf.d"              : PatternSpec(r"etc/yum/pluginconf\.d/\w+\.conf"),
    "postgresql.conf"           : All([SimpleFileSpec("var/lib/pgsql/data/postgresql.conf"),
                                    SimpleFileSpec("opt/rh/postgresql92/root/var/lib/pgsql/data/postgresql.conf")]),
    "postgresql.log"            : All([PatternSpec(r"var/lib/pgsql/data/pg_log/postgresql-.+\.log", large_content=True),
                                    PatternSpec(r"opt/rh/postgresql92/root/var/lib/pgsql/data/pg_log/postgresql-.+\.log", large_content=True)]),
    "ps_aux"                    : CommandSpec("/bin/ps aux"),
    "ps_auxcww"                 : CommandSpec("/bin/ps auxcww"),
    "pvs"                       : NoneGroup([CommandSpec('/sbin/pvs -a -v -o +pv_mda_free,pv_mda_size,pv_mda_count,pv_mda_used_count,pe_count --config="global{locking_type=0}"')]),
    "pvs_noheadings"            : CommandSpec("/sbin/pvs --nameprefixes --noheadings --separator='|' -a -o pv_all,vg_name --config=\"global{locking_type=0}\""),
    "spfile.ora"                : PatternSpec(r"{ORACLE_HOME}/dbs/spfile.*\.ora"),
    "rabbitmq_policies"         : CommandSpec("rabbitmqctl list_policies"),
    "rabbitmq_queues"           : CommandSpec("rabbitmqctl list_queues name messages consumers auto_delete"),
    "rabbitmq_report"           : CommandSpec("rabbitmqctl report"),
    "rc.local"                  : SimpleFileSpec("etc/rc.d/rc.local"),
    "redhat-release"            : SimpleFileSpec("etc/redhat-release"),
    "resolv.conf"               : SimpleFileSpec("etc/resolv.conf"),
    "rhn.conf"                  : First([SimpleFileSpec("etc/rhn/rhn.conf"),
                                    SimpleFileSpec("conf/rhn/rhn/rhn.conf")]),
    "rhn-charsets"              : First([CommandSpec("/usr/bin/rhn-charsets"),
                                    SimpleFileSpec("database-character-sets")]),
    "rhn-entitlement-cert.xml"  : First([PatternSpec(r"etc/sysconfig/rhn/rhn-entitlement-cert\.xml.*"),
                                    PatternSpec(r"conf/rhn/sysconfig/rhn/rhn-entitlement-cert\.xml.*")]),
    "rhn_hibernate.conf"        : SimpleFileSpec("usr/share/rhn/config-defaults/rhn_hibernate.conf"),
    "rhn-schema-version"        : First([CommandSpec("/usr/bin/rhn-schema-version"),
                                    SimpleFileSpec("database-schema-version")]),
    "rhn-schema-stats"          : First([CommandSpec("/usr/bin/rhn-schema-stats -"),
                                    SimpleFileSpec("database/schema-stats.log")]),
    "rhn_server_xmlrpc.log"     : SimpleFileSpec("var/log/rhn/rhn_server_xmlrpc.log", large_content=True),
    "rhn_taskomatic_daemon.log" : SimpleFileSpec("var/log/rhn/rhn_taskomatic_daemon.log", large_content=True),
    "root_crontab"              : CommandSpec("/usr/bin/crontab -l -u root"),
    "route"                     : First([CommandSpec("/sbin/route -n"),
                                    SimpleFileSpec("route")]),
    "rpm_-V_packages"           : CommandSpec("/bin/rpm -V coreutils procps procps-ng shadow-utils passwd sudo"),
    "rsyslog.conf"              : SimpleFileSpec("etc/rsyslog.conf"),
    "samba"                     : SimpleFileSpec("etc/samba/smb.conf"),
    "satellite_version.rb"      : First([SimpleFileSpec("usr/share/foreman/lib/satellite/version.rb"),
                                    SimpleFileSpec("satellite_version")]),
    "scsi"                      : SimpleFileSpec("proc/scsi/scsi"),
    "secure"                    : SimpleFileSpec("var/log/secure", large_content=True),
    "selinux-config"            : SimpleFileSpec("etc/selinux/config"),
    "sestatus"                  : CommandSpec("/usr/sbin/sestatus -b"),
    "slapd_errors"              : PatternSpec(r"var/log/dirsrv/slapd-.*/errors"),
    "ssh_config"                : SimpleFileSpec("etc/ssh/ssh_config"),
    "sshd_config"               : SimpleFileSpec("etc/ssh/sshd_config"),
    "sshd_config_perms"         : CommandSpec("ls -l /etc/ssh/sshd_config"),
    "sysctl"                    : CommandSpec("/sbin/sysctl -a"),
    "sysctl.conf"               : SimpleFileSpec("etc/sysctl.conf"),
    "sysctl.conf_initramfs"     : CommandSpec("/usr/bin/lsinitrd /boot/initramfs-*kdump.img -f /etc/sysctl.conf /etc/sysctl.d/*.conf"),
    "systemctl_list-unit-files" : CommandSpec("systemctl list-unit-files"),
    "systemd_system.conf"       : SimpleFileSpec("etc/systemd/system.conf"),
    "systemd_docker"            : SimpleFileSpec("usr/lib/systemd/system/docker.service"),
    "systemid"                  : SimpleFileSpec("etc/sysconfig/rhn/systemid"),
    "tomcat_web.xml"            : First([PatternSpec(r"etc/tomcat.*/web\.xml"),
                                    PatternSpec(r"conf/tomcat/tomcat.*/web\.xml")]),
    "udev-persistent-net.rules" : SimpleFileSpec("etc/udev/rules.d/70-persistent-net.rules"),
    "uname"                     : CommandSpec("/bin/uname -a"),
    "up2date"                   : SimpleFileSpec("etc/sysconfig/rhn/up2date"),
    "uptime"                    : CommandSpec("/usr/bin/uptime"),
    "vgdisplay"                 : CommandSpec("/sbin/vgdisplay"),
    "vgs"                       : NoneGroup([CommandSpec('/sbin/vgs -v -o +vg_mda_count,vg_mda_free,vg_mda_size,vg_mda_used_count,vg_tags --config="global{locking_type=0}"')]),
    "vgs_noheadings"            : CommandSpec("/sbin/vgs --nameprefixes --noheadings --separator='|' -a -o vg_all --config=\"global{locking_type=0}\""),
    "vdsm.conf"                 : SimpleFileSpec("etc/vdsm/vdsm.conf"),
    "vdsm.log"                  : SimpleFileSpec("var/log/vdsm/vdsm.log"),
    "virt-what"                 : CommandSpec("/usr/sbin/virt-what"),
    "vmcore-dmesg"              : PatternSpec(r"var/crash/.*/vmcore-dmesg\.txt", large_content=True),
    "vsftpd.conf"               : SimpleFileSpec("etc/vsftpd/vsftpd.conf"),
    "vsftpd"                    : SimpleFileSpec("etc/pam.d/vsftpd"),
    "yum-repolist"              : CommandSpec("/usr/bin/yum -C repolist"),
    "yum.log"                   : SimpleFileSpec("var/log/yum.log"),
    "yum.repos.d"               : PatternSpec(r"etc/yum\.repos\.d/.*")

}

pre_commands = {
    "iface": "/sbin/ip -o link | awk -F ': ' '/.*link\\/ether/ {print $2}'",
    "block": "/bin/ls /sys/block | awk '!/^ram|^\\.+$/ {print \"/dev/\" $1 \" unit s print\"}'",
    "module": "/bin/ls /sys/module"
}

meta_files = {
    "machine-id"                : SimpleFileSpec("etc/redhat-access-insights/machine-id"),
    "branch_info"               : SimpleFileSpec("branch_info"),
    "uploader_log"              : SimpleFileSpec("var/log/redhat-access-insights/redhat-access-insights.log"),
    "metadata.json"             : SimpleFileSpec("metadata.json")
}

# flake8: noqa

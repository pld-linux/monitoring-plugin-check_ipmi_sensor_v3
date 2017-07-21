%define		plugin	check_ipmi_sensor_v3
Summary:	Monitoring plugin to check IPMI sensors
Name:		nagios-plugin-%{plugin}
Version:	3.12
Release:	0.1
License:	GPL v3+
Group:		Networking
Source0:	https://github.com/thomas-krenn/check_ipmi_sensor_v3/archive/v%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	74fbfcc48bdbb6e4101f2fcaaea248a1
URL:		https://www.thomas-krenn.com/en/wiki/IPMI_Sensor_Monitoring_Plugin
BuildRequires:	rpmbuild(macros) >= 1.685
Requires:	nagios-common >= 3.2.3-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Nagios/Icinga plugin to check IPMI sensors.

%prep
%setup -q -n %{plugin}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{nrpeddir},%{plugindir},%{cachedir}}
install -p check_ipmi_sensor $RPM_BUILD_ROOT%{plugindir}/%{plugin}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changelog.txt
%doc contrib/default-combinedgraph.template
%attr(755,root,root) %{plugindir}/%{plugin}

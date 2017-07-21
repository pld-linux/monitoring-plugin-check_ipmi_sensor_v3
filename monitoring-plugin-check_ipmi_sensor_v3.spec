%define		plugin	check_ipmi_sensor_v3
%include	/usr/lib/rpm/macros.perl
Summary:	Monitoring plugin to check IPMI sensors
Name:		monitoring-plugin-%{plugin}
Version:	3.12
Release:	0.5
License:	GPL v3+
Group:		Networking
Source0:	https://github.com/thomas-krenn/check_ipmi_sensor_v3/archive/v%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	74fbfcc48bdbb6e4101f2fcaaea248a1
Source1:	%{plugin}.cfg
URL:		https://www.thomas-krenn.com/en/wiki/IPMI_Sensor_Monitoring_Plugin
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.685
Requires:	freeipmi
Requires:	nagios-common >= 3.2.3-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		nrpeddir	/etc/nagios/nrpe.d
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Nagios/Icinga plugin to check IPMI sensors.

%prep
%setup -q -n %{plugin}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{nrpeddir},%{plugindir}}
install -p check_ipmi_sensor $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg
touch $RPM_BUILD_ROOT%{nrpeddir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- nagios-nrpe
%nagios_nrpe -a %{plugin} -f %{_sysconfdir}/%{plugin}.cfg

%triggerun -- nagios-nrpe
%nagios_nrpe -d %{plugin} -f %{_sysconfdir}/%{plugin}.cfg

%files
%defattr(644,root,root,755)
%doc README changelog.txt
%doc contrib/default-combinedgraph.template
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%ghost %{nrpeddir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}

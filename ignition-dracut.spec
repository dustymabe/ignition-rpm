%global debug_package %{nil}
%global dracutlibdir %{_prefix}/lib/dracut

%global provider        github
%global provider_tld    com
%global project         dustymabe
%global repo            bootengine
# https://github.com/dustymabe/bootengine
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          bf3b454db89bcff82d01b472786821bd458d3593
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           ignition-dracut
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Dracut modules for ignition

License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

Requires: ignition
Requires: dracut
Requires: dracut-network

BuildArchitectures: noarch

%description
Dracut modules for ignition to enable ignition services to run in the
initramfs on boot.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
# dracut modules
install -d -p %{buildroot}/%{dracutlibdir}/modules.d
rm ./dracut/README.txt
cp -r ./dracut/* %{buildroot}/%{dracutlibdir}/modules.d/

%files
%doc README.md
%license LICENSE
%defattr(-,root,root,0755)
%{dracutlibdir}/modules.d/30ignition
%{dracutlibdir}/modules.d/99journald-conf

%changelog
* Thu Jun 21 2018 Dusty Mabe <dusty@dustymabe.com> - 0-0.1.gitbf3b454
- First package for Fedora

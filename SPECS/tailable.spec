Name:           tailable
Version:        0.0
Release:        1%{?dist}
Summary:        Prints new lines in watched file

Group:          Applications/File
License:        BSD
URL:            https://github.com/LukasNormantas-awin/tailable
Source0:        https://github.com/LukasNormantas-awin/%{name}/archive/v%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      x86_64 
Packager:       Lukas Normantas

%description
This application reads and outputs lines from the tail of a file. It keeps a track of how many lines has it read already and only reads new lines.

%prep
%setup -q

%build
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/usr/local/bin
%{__install} -m 755 tailable %{buildroot}/usr/local/bin/tailable

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir /usr/local/bin
/usr/local/bin/tailable

%changelog

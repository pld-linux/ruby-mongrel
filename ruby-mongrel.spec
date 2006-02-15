Summary:	Ruby webserver toolkit
Name:		ruby-mongrel
Version:	0.3.3
Release:	1
License:	Ruby
Source0:	http://rubyforge.org/frs/download.php/8600/mongrel-%{version}.tgz
# Source0-md5:	4adb811d349e14403de9672572eaa059
Group:		Development/Libraries
URL:		http://mongrel.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n mongrel-%{version}

%build
ruby setup.rb config --rbdir=%{ruby_rubylibdir} --sodir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*.rb
%{ruby_rubylibdir}/mongrel/
%attr(755,root,root) %{ruby_archdir}/*.so

Summary:	Ruby webserver toolkit
Summary(pl):	Toolkit jêzyka Ruby dla serwera WWW
Name:		ruby-mongrel
Version:	0.3.13.4
Release:	1
License:	Ruby
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/13231/mongrel-%{version}.gem
# Source0-md5:	3fc1970ca01d06c39c2b40e503f07b88
Patch0:		%{name}-nogems.patch
URL:		http://mongrel.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby webserver toolkit.

%description -l pl
Toolkit jêzyka Ruby dla serwera WWW.

%prep
%setup -q -c -T
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
%patch0 -p1

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
%{ruby_rubylibdir}/mongrel
%attr(755,root,root) %{ruby_archdir}/*.so

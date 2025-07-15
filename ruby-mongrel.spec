%define pkgname mongrel
Summary:	Ruby webserver toolkit
Summary(pl.UTF-8):	Toolkit języka Ruby dla serwera WWW
Name:		ruby-%{pkgname}
Version:	1.1.5
Release:	12
License:	Ruby
Group:		Development/Libraries
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	a37617eb48f0932cc32143b2d76c0d12
Patch0:		%{name}-nogems.patch
Patch1:		%{name}-ruby1.9.patch
Patch2:		format-security.patch
URL:		https://rubygems.org/gems/mongrel
BuildRequires:	dos2unix
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-irb
BuildRequires:	ruby-modules
BuildRequires:	setup.rb >= 3.4.1-6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby webserver toolkit.

%description -l pl.UTF-8
Toolkit języka Ruby dla serwera WWW.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4
BuildArch:	noarch

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby
BuildArch:	noarch

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README  -o -print | xargs touch --reference %{SOURCE0}
dos2unix examples/mongrel_simple_service.rb
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

find -name '*.rb' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'

cp %{_datadir}/setup.rb .

%build
# passing CFLAGS breaks -fPIC parsing,
# patch mkmf module to be able to pass CC and OPTFLAGS
%{__ruby} setup.rb config \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--datadir=%{_datadir} \
	--mandir=%{_mandir} \
	--sysconfdir=%{_sysconfdir} \
	--localstatedir=%{_localstatedir} \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir} \
	--make-prog="%{__make} CC=\"%{__cc}\""

%{__ruby} setup.rb setup

rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -r ri/{IO,Kernel,RequestLog,TCPServer}
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

%{__ruby} setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*.rb
%{ruby_rubylibdir}/mongrel
%attr(755,root,root) %{ruby_archdir}/*.so

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Mongrel*

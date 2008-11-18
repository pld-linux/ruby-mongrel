Summary:	Ruby webserver toolkit
Summary(pl.UTF-8):	Toolkit języka Ruby dla serwera WWW
Name:		ruby-mongrel
Version:	1.1.1
Release:	3
License:	Ruby
Group:		Development/Libraries
Source0:	http://mongrel.rubyforge.org/releases/gems/mongrel-%{version}.gem
# Source0-md5:	6abbf97ba32a24614230076bfc77034b
Patch0:		%{name}-nogems.patch
URL:		http://mongrel.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# passing CFLAGS breaks -fPIC parsing, patch mkmf module to be able to pass CC and OPTFLAgs

%define	ruby_config {\
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
		--make-prog="%{__make} CC=\"%{__cc}\"" \
}

%define	ruby_setup { \
	%{__ruby} setup.rb setup \
}

%define ruby_install { \
	%{__ruby} setup.rb install \
}

%description
Ruby webserver toolkit.

%description -l pl.UTF-8
Toolkit języka Ruby dla serwera WWW.

%prep
%setup -q -c -T
tar xf %{SOURCE0} -O data.tar.gz | tar xz
%patch0 -p1

find -name '*.rb' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'

%build
%ruby_config
%ruby_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}
%ruby_install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*.rb
%{ruby_rubylibdir}/mongrel
%attr(755,root,root) %{ruby_archdir}/*.so

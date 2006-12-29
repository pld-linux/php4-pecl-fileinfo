%define		_modname	fileinfo
%define		_smodname	Fileinfo
%define		_status		beta
Summary:	%{_modname} - libmagic bindings
Summary(pl):	%{_modname} - dowi±zania biblioteki libmagic
Name:		php4-pecl-%{_modname}
Version:	1.0.4
Release:	2
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_smodname}-%{version}.tgz
# Source0-md5:	2854e749db157365c769cb9496f5586f
Patch0:		pecl-fileinfo-defaultdb.patch
URL:		http://pecl.php.net/package/Fileinfo/
BuildRequires:	php4-devel >= 3:4.3.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php4-common >= 3:4.4.0-3
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension allows retrieval of information regarding vast majority
of file. This information may include dimensions, quality, length
etc...

Additionally it can also be used to retrieve the MIME type for a
particular file and for text files proper language encoding.

In PECL status of this extension is: %{_status}.

%description -l pl
To rozszerzenie pozwala na uzyskanie wielu informacji na temat plików.
Informacje te uwzglêdniaj± miêdzy innymi rozmiar, jako¶æ, d³ugo¶æ itp.

Dodatkowo mo¿e byæ u¿yte do uzyskania typu MIME danego pliku, a dla
plików tekstowych - u¿ytego kodowania.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c
%patch0 -p1

%build
cd %{_smodname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/conf.d,%{extensionsdir}}
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_smodname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php4_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php4_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc %{_smodname}-%{version}/{CREDITS,EXPERIMENTAL,fileinfo.php}
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so

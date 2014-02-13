%define		_name	AnonymousPro
Summary:	A set of fixed-width fonts designed with coding in mind
Name:		fonts-TTF-%{_name}
Version:	1.002
Release:	1
License:	OFL
Group:		Fonts
Source0:	http://www.marksimonson.com/assets/content/fonts/AnonymousPro-%{version}.zip
# Source0-md5:	bb5141b20b9d69b3190be03e5706c8b7
Source1:	%{name}-fontconfig.conf
URL:		http://www.marksimonson.com/fonts/view/anonymous-pro
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         ttffontsdir     %{_fontsdir}/TTF

%description
Anonymous Pro (2009) is a family of four fixed-width fonts designed
with coding in mind. Anonymous Pro features an international,
Unicode-based character set, with support for most Western and Central
European Latin-based languages, plus Greek and Cyrillic. Anonymous Pro
is based on an earlier font, Anonymous(TM) (2001), my TrueType version
of Anonymous 9, a Macintosh bitmap font developed in the mid-’90s by
Susan Lesch and David Lamkins.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_name}-%{version}.*

install -d $RPM_BUILD_ROOT{%{ttffontsdir},%{_datadir}/fontconfig/conf.avail,%{_sysconfdir}/fonts/conf.d}

install -p *.ttf $RPM_BUILD_ROOT%{ttffontsdir}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/%{name}.conf
ln -s %{_datadir}/fontconfig/conf.avail/%{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d/

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{ttffontsdir}/*.ttf
%{_sysconfdir}/fonts/conf.d/%{name}.conf
%{_datadir}/fontconfig/conf.avail/%{name}.conf

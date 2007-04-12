%define	name	sdlBasic
%define	version	20040425
%define	release	2
%define	Summary	A small, efficient and multiplatform basic interpreter

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
URL:		http://sdlbasic.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
License:	LGPL
Group:		Development/Other
Summary:	%{Summary}
BuildRequires:	SDL-devel SDL_mixer-devel SDL_image-devel SDL_ttf-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A easy basic in order to make games in 2d style amos for linux and windows.
The basic it comprises a module runtime, ide examples and games.

%prep
%setup -q -n %{name}
perl -pi -e "s#/usr/local/bin#%{_bindir}#g" clickme.sdlbas
chmod 755 clickme.sdlbas

%build
%make CFLAG="$RPM_OPT_FLAGS `sdl-config --cflags` -DPLAY_MOD -DUNIX" -C src

%install
rm -rf $RPM_BUILD_ROOT

install -m755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m644 setup/VeraMono.ttf -D $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/vera/VeraMono.ttf
install -m644 setup/Vera.ttf -D $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/vera/Vera.ttf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/* clickme.sdlbas lizard.mod sdlBasic.bmp sdlBasic.gif sdlBasic.png sdlBasic.xpm sdlnow.gif
%{_bindir}/%{name}
%{_datadir}/fonts/ttf



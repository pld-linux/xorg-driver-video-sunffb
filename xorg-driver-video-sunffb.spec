Summary:	X.org video driver for Sun Creator, Creator 3D and Elite 3D video cards
Summary(pl.UTF-8):	Sterownik obrazu X.org dla kart graficznych Sun Creator, Creator 3D i Elite 3D
Name:		xorg-driver-video-sunffb
Version:	1.2.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-sunffb-%{version}.tar.xz
# Source0-md5:	095c56ee2c4c4259ab6900e55d8f7882
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.0.99.901
Provides:	xorg-driver-video
Obsoletes:	X11-driver-sunffb < 1:7.0.0
Obsoletes:	XFree86-driver-sunffb < 1:7.0.0
ExclusiveArch:	sparc sparcv9 sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Sun Creator, Creator 3D and Elite 3D video
cards.

%description -l pl.UTF-8
Sterownik obrazu X.org dla kart graficznych Sun Creator, Creator 3D i
Elite 3D.

%prep
%setup -q -n xf86-video-sunffb-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/sunffb_drv.so
%{_mandir}/man4/sunffb.4*
